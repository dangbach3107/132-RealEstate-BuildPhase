# PM Worksheet - HomeValue AI

File này dùng để team cập nhật thông tin quan trọng của dự án ở một nơi dễ đọc, dễ theo dõi và dễ review trên GitHub.

Quy ước cập nhật:
- `Trạng thái`: Chưa làm, Đang làm, Đang review, Bị chặn, Đã xong, Đang mở, Đã giảm rủi ro
- `Ưu tiên`: P0 là gấp/ảnh hưởng demo hoặc vận hành, P1 quan trọng, P2 nên làm, P3 nice-to-have
- Mỗi task quan trọng nên có link PR/issue/doc/demo nếu có.
- Owner cập nhật tối thiểu mỗi ngày làm việc hoặc sau mỗi thay đổi lớn.

## 01. Tổng Quan Dự Án

| Hạng mục | Nội dung | Owner | Cập nhật lần cuối | Ghi chú |
|---|---|---|---|---|
| Tên dự án | HomeValue AI - Định giá BĐS Vinhomes Hà Nội | PM |  |  |
| Mục tiêu sản phẩm | Hỗ trợ định giá bán/thuê, xem xu hướng thị trường và giải thích kết quả bằng chatbot tự nhiên. | PM |  | Cần bổ sung success metrics cụ thể. |
| Người dùng mục tiêu | Người mua/bán/thuê, môi giới, team vận hành dữ liệu, người demo sản phẩm. | PM |  | Có thể tách persona chi tiết hơn. |
| Use case chính | Định giá bán/thuê, hỏi thông tin còn thiếu, xem trend, tra snapshot giá, giải thích yếu tố ảnh hưởng giá. | PM |  |  |
| Giai đoạn hiện tại | Build phase | PM |  | Đang hoàn thiện dữ liệu, API, chatbot answer quality và tracking PM. |
| Phạm vi backend chính | `data_analysis/` | Tech Lead |  | FastAPI, valuation logic, storage, crawler, prompt chatbot. |
| Nguồn dữ liệu hiện tại | Listing/snapshot crawl + SQLite local, có kế hoạch dùng MongoDB production. | Data/Backend |  | Verified transaction hiện cần nhập thêm. |
| Demo/production URL |  | Tech Lead |  | Cần team điền. |
| GitHub repository |  | Tech Lead |  | Cần team điền. |
| Ưu tiên hiện tại | Tập trung answer quality, quản lý PM sheet, dữ liệu thật/verified transaction, demo readiness. | PM |  |  |
| Milestone tiếp theo | Chuẩn hóa thông tin PM + hoàn thiện demo flow end-to-end. | PM |  |  |

## 02. Việc Đã Hoàn Thành

| ID | Nhóm việc | Việc đã làm | Kết quả/Deliverable | File/đường dẫn liên quan | Owner | Trạng thái | Ghi chú |
|---|---|---|---|---|---|---|---|
| DONE-001 | Chatbot | Bỏ trả lời định giá hardcode trực tiếp. | Luồng định giá đủ dữ liệu gọi `generate_answer("valuation", ...)` để LLM viết câu trả lời tự nhiên hơn. | `app/chatbot.py` | Backend | Đã xong | Hardcode cũ vẫn được giữ làm ví dụ/fallback. |
| DONE-002 | Chatbot | Biến câu trả lời hardcode cũ thành `example_answer`. | LLM nhận bản nháp cũ trong context và dùng như ví dụ về số liệu/ý chính, không copy máy móc. | `app/chatbot.py`, `prompts/chatbot_system.md` | Backend | Đã xong | Giữ an toàn số liệu P10/P50/P90/sample/confidence. |
| DONE-003 | Chatbot | Thêm prompt rule cho LLM viết tự nhiên hơn. | System prompt nói rõ `example_answer` chỉ là bản nháp, cần viết lại tự nhiên. | `prompts/chatbot_system.md` | Backend | Đã xong | Không nhắc implementation/API/prompt với người dùng cuối. |
| DONE-004 | Chatbot | Thêm đa dạng hóa cách trả lời. | Mỗi lần gọi LLM có `response_style` ngẫu nhiên như direct, consultative, compact, analytical, next_step. | `app/llm.py` | Backend | Đã xong | Giúp câu trả lời bớt cùng một khuôn. |
| DONE-005 | Chatbot | Tăng độ sáng tạo mặc định khi model hỗ trợ temperature. | `OPENAI_TEMPERATURE` default từ `0.2` lên `0.55`; `.env.example` cũng cập nhật. | `app/llm.py`, `.env.example` | Backend | Đã xong | Với GPT-5 style model không set temperature thì vẫn dùng style hint. |
| DONE-006 | Chatbot | Giữ fallback khi không bật LLM hoặc thiếu API key/model. | Nếu LLM lỗi/tắt, API vẫn trả lời được bằng fallback deterministic. | `prompts/fallback_answers.yaml`, `app/llm.py` | Backend | Đã xong | Local/test không bị phụ thuộc OpenAI. |
| DONE-007 | Test | Thêm test bảo vệ luồng định giá đi qua LLM prompt. | Test xác nhận valuation gọi `generate_answer`, có `example_answer`, và sample size khớp valuation result. | `tests/test_api.py` | Backend | Đã xong | Test chạy trực tiếp `handle_chat` để tránh vấn đề TestClient trong env hiện tại. |
| DONE-008 | Verification | Chạy kiểm tra compile và test chính. | `python -m py_compile app/llm.py app/chatbot.py` pass; test `test_chat_valuation_routes_answer_through_llm_prompt` pass. | Terminal/test log | Backend | Đã xong | Full TestClient API test đang bị treo ở starlette/anyio trong môi trường này. |
| DONE-009 | PM | Tạo PM worksheet bản Markdown. | Team có file quản lý project ngay trong repo/GitHub. | `PM_WORKSHEET.md` | PM/Backend | Đã xong | Bản này đang được Việt hóa và chi tiết hóa. |
| DONE-010 | PM | Tạo PM worksheet bản Excel. | Có workbook nhiều tab, freeze header, filter và dropdown để nhập liệu. | `PM_Worksheet.xlsx` | PM/Backend | Đã xong | Đã có các tab overview, ownership, milestones, task, risks, links. |
| DONE-011 | Storage/Plan | Lập plan chuyển storage sang MongoDB production, SQLite fallback local. | Có plan mô tả backend auto/mongo/sqlite, migration, test plan và assumption. | `../plan.md` | Backend/Data | Đã xong | Cần team quyết định owner/import verified transactions. |

