const PRODUCTION_API_BASE = "https://apivinhomes.solanai.us";
const LOCAL_API_BASE = "http://127.0.0.1:8000";

const state = {
  apiBase: initialApiBase(),
  projects: [],
  latestValuation: null,
  chatHistory: [],
};

const CHAT_HISTORY_KEY = "homevalue_chat_history";
const MAX_CHAT_HISTORY = 120;

const purposeLabels = {
  sale: "Bán",
  rent: "Thuê",
};

const propertyTypeLabels = {
  apartment: "Căn hộ",
  villa: "Biệt thự",
  townhouse: "Liền kề",
  shophouse: "Shophouse",
  house: "Nhà phố",
  other: "Khác",
};

const confidenceLabels = {
  low: "Thấp",
  medium: "Trung bình",
  high: "Cao",
};

const trendLabels = {
  "1m": "1 tháng",
  "3m": "3 tháng",
  "6m": "6 tháng",
  "12m": "12 tháng",
};

const $ = (id) => document.getElementById(id);

function initialApiBase() {
  const localHostnames = new Set(["127.0.0.1", "localhost", "0.0.0.0", ""]);
  const isLocal = localHostnames.has(window.location.hostname);
  return isLocal ? LOCAL_API_BASE : PRODUCTION_API_BASE;
}

document.addEventListener("DOMContentLoaded", () => {
  state.chatHistory = loadChatHistory();
  bindEvents();
  renderChatHistory();
  drawValuationChart();
  boot();
});

function bindEvents() {
  $("samplePrompt").addEventListener("click", () => {
    $("chatMessage").value = "Định giá bán căn hộ Vinhomes Smart City 54.2m2 2PN full nội thất";
    $("chatMessage").focus();
  });

  $("clearChat").addEventListener("click", () => {
    state.chatHistory = [];
    saveChatHistory();
    renderChatHistory();
  });

  $("chatMessage").addEventListener("keydown", (event) => {
    if (event.key !== "Enter" || event.shiftKey || event.isComposing) return;
    event.preventDefault();
    if (typeof $("chatForm").requestSubmit === "function") {
      $("chatForm").requestSubmit();
    } else {
      $("chatForm").dispatchEvent(new Event("submit", { bubbles: true, cancelable: true }));
    }
  });

  $("resetForm").addEventListener("click", () => {
    $("valuationForm").reset();
    $("areaM2").value = "54.2";
    $("bedrooms").value = "2";
  });

  $("valuationForm").addEventListener("submit", async (event) => {
    event.preventDefault();
    const payload = readValuationForm();
    await runValuation(payload);
    await refreshMarket();
  });

  $("chatForm").addEventListener("submit", async (event) => {
    event.preventDefault();
    const message = $("chatMessage").value.trim();
    if (!message) return;
    $("chatMessage").value = "";
    appendMessage("user", message);
    await runChat(message);
  });

  $("refreshMarket").addEventListener("click", refreshMarket);
  $("project").addEventListener("change", refreshMarket);
  $("propertyType").addEventListener("change", refreshMarket);
  document.querySelectorAll("input[name='purpose']").forEach((input) => {
    input.addEventListener("change", refreshMarket);
  });
}

async function boot() {
  setApiStatus("wait", "Đang kiểm tra");
  try {
    await apiGet("/health");
    setApiStatus("ok", "API sẵn sàng");
    await loadProjects();
    await refreshMarket();
  } catch (error) {
    setApiStatus("bad", "API lỗi");
    appendMessage("bot", `Không kết nối được API: ${error.message}`, { save: false });
  }
  refreshIcons();
}

async function loadProjects() {
  const projects = await apiGet("/projects");
  state.projects = Array.isArray(projects) ? projects : [];
  const select = $("project");
  select.textContent = "";
  if (!state.projects.length) {
    const option = document.createElement("option");
    option.value = "";
    option.textContent = "Chưa có dự án";
    select.append(option);
    return;
  }

  state.projects.forEach((project) => {
    const option = document.createElement("option");
    option.value = project.slug;
    option.textContent = project.name;
    select.append(option);
  });

  const smartCity = state.projects.find((project) => project.slug === "vinhomes-smart-city");
  if (smartCity) select.value = smartCity.slug;
}

