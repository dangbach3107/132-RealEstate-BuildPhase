# Product Requirements Document (PRD)

**Dự án:** AI Định Giá Căn Hộ Đại Đô Thị (HomeValue AI)  
**Tầm nhìn:** Trở thành nền tảng định giá và phân tích thị trường thứ cấp đáng tin cậy nhất dành riêng cho các Đại Đô Thị tại Việt Nam.

---

## 1. Mục Đích & Phạm Vi Dự Án (Project Scope)
Dự án hướng tới việc giải quyết bài toán định giá ảo trên thị trường mua bán/cho thuê lại căn hộ tại **tất cả các Đại đô thị lớn** (Ví dụ: Vinhomes Ocean Park, Smart City, Grand Park, Central Park, Ecopark...).

Dự án cung cấp một bộ công cụ sử dụng Trí tuệ nhân tạo (Machine Learning & LLM) để:
- Định giá trị thực của căn hộ dựa trên các đặc điểm vi mô (Tầng, View, Nội thất, Phân khu).
- Cung cấp lý do giải thích mức giá minh bạch (Explainable AI).
- Theo dõi biến động và xu hướng giá theo thời gian thực (Market Trends).

## 2. Các Tính Năng Cốt Lõi (Core Features)

### Epic 1: Giao Diện Người Dùng (User Experience)
- **F1. Form Định Giá Đa Năng:**
  - Chọn Đại đô thị (VOP, Smart City, Grand Park...).
  - Nhập liệu chi tiết: Diện tích, Số phòng ngủ/WC, Khoảng tầng, Tầm View (động theo từng đại đô thị), Tình trạng nội thất, Hướng ban công.
- **F2. Báo Cáo Định Giá Chi Tiết (Valuation Dashboard):**
  - Hiển thị mức giá ước tính (Bán / Cho Thuê).
  - Biểu đồ phân bố độ tin cậy (Confidence Interval).
- **F3. Khối Giải Thích AI (Explainable AI):**
  - Tích hợp LLM sinh ra đoạn văn 3-4 câu giải thích logic tại sao lại có mức giá đó dựa trên tiện ích nội khu và dữ liệu thị trường hiện tại.
- **F4. Dashboard Xu Hướng Thị Trường (Market Trends):**
  - Biểu đồ Line chart thể hiện lịch sử biến động giá (m2) của từng phân khu qua các tháng.
  - So sánh mức chênh lệch giữa "Giá rao bán" và "Giá giao dịch thực".

### Epic 2: Quản Lý Người Dùng & Dữ Liệu (User & Data Management)
- **F5. Authentication & Profiles:**
  - Đăng nhập/Đăng ký qua Email/Google.
  - Phân quyền: Cư dân (User) & Môi giới/Admin (Pro User).
- **F6. Lịch Sử & Theo Dõi Định Giá (Tracking):**
  - Lưu lại các căn hộ đã định giá.
  - Bật cảnh báo (Alert) khi giá trung bình của tòa nhà đó thay đổi.

### Epic 3: Lõi AI Định Giá (AI Engine)
- **F7. Multi-City ML Models:**
  - Huấn luyện nhiều mô hình ML (`RandomForest`, `XGBoost`) độc lập cho từng Đại đô thị để đảm bảo độ chính xác vi mô cao nhất (R2 Score >= 0.85).
- **F8. Automated Data Pipeline:**
  - Hệ thống tự động crawl dữ liệu tin rao mới hàng tuần từ Batdongsan, Nhatot.
  - Tự động làm sạch, dán nhãn và tái huấn luyện (Retrain) mô hình hàng tháng.

## 3. Lộ Trình Phát Triển (Product Roadmap)

### Phase 1: MVP (Minimum Viable Product)
*Chứng minh tính khả thi của mô hình AI.*
- **Scope:** Tập trung **duy nhất 1 Đại đô thị (Vinhomes Ocean Park 1)**.
- **Features:** Hoàn thiện F1, F2, F3, F5, F7 cho VOP1. Dữ liệu tĩnh thu thập 1 lần. Chạy web dạng Public không cần Login.

### Phase 2: User Expansion & Market Trends
*Mở rộng người dùng và tính năng theo dõi.*
- **Scope:** Mở rộng ra Vinhomes Smart City và Grand Park.
- **Features:** Hoàn thiện F4, F5, F6. Ra mắt hệ thống đăng nhập và lưu lịch sử.

### Phase 3: Automation & B2B Integration
*Tự động hóa hoàn toàn và thương mại hóa.*
- **Scope:** Tất cả các Đại đô thị lớn toàn quốc.
- **Features:** Triển khai F8 (Tự động crawl & retrain). Cung cấp API định giá cho các sàn giao dịch Bất động sản (B2B).

## 4. Kiến Trúc Kỹ Thuật (Tech Stack)
- **Frontend:** Next.js (React), TailwindCSS, TypeScript, Shadcn/UI, Recharts (Vẽ biểu đồ).
- **Backend:** FastAPI (Python) cho ML/AI, Node.js/Supabase cho User Auth & Database.
- **Machine Learning:** Scikit-learn, XGBoost, Pandas.
- **LLM Integration:** OpenAI API (GPT-4o-mini).
- **Database:** PostgreSQL (Supabase).
- **Hosting/Deployment:** Vercel (Frontend), Render/Railway (Backend Python API).