## 03. Team & Trách Nhiệm

| Vai trò | Tên | GitHub | Liên hệ | Trách nhiệm chính | Backup | Trạng thái | Ghi chú |
|---|---|---|---|---|---|---|---|
| PM |  |  |  | Quản lý scope, timeline, milestone, quyết định ưu tiên, cập nhật worksheet. |  | Chưa điền |  |
| Tech Lead |  |  |  | Kiến trúc, review code, release readiness, quản lý rủi ro kỹ thuật. |  | Chưa điền |  |
| Backend |  |  |  | FastAPI, valuation logic, chatbot prompt/LLM, storage abstraction. |  | Chưa điền |  |
| Data |  |  |  | Crawl/import data, kiểm tra chất lượng listing/snapshot/transaction. |  | Chưa điền |  |
| Frontend |  |  |  | UI chatbot, luồng người dùng, hiển thị valuation/trend/snapshot. |  | Chưa điền |  |
| QA/Demo |  |  |  | Test case, demo script, kiểm tra bug trước demo. |  | Chưa điền |  |

## 04. Milestone

| Milestone | Mục tiêu | Owner | Ngày bắt đầu | Deadline | Trạng thái | Tiến độ % | Deliverable | Link | Blocker | Ghi chú |
|---|---|---|---|---|---|---:|---|---|---|---|
| M1 - Data foundation | Có dữ liệu listing/snapshot đủ để valuation chạy ổn. | Data |  |  | Đang làm |  | CSV/SQLite/Mongo collections, data quality report |  | Thiếu verified transaction |  |
| M2 - Valuation API | API định giá, trend, snapshot ổn định và có fallback lỗi rõ ràng. | Backend |  |  | Đang làm |  | `/valuation`, `/market-trends`, `/price-snapshots`, `/chat` |  | TestClient env đang cần kiểm tra thêm |  |
| M3 - Chatbot answer quality | Chatbot trả lời tự nhiên, không hardcode máy móc, giữ đúng số liệu. | Backend |  |  | Đã xong phần chính |  | LLM context, style hint, fallback, prompt guardrails |  | Cần test thực tế với API key/model |  |
| M4 - PM tracking | Team có sheet chung để nhập owner, milestone, task, risk, link demo. | PM |  |  | Đã xong bản đầu |  | Markdown + Excel worksheet |  | Cần team điền dữ liệu thật |  |
| M5 - Demo readiness | Có demo flow end-to-end, data sample tốt, script trình bày rõ. | PM/QA |  |  | Chưa làm |  | Demo checklist, bug list, expected answers |  | Cần chốt deadline/demo owner |  |

## 05. Task Tracker