async function runChat(message) {
  setPanelLoading("chatLog", true);
  try {
    const response = await apiPost("/chat", { message });
    if (response.extracted) applyExtracted(response.extracted);
    appendBotResponse(response);

    if (response.valuation) {
      state.latestValuation = response.valuation;
      renderValuation(response.valuation);
      await refreshMarket();
    } else if (response.data?.windows) {
      renderTrends(response.data);
    }
  } catch (error) {
    appendMessage("bot", `Không xử lý được câu hỏi: ${error.message}`);
  } finally {
    setPanelLoading("chatLog", false);
  }
}

async function runValuation(payload) {
  setPanelLoading("runValuation", true);
  try {
    const valuation = await apiPost("/valuation", payload);
    state.latestValuation = valuation;
    renderValuation(valuation);
    appendMessage("bot", summarizeValuation(valuation));
  } catch (error) {
    appendMessage("bot", `Không định giá được: ${error.message}`);
  } finally {
    setPanelLoading("runValuation", false);
  }
}

async function refreshMarket() {
  const project = $("project").value;
  if (!project) return;
  const purpose = getPurpose();
  const propertyType = $("propertyType").value;
  const params = new URLSearchParams({
    project,
    purpose,
    property_type: propertyType,
  });

  setPanelLoading("refreshMarket", true);
  try {
    const trends = await apiGet(`/market-trends?${params.toString()}`);
    renderTrends(trends);
  } catch (error) {
    renderTrendError(error.message);
  } finally {
    setPanelLoading("refreshMarket", false);
  }
}

function readValuationForm() {
  const form = new FormData($("valuationForm"));
  const payload = {
    purpose: getPurpose(),
    project: form.get("project"),
    property_type: form.get("property_type"),
    area_m2: Number(form.get("area_m2")),
  };

  addNumber(payload, "bedrooms", form.get("bedrooms"));
  addString(payload, "view", form.get("view"));
  addString(payload, "furniture", form.get("furniture"));
  return payload;
}

function getPurpose() {
  return document.querySelector("input[name='purpose']:checked").value;
}

function addNumber(payload, key, value) {
  if (value === null || value === "") return;
  const number = Number(value);
  if (Number.isFinite(number)) payload[key] = number;
}

function addString(payload, key, value) {
  const text = String(value || "").trim();
  if (text) payload[key] = text;
}

function applyExtracted(extracted) {
  setValueIfPresent("areaM2", extracted.area_m2);
  setValueIfPresent("bedrooms", extracted.bedrooms);
  setValueIfPresent("view", extracted.view);
  setValueIfPresent("furniture", extracted.furniture);

  if (extracted.purpose) {
    const purposeInput = document.querySelector(`input[name='purpose'][value='${extracted.purpose}']`);
    if (purposeInput) purposeInput.checked = true;
  }
  if (extracted.property_type && $("propertyType").querySelector(`option[value='${extracted.property_type}']`)) {
    $("propertyType").value = extracted.property_type;
  }
  if (extracted.project) {
    const matchingProject = state.projects.find((project) => {
      const aliases = [project.slug, project.name, ...(project.aliases || [])].map(normalizeText);
      return aliases.includes(normalizeText(extracted.project));
    });
    if (matchingProject) $("project").value = matchingProject.slug;
  }
}

function setValueIfPresent(id, value) {
  if (value === null || value === undefined || value === "") return;
  const input = $(id);
  if (!input) return;
  input.value = value;
}

function appendBotResponse(response) {
  appendMessage("bot", response.answer || "Đã xử lý xong.", {
    missingFields: response.missing_fields || [],
  });
}

function appendMessage(role, text, options = {}) {
  const entry = {
    role,
    text,
    missingFields: options.missingFields || [],
    timestamp: options.timestamp || new Date().toISOString(),
  };
  renderChatEntry(entry);
  if (options.save !== false) {
    state.chatHistory.push(entry);
    trimChatHistory();
    saveChatHistory();
  }
  updateChatHistoryMeta();
}

