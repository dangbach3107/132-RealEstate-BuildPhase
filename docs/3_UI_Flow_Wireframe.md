# Wireframe & UI Flow

**Dự án:** AI Định Giá Căn Hộ Đại Đô Thị  

---

## 1. Bản Vẽ Trực Quan (UI Mockup)
Dưới đây là bản vẽ phác thảo giao diện Web App cho MVP, được thiết kế theo phong cách Dark Mode hiện đại, chuyên nghiệp dành cho PropTech.

![UI Mockup](/Users/ngocbach/.gemini/antigravity-ide/brain/610c4f80-8fd1-414f-9542-65b73cc60d82/ui_mockup_realestate_1781000136504.png)

## 2. Sơ Đồ Luồng Người Dùng (User Flow)
Luồng thao tác từ lúc người dùng (Cư dân/Môi giới) truy cập web cho đến khi nhận được kết quả định giá AI.

```mermaid
sequenceDiagram
    actor User as Khách Hàng
    participant UI as Web Frontend (Next.js)
    participant API as FastAPI Backend
    participant ML as Machine Learning Model
    participant LLM as OpenAI (ChatGPT)

    User->>UI: Truy cập ứng dụng & chọn Vinhomes Ocean Park
    UI->>User: Hiển thị Form nhập liệu
    User->>UI: Nhập (Diện tích, Tầng, View, Nội thất...)
    User->>UI: Bấm nút "Định Giá Căn Hộ"
    UI->>API: Gửi POST Request chứa thông số
    API->>ML: Trích xuất Features & Mã hóa (Encode)
    ML-->>API: Trả kết quả dự đoán (Ví dụ: 2.5 Tỷ)
    API->>LLM: Gửi Prompt (Thông số + Giá dự đoán)
    LLM-->>API: Trả đoạn văn bản giải thích
    API-->>UI: Trả JSON {giá_tiền, text_giải_thích}
    UI-->>User: Hiển thị Result Card & AI Explanation Box
```

## 3. Đặc Tả Giao Diện (Wireframe Description)

Giao diện (như hình Mockup) được chia làm 2 phân khu chính để tối ưu hóa trải nghiệm trên một màn hình duy nhất (Single Page Dashboard).

### Khu vực trái: Input Panel (Form Nhập Liệu)
- **Style:** Glassmorphism, bo góc mềm mại.
- **Components:**
  - Dropdown chọn Phân khu (Sapphire, Zenpark...).
  - Input số: Diện tích.
  - Dropdown: Tầm view (Nội khu, Hồ...).
  - Button Action: "Get Valuation" (Hiệu ứng Gradient Teal nổi bật).

### Khu vực phải: Output Panel (Dashboard Kết Quả)
- **Top Card (Giá Trị Cốt Lõi):**
  - Text siêu to khổng lồ hiển thị giá trị dự đoán: **2.5 Tỷ VNĐ**.
  - Bên dưới là đồ thị hình chuông (Bell Curve) hiển thị khoảng tin cậy (Confidence Range) để giúp người dùng hiểu rằng giá nhà dao động theo cung cầu.
- **Bottom Card (Explainable AI):**
  - Chứa logo Robot AI nhỏ báo hiệu đây là text tự sinh.
  - Box nội dung: Giải thích rành mạch tại sao căn hộ này lại có giá đó (ví dụ: nhờ view đẹp, thiết kế cao cấp của Zenpark...).
