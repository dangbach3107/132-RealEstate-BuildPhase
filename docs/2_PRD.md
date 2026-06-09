# Product Requirements Document (PRD)

**Dự án:** AI Định Giá Căn Hộ Đại Đô Thị  
**Giai đoạn:** MVP (Minimum Viable Product)  

---

## 1. Mục Đích & Phạm Vi (Scope)
Sản phẩm MVP sẽ tập trung giải quyết bài toán định giá cho **duy nhất 1 Đại đô thị: Vinhomes Ocean Park 1 (Hà Nội)** và 1 loại hình bất động sản: **Căn hộ chung cư bán/cho thuê**. Việc thu hẹp scope này nhằm đảm bảo tính đồng nhất của dữ liệu, giúp mô hình ML đạt độ chính xác (R2 Score) trên 80% chỉ với nguồn dữ liệu nhỏ gọn dưới 1000 mẫu.

## 2. Các Tính Năng Cốt Lõi (Core Features - MVP)

### Epic 1: Giao Diện Người Dùng (User Interface)
**Mục tiêu:** Cung cấp trải nghiệm mượt mà, tối giản để người dùng nhanh chóng nhập thông số và nhận kết quả.
- **F1. Form Nhập Liệu Căn Hộ:**
  - Dropdown: Phân khu (Sapphire, Zenpark, Pavilion, Ruby).
  - Number Input: Diện tích (m2), Số phòng ngủ (1, 2, 3+).
  - Dropdown: Khoảng tầng (Thấp, Trung, Cao).
  - Dropdown: Tầm View (Nội khu, Hồ Ngọc Trai, VinUni).
  - Dropdown: Tình trạng nội thất (Trống, Cơ bản, Full đồ).
- **F2. Trang Kết Quả Định Giá (Result Dashboard):**
  - Hiển thị mức giá ước tính (Ví dụ: 2.5 Tỷ VNĐ).
  - Hiển thị độ tin cậy (Confidence Interval) dạng khoảng giá (Ví dụ: 2.4 - 2.6 Tỷ).
- **F3. Khối Giải Thích AI (Explainable AI Box):**
  - Hiển thị một đoạn phân tích 3-4 câu từ chuyên gia AI (LLM) diễn giải vì sao lại có mức giá đó dựa trên tiện ích nội khu (Ví dụ: *"Căn của bạn ở mức giá cận cao do thuộc phân khu Zenpark với tiêu chuẩn Ruby, kết hợp với view Hồ Ngọc Trai đắt giá..."*).

### Epic 2: Lõi AI Định Giá (Predictive Engine)
**Mục tiêu:** Xử lý và dự đoán chính xác giá trị bất động sản.
- **F4. Data Pipeline:**
  - Tiền xử lý dữ liệu (Làm sạch chuỗi, mã hóa LabelEncoder cho các biến phân loại).
- **F5. Mô Hình ML:**
  - Sử dụng thuật toán `RandomForestRegressor` hoặc `XGBoost`.
  - Phải đạt tỷ lệ dự đoán chính xác (R2 Score) >= 0.75 trên tập Test (Dữ liệu VOP1).

### Epic 3: Giao Tiếp LLM (Explainability)
**Mục tiêu:** Kết nối kết quả ML với ngôn ngữ tự nhiên.
- **F6. API Integration:** 
  - Gửi Prompt động (Dynamic Prompt) bao gồm: Thông số nhà + Giá dự đoán từ ML tới OpenAI API (GPT-3.5 hoặc GPT-4o-mini).
  - Parse và trả kết quả văn bản về Frontend trong thời gian < 3 giây.

## 3. Kiến Trúc Kỹ Thuật (Tech Stack)
- **Frontend:** Next.js (React), TailwindCSS, TypeScript. (UI Framwork: Shadcn/UI). Vercel Hosting.
- **Backend (API + ML):** FastAPI (Python). Render hoặc Railway Hosting.
- **Machine Learning:** Scikit-learn (RandomForest), Pandas, Joblib.
- **LLM Integration:** Thư viện `openai` Python.
- **Cơ sở dữ liệu (Dự kiến Phase 2):** PostgreSQL (Supabase) để lưu lịch sử định giá của người dùng. (Phase MVP hiện tại chạy Stateless qua RAM).

## 4. Yêu Cầu Phi Chức Năng (Non-Functional Requirements)
- **Hiệu năng:** Tổng thời gian từ lúc bấm "Định giá" đến lúc hiện kết quả + text giải thích phải dưới 4 giây.
- **Responsive:** Giao diện web phải hiển thị hoàn hảo và dễ thao tác trên thiết bị Di động (Mobile-first design) vì 80% người mua/bán nhà dùng smartphone.
- **Độ ổn định:** Nếu API của OpenAI bị lỗi, hệ thống phải trả về kết quả giá tiền ML bình thường, kèm câu giải thích mẫu fallback, không được sập hoàn toàn (Graceful degradation).