function renderChatEntry(entry) {
  const intro = $("chatLog").querySelector(".chat-intro");
  if (intro) intro.remove();

  const wrapper = document.createElement("article");
  wrapper.className = `message ${entry.role}`;
  const avatar = document.createElement("span");
  avatar.className = "avatar";
  avatar.textContent = entry.role === "user" ? "Bạn" : "AI";
  const content = document.createElement("div");
  content.className = "bubble";
  renderMessageContent(content, entry.text, entry.role);

  if (Array.isArray(entry.missingFields) && entry.missingFields.length) {
    const list = document.createElement("ul");
    list.className = "missing-list";
    entry.missingFields.forEach((field) => {
      const item = document.createElement("li");
      item.textContent = field;
      list.append(item);
    });
    content.append(list);
  }

  const meta = document.createElement("span");
  meta.className = "message-meta";
  meta.textContent = formatMessageTime(entry.timestamp);
  content.append(meta);

  wrapper.append(avatar, content);
  $("chatLog").append(wrapper);
  scrollChatToBottom();
}

function renderChatHistory() {
  const log = $("chatLog");
  log.textContent = "";
  if (!state.chatHistory.length) {
    renderChatIntro();
  } else {
    state.chatHistory.forEach((entry) => renderChatEntry(entry));
  }
  updateChatHistoryMeta();
}

function renderChatIntro() {
  const intro = document.createElement("div");
  intro.className = "chat-intro";
  const title = document.createElement("strong");
  title.textContent = "Bắt đầu với một câu hỏi";
  const body = document.createElement("span");
  body.textContent = "Chọn một mẫu hoặc nhập trực tiếp câu hỏi của bạn.";
  const chips = document.createElement("div");
  chips.className = "prompt-chips";
  [
    "Định giá bán căn hộ Vinhomes Smart City 54m2 2PN full nội thất",
    "Giá thuê hợp lý căn hộ Vinhomes Ocean Park 2PN",
    "Xu hướng giá Ocean Park căn hộ bán",
  ].forEach((prompt) => {
    const button = document.createElement("button");
    button.type = "button";
    button.textContent = prompt;
    button.addEventListener("click", () => {
      $("chatMessage").value = prompt;
      $("chatMessage").focus();
    });
    chips.append(button);
  });
  intro.append(title, body, chips);
  $("chatLog").append(intro);
}

function renderMessageContent(container, text, role) {
  const lines = String(text || "")
    .split(/\r?\n/)
    .map((line) => line.trim())
    .filter(Boolean);
  if (role === "bot" && lines.length && lines.every((line) => /^[-*•]\s+/.test(line))) {
    const list = document.createElement("ul");
    list.className = "response-list";
    lines.forEach((line) => {
      const item = document.createElement("li");
      item.textContent = line.replace(/^[-*•]\s+/, "");
      list.append(item);
    });
    container.append(list);
    return;
  }
  container.textContent = text;
}

function loadChatHistory() {
  try {
    const parsed = JSON.parse(localStorage.getItem(CHAT_HISTORY_KEY) || "[]");
    if (!Array.isArray(parsed)) return [];
    return parsed
      .filter((entry) => entry && ["user", "bot"].includes(entry.role) && typeof entry.text === "string")
      .map((entry) => ({
        role: entry.role,
        text: entry.text,
        missingFields: Array.isArray(entry.missingFields) ? entry.missingFields : [],
        timestamp: entry.timestamp || new Date().toISOString(),
      }))
      .slice(-MAX_CHAT_HISTORY);
  } catch {
    return [];
  }
}

function saveChatHistory() {
  try {
    localStorage.setItem(CHAT_HISTORY_KEY, JSON.stringify(state.chatHistory));
  } catch {
    // Browser storage can be disabled or full; chat should still work for the current session.
  }
}

function trimChatHistory() {
  if (state.chatHistory.length > MAX_CHAT_HISTORY) {
    state.chatHistory = state.chatHistory.slice(-MAX_CHAT_HISTORY);
  }
}

function updateChatHistoryMeta() {
  const count = state.chatHistory.length;
  $("chatHistoryMeta").textContent = count
    ? `Đã lưu ${count} tin nhắn trên trình duyệt này.`
    : "Lịch sử chat được lưu trên trình duyệt này.";
}

function scrollChatToBottom() {
  const log = $("chatLog");
  log.scrollTop = log.scrollHeight;
}

function renderValuation(valuation) {
  const purpose = valuation.purpose || getPurpose();
  const project = valuation.project || currentProjectName();
  const typeLabel = propertyTypeLabels[valuation.property_type] || valuation.property_type || "BĐS";
  $("resultMeta").textContent = `${purposeLabels[purpose] || purpose} - ${project} - ${typeLabel}. ${valuation.caveat || ""}`;
  $("p10Value").textContent = formatTotal(valuation.p10_total_vnd, purpose);
  $("p50Value").textContent = formatTotal(valuation.p50_total_vnd, purpose);
  $("p90Value").textContent = formatTotal(valuation.p90_total_vnd, purpose);
  $("confidenceValue").textContent = confidenceLabels[valuation.confidence] || valuation.confidence || "-";
  $("sampleValue").textContent = `${valuation.sample_size ?? 0} mẫu`;
  $("freshnessValue").textContent = formatDateTime(valuation.data_freshness);

  renderFactors(valuation.top_factors || []);
  renderComps(valuation.comparable_listings || [], purpose);
  drawValuationChart(valuation);
}

function summarizeValuation(valuation) {
  const purpose = valuation.purpose || getPurpose();
  const ppm = valuation.p50_price_per_m2_vnd
    ? `, tương đương ${formatPricePerM2(valuation.p50_price_per_m2_vnd)}`
    : "";
  return `P50 hợp lý: ${formatTotal(valuation.p50_total_vnd, purpose)}${ppm}. Khoảng P10-P90: ${formatTotal(
    valuation.p10_total_vnd,
    purpose,
  )} đến ${formatTotal(valuation.p90_total_vnd, purpose)}. Mẫu so sánh: ${valuation.sample_size}.`;
}

function renderFactors(factors) {
  const list = $("factorList");
  list.textContent = "";
  if (!factors.length) {
    const item = document.createElement("li");
    item.textContent = "Chưa có yếu tố giải thích.";
    list.append(item);
    return;
  }
  factors.forEach((factor) => {
    const item = document.createElement("li");
    item.textContent = factor;
    list.append(item);
  });
}

function renderComps(comps, purpose) {
  const tbody = $("compRows");
  tbody.textContent = "";
  if (!comps.length) {
    appendEmptyRow(tbody, 6, "Chưa có căn so sánh.");
    return;
  }

  comps.forEach((comp) => {
    const row = document.createElement("tr");
    row.append(
      textCellWithLink(comp.title || "Tin chưa có tiêu đề", comp.source_url),
      textCell(comp.project || "-"),
      textCell(formatArea(comp.area_m2)),
      textCell(comp.bedrooms ?? "-"),
      textCell(formatComparablePrice(comp, purpose)),
      textCell(`${Math.round((comp.similarity_score || 0) * 100)}%`),
    );
    tbody.append(row);
  });
}

function renderTrends(trends) {
  const grid = $("trendGrid");
  grid.textContent = "";
  const windows = trends?.windows || {};
  const entries = Object.keys(trendLabels).map((key) => [key, windows[key]]);
  if (!entries.some(([, value]) => value)) {
    renderTrendError("Chưa có dữ liệu trend.");
    return;
  }

  entries.forEach(([key, value]) => {
    const cell = document.createElement("div");
    cell.className = "trend-cell";
    const label = document.createElement("span");
    label.textContent = trendLabels[key];
    const median = document.createElement("strong");
    median.textContent = value?.median ? formatTrendMetric(value.median, trends.purpose) : "-";
    const sample = document.createElement("small");
    sample.textContent = `${value?.sample_size || 0} mẫu - P10 ${formatTrendMetric(value?.p10, trends.purpose)} / P90 ${formatTrendMetric(
      value?.p90,
      trends.purpose,
    )}`;
    cell.append(label, median, sample);
    grid.append(cell);
  });
}

function renderTrendError(message) {
  const grid = $("trendGrid");
  grid.textContent = "";
  const empty = document.createElement("div");
  empty.className = "empty-state";
  empty.textContent = message;
  grid.append(empty);
}