| ID | Nhóm | Task | Owner | Ưu tiên | Trạng thái | Ngày bắt đầu | Deadline | Link PR/Issue | Phụ thuộc | Acceptance Criteria | Ghi chú |
|---|---|---|---|---|---|---|---|---|---|---|---|
| T-001 | Chatbot | Chuyển câu trả lời định giá hardcode sang LLM generate. | Backend | P1 | Đã xong |  |  |  | LLM config | Người dùng nhận câu trả lời do LLM viết từ context valuation. | Fallback vẫn hoạt động. |
| T-002 | Chatbot | Dùng hardcode cũ làm ví dụ cho LLM. | Backend | P1 | Đã xong |  |  |  | T-001 | Context có `example_answer`, prompt yêu cầu rewrite tự nhiên. |  |
| T-003 | Chatbot | Làm câu trả lời đa dạng hơn. | Backend | P2 | Đã xong |  |  |  | T-001 | Có response style hint và temperature mặc định cao hơn. | Cần kiểm thử với API key thật. |
| T-004 | PM | Tạo PM worksheet để team cập nhật thông tin dự án. | PM/Backend | P0 | Đã xong |  |  |  |  | Có `.md` và `.xlsx` trong repo. | Đang Việt hóa chi tiết. |
| T-005 | PM | Team điền owner, deadline, link repo/demo, success metrics. | PM | P0 | Chưa làm |  |  |  | PM worksheet | Không còn ô owner/deadline quan trọng bị trống. | Cần PM điều phối. |
| T-006 | Data | Thu thập/import verified transaction thật. | Data/PM | P0 | Đang mở |  |  |  | Nguồn giao dịch tin cậy | Có dữ liệu transaction đủ để calibration tốt hơn. | Rủi ro lớn nhất về độ chính xác. |
| T-007 | Storage | Chạy migration SQLite sang MongoDB khi có URI. | Backend/Data | P1 | Chưa làm |  |  |  | MongoDB URI | Mongo có đủ collections và count không duplicate khi chạy lại. | Đã có plan. |
| T-008 | QA | Viết demo checklist và expected Q&A. | QA/PM | P1 | Đã xong |  |  | `QA_TEST_CASES.md` | Demo scenario | Có test case manual để QA/PM tick pass/fail trước demo. | Cần team chạy và cập nhật trạng thái từng case. |

## 06. Data, Model & API Inventory

| Hạng mục | Loại | Owner | Trạng thái | Nguồn | Endpoint/Collection | Field quan trọng | Ghi chú chất lượng dữ liệu | Link | Ghi chú |
|---|---|---|---|---|---|---|---|---|---|
| Market listings | Data | Data | Đang có | Crawled listing pages | `listing_observation` | project, purpose, property_type, price, area, bedrooms | Dựa trên giá rao công khai đã lọc nhiễu, chưa phải giá chốt tuyệt đối. |  |  |
| Price snapshots | Data | Data | Đang có | Crawled/reference price pages | `price_snapshot` | project, type, range, observed_at | Dùng làm tham khảo, không trộn trực tiếp làm giao dịch chốt. |  |  |
| Verified transactions | Data | Data/PM | Thiếu | Manual/import | `verified_transaction` | transaction_price, rent, area, confidence | Cần nguồn dữ liệu thật để tăng độ tin cậy. |  | P0. |
| Chat endpoint | API | Backend | Đang có | FastAPI | `POST /chat` | message, property, answer, valuation, extracted | Đã có LLM rewrite + fallback. |  |  |
| Valuation endpoint | API | Backend | Đang có | FastAPI | `POST /valuation` | p10, p50, p90, confidence, comps | Dựa trên comparable listings + weighted quantile. |  |  |
| Trend endpoint | API | Backend | Đang có | FastAPI | `GET /market-trends` | median, p10, p90, windows | Cần đủ sample theo project/type. |  |  |
| Snapshot endpoint | API | Backend | Đang có | FastAPI | `GET /price-snapshots` | source, range, observed_at | Dùng để đối chiếu. |  |  |

## 07. Rủi Ro & Blocker