function drawValuationChart(valuation) {
  const canvas = $("valuationChart");
  if (!canvas) return;
  const container = canvas.parentElement;
  const rect = container.getBoundingClientRect();
  const width = Math.max(320, rect.width);
  const height = Math.max(200, rect.height);
  const ratio = window.devicePixelRatio || 1;
  canvas.width = Math.round(width * ratio);
  canvas.height = Math.round(height * ratio);
  canvas.style.width = `${width}px`;
  canvas.style.height = `${height}px`;

  const ctx = canvas.getContext("2d");
  ctx.setTransform(ratio, 0, 0, ratio, 0, 0);
  ctx.clearRect(0, 0, width, height);
  ctx.fillStyle = "#ffffff";
  ctx.fillRect(0, 0, width, height);

  const values = valuation
    ? [valuation.p10_total_vnd, valuation.p50_total_vnd, valuation.p90_total_vnd].map(Number)
    : [];
  if (!values.length || values.some((value) => !Number.isFinite(value))) {
    drawEmptyChart(ctx, width, height);
    return;
  }

  const [p10, p50, p90] = values;
  const left = 42;
  const right = width - 24;
  const bottom = height - 42;
  const top = 28;
  const range = Math.max(p90 - p10, 1);
  const min = p10 - range * 0.45;
  const max = p90 + range * 0.45;
  const toX = (value) => left + ((value - min) / (max - min)) * (right - left);

  ctx.strokeStyle = "#dce3df";
  ctx.lineWidth = 1;
  ctx.beginPath();
  ctx.moveTo(left, bottom);
  ctx.lineTo(right, bottom);
  ctx.stroke();

  ctx.beginPath();
  const sigma = Math.max((p90 - p10) / 2.56, range / 4);
  const amplitude = bottom - top - 22;
  for (let i = 0; i <= 120; i += 1) {
    const x = left + ((right - left) * i) / 120;
    const value = min + ((max - min) * i) / 120;
    const z = (value - p50) / sigma;
    const y = bottom - Math.exp(-0.5 * z * z) * amplitude;
    if (i === 0) ctx.moveTo(x, y);
    else ctx.lineTo(x, y);
  }
  ctx.strokeStyle = "#0d7f73";
  ctx.lineWidth = 3;
  ctx.stroke();

  drawMarker(ctx, toX(p10), bottom, "P10", formatTotal(p10, valuation.purpose));
  drawMarker(ctx, toX(p50), bottom, "P50", formatTotal(p50, valuation.purpose), true);
  drawMarker(ctx, toX(p90), bottom, "P90", formatTotal(p90, valuation.purpose));
}

function drawEmptyChart(ctx, width, height) {
  ctx.strokeStyle = "#dce3df";
  ctx.lineWidth = 1;
  ctx.beginPath();
  ctx.moveTo(36, height - 42);
  ctx.lineTo(width - 24, height - 42);
  ctx.stroke();
  ctx.fillStyle = "#65716b";
  ctx.font = "14px sans-serif";
  ctx.fillText("Khoảng P10-P50-P90 sẽ hiện ở đây sau khi định giá.", 36, 72);
}

function drawMarker(ctx, x, bottom, label, value, isMain = false) {
  ctx.strokeStyle = isMain ? "#c95f44" : "#a67823";
  ctx.fillStyle = ctx.strokeStyle;
  ctx.lineWidth = isMain ? 2 : 1;
  ctx.beginPath();
  ctx.moveTo(x, 28);
  ctx.lineTo(x, bottom + 4);
  ctx.stroke();
  ctx.beginPath();
  ctx.arc(x, bottom, isMain ? 5 : 4, 0, Math.PI * 2);
  ctx.fill();
  ctx.font = isMain ? "700 12px sans-serif" : "12px sans-serif";
  ctx.fillText(label, x - 12, bottom + 22);
  ctx.font = "11px sans-serif";
  ctx.fillStyle = "#65716b";
  ctx.fillText(value, Math.max(8, Math.min(x - 34, ctx.canvas.width - 150)), bottom + 36);
}

async function apiGet(path) {
  return request(path);
}

async function apiPost(path, body) {
  return request(path, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(body),
  });
}

async function request(path, options = {}) {
  const url = `${state.apiBase}${path}`;
  const response = await fetch(url, options);
  let payload = null;
  const text = await response.text();
  if (text) {
    try {
      payload = JSON.parse(text);
    } catch {
      payload = text;
    }
  }
  if (!response.ok) {
    const detail = payload?.detail || payload || response.statusText;
    throw new Error(Array.isArray(detail) ? detail.map((item) => item.msg || item).join(", ") : detail);
  }
  return payload;
}

function setApiStatus(kind, text) {
  const status = $("apiStatus");
  status.className = `status-pill status-${kind}`;
  status.textContent = text;
}

function setPanelLoading(id, loading) {
  const element = $(id);
  if (!element) return;
  element.classList.toggle("is-loading", loading);
  if ("disabled" in element) element.disabled = loading;
}

function refreshIcons() {
  if (window.lucide) window.lucide.createIcons();
}

function currentProjectName() {
  const option = $("project").selectedOptions[0];
  return option ? option.textContent : "-";
}

function normalizeText(value) {
  return String(value || "")
    .normalize("NFD")
    .replace(/[\u0300-\u036f]/g, "")
    .toLowerCase()
    .trim();
}

function textCell(value) {
  const cell = document.createElement("td");
  cell.textContent = value === null || value === undefined || value === "" ? "-" : value;
  return cell;
}

function textCellWithLink(text, href) {
  const cell = document.createElement("td");
  if (href) {
    const link = document.createElement("a");
    link.href = href;
    link.target = "_blank";
    link.rel = "noreferrer";
    link.textContent = text;
    cell.append(link);
  } else {
    cell.textContent = text;
  }
  return cell;
}

function appendEmptyRow(tbody, colspan, message) {
  const row = document.createElement("tr");
  const cell = document.createElement("td");
  cell.colSpan = colspan;
  cell.textContent = message;
  row.append(cell);
  tbody.append(row);
}

function formatTotal(value, purpose = "sale") {
  if (!Number.isFinite(Number(value))) return "-";
  return purpose === "rent" ? `${formatCompactVnd(value)} / tháng` : formatCompactVnd(value);
}

function formatTrendMetric(value, purpose = "sale") {
  if (!Number.isFinite(Number(value))) return "-";
  return purpose === "rent" ? `${formatCompactVnd(value)} / tháng` : formatPricePerM2(value);
}

function formatComparablePrice(comp, purpose = "sale") {
  if (purpose === "rent") return formatTotal(comp.rent_monthly_vnd, "rent");
  const total = formatTotal(comp.price_total_vnd, "sale");
  const ppm = comp.price_per_m2_vnd ? ` (${formatPricePerM2(comp.price_per_m2_vnd)})` : "";
  return `${total}${ppm}`;
}

function formatArea(value) {
  return Number.isFinite(Number(value)) ? `${formatNumber(value)} m²` : "-";
}

function formatPricePerM2(value) {
  if (!Number.isFinite(Number(value))) return "-";
  return `${formatNumber(Number(value) / 1_000_000)} tr/m²`;
}

function formatCompactVnd(value) {
  const number = Number(value);
  if (!Number.isFinite(number)) return "-";
  if (Math.abs(number) >= 1_000_000_000) return `${formatNumber(number / 1_000_000_000)} tỷ`;
  if (Math.abs(number) >= 1_000_000) return `${formatNumber(number / 1_000_000)} triệu`;
  return `${new Intl.NumberFormat("vi-VN", { maximumFractionDigits: 0 }).format(number)} đ`;
}

function formatNumber(value) {
  return new Intl.NumberFormat("vi-VN", {
    maximumFractionDigits: 1,
  }).format(Number(value));
}

function formatDateTime(value) {
  if (!value) return "-";
  const date = new Date(value);
  if (Number.isNaN(date.getTime())) return "-";
  return new Intl.DateTimeFormat("vi-VN", {
    dateStyle: "short",
    timeStyle: "short",
  }).format(date);
}

function formatMessageTime(value) {
  const date = new Date(value);
  if (Number.isNaN(date.getTime())) return "";
  return new Intl.DateTimeFormat("vi-VN", {
    hour: "2-digit",
    minute: "2-digit",
    day: "2-digit",
    month: "2-digit",
  }).format(date);
}

window.addEventListener("resize", () => {
  drawValuationChart(state.latestValuation);
});