| ID | Rủi ro/Blocker | Ảnh hưởng | Khả năng | Owner | Cách xử lý | Deadline | Trạng thái | Cần quyết định gì | Ghi chú |
|---|---|---|---|---|---|---|---|---|---|
| R-001 | Thiếu verified transaction thật. | Cao | Trung bình | PM/Data | Chốt nguồn dữ liệu, import manual hoặc tạo form nhập transaction. |  | Đang mở | Ai sở hữu nguồn data thật? | Ảnh hưởng trực tiếp độ tin cậy valuation. |
| R-002 | LLM trả lời bị lặp khuôn hoặc khô. | Trung bình | Thấp | Backend | Đã thêm style hint, prompt rewrite và temperature 0.55. |  | Đã giảm rủi ro | Cần test thực tế với model production. |  |
| R-003 | Thông tin dự án rải rác trong GitHub/chat. | Trung bình | Trung bình | PM | Dùng worksheet này làm source of truth cho PM tracking. |  | Đã giảm rủi ro | Team cần duy trì cập nhật. |  |
| R-004 | TestClient trong môi trường hiện tại bị treo ở tầng starlette/anyio. | Trung bình | Trung bình | Backend | Dùng direct unit test cho logic mới; cần kiểm tra dependency/env nếu muốn chạy full API test. |  | Đang mở | Có cần fix env test ngay không? | Không thấy kẹt trong code app. |
| R-005 | Mongo production chưa migrate/chưa smoke test. | Cao | Trung bình | Backend/Data | Chạy migration khi có URI, kiểm tra idempotent và endpoint smoke. |  | Chưa làm | Chốt Mongo URI và người chạy migration. |  |

## 08. Quyết Định

| Ngày | Quyết định | Bối cảnh | Phương án đã cân nhắc | Owner | Ảnh hưởng | Link | Follow-up |
|---|---|---|---|---|---|---|---|
|  | Dùng LLM để viết câu trả lời cuối thay vì trả hardcode. | Câu trả lời cũ máy móc, khó tự nhiên. | Hardcode template, LLM rewrite từ context, full free-form LLM. | Backend | Tăng naturalness nhưng vẫn giữ số liệu trong context. |  | Test với API key/model thật. |
|  | Giữ fallback deterministic khi LLM tắt/lỗi. | Local/test không nên phụ thuộc OpenAI. | Fail request khi LLM lỗi, hoặc fallback. | Backend | App ổn định hơn. |  |  |
|  | Tạo PM worksheet trong repo. | Anh/team khó quản lý khi mọi thứ chỉ nằm trên GitHub. | Google Sheet ngoài repo, Excel trong repo, Markdown trong repo. | PM | Team có file chung dễ truy cập. |  | Team điền owner/deadline thật. |

## 09. Link & Demo

| Nhóm | Tên | URL/Path | Owner | Ghi chú truy cập | Lần kiểm tra cuối | Ghi chú |
|---|---|---|---|---|---|---|
| Repo | GitHub repository |  | Tech Lead | Cần điền link chính thức. |  |  |
| API | Local FastAPI | `http://127.0.0.1:8000` | Backend | Khi chạy server local. |  |  |
| Frontend | Local app | `http://localhost:5173` | Frontend | Khi chạy frontend dev server. |  |  |
| Docs | Architecture notes | `docs/architecture.md` | Tech Lead | Trong `data_analysis`. |  |  |
| PM | PM worksheet Markdown | `PM_WORKSHEET.md` | PM | Xem trực tiếp trên GitHub. |  |  |
| PM | PM worksheet Excel | `PM_Worksheet.xlsx` | PM | Dùng để nhập liệu dạng bảng. |  |  |

## 10. Việc Cần Làm Tiếp

| ID | Việc cần làm | Owner đề xuất | Ưu tiên | Trạng thái | Vì sao cần làm | Output mong muốn |
|---|---|---|---|---|---|---|
| NEXT-001 | Team điền đầy đủ owner, deadline, link repo/demo, success metrics. | PM | P0 | Chưa làm | Để worksheet thành source of truth thật, không chỉ là template. | Không còn ô trống ở project overview/team/milestone quan trọng. |
| NEXT-002 | Test LLM production với API key/model thật. | Backend | P1 | Chưa làm | Đảm bảo response style hoạt động và câu trả lời không bịa số liệu. | 5-10 câu hỏi mẫu + expected behavior. |
| NEXT-003 | Thu thập/import verified transaction thật. | Data/PM | P0 | Đang mở | Tăng độ tin cậy của valuation và giảm phụ thuộc listing price. | Dataset verified transaction có schema rõ và owner. |
| NEXT-004 | Chạy Mongo migration/smoke test khi có URI. | Backend/Data | P1 | Chưa làm | Production dùng MongoDB, cần đảm bảo dữ liệu lên đúng. | Migration report + endpoint smoke pass. |
| NEXT-005 | Chạy bộ test case demo trong `QA_TEST_CASES.md`. | QA/PM | P1 | Chưa chạy | Tránh demo lỗi flow hoặc câu trả lời không như kỳ vọng. | Test result pass/fail, bug list, action owner. |

## 11. Meeting Notes

| Ngày | Người tham gia | Tóm tắt | Action items | Owner | Deadline | Trạng thái | Ghi chú |
|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |
