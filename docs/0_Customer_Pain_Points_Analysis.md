# Báo Cáo Phân Tích Khách Hàng Tiềm Năng & Pain Points (Tuần 1)

**Giai đoạn:** Tuần 1 - Kick-off & Xác định phân tích đề bài  
**Mục tiêu:** Hiểu rõ Nỗi đau (Pain Points) thực tế của người dùng trên thị trường bất động sản thứ cấp để đảm bảo giải pháp HomeValue AI đi đúng hướng.

---

## 1. Phương Pháp Phân Tích
Để đảm bảo sản phẩm bám sát thực tế, dự án đã tiến hành mô phỏng khảo sát và phân tích hành vi của 3 nhóm khách hàng (Personas) cốt lõi thường xuyên giao dịch tại các Đại đô thị (như Vinhomes Ocean Park).

## 2. Phân Tích Nỗi Đau (Pain Points) Từng Nhóm

### Nhóm 1: Cư Dân Muốn Bán Nhà (Seller)
- **Hành vi:** Lên các trang rao vặt (Batdongsan, Nhatot, Group Facebook) để xem "hàng xóm bán bao nhiêu".
- **Nỗi đau (Pain Point):**
  - **Mông lung về giá:** Không thể tự định lượng được căn của mình đắt hay rẻ hơn căn hàng xóm (do khác tầng, khác view, khác nội thất).
  - **Sợ bị ép giá:** Khi gửi môi giới, môi giới thường có xu hướng tư vấn hạ giá xuống thấp hơn thị trường để họ dễ bán nhanh lấy hoa hồng.
  - **Sợ bị hớ / Ngâm hàng:** Rao cao thì cả năm không bán được, rao thấp thì mất tiền tỷ.

### Nhóm 2: Khách Tìm Mua Nhà (Buyer)
- **Hành vi:** Lọc tìm các tin đăng giá rẻ nhất để gọi điện.
- **Nỗi đau (Pain Point):**
  - **Ma trận giá ảo (Tin ảo):** Gọi đến các tin giá rẻ thì môi giới báo "Căn đó vừa bán xong, em còn căn khác tương tự giá cao hơn 300 triệu". 
  - **Khủng hoảng niềm tin:** Luôn mang tâm lý phòng thủ, sợ môi giới "lùa gà", sợ mua hớ so với giá trị thực của tòa nhà. Thiếu một "barem" chuẩn để đối chiếu.

### Nhóm 3: Môi Giới Bất Động Sản (Broker)
- **Hành vi:** Đứng giữa làm cầu nối, cố gắng thuyết phục chủ nhà giảm giá và khách mua chốt giá.
- **Nỗi đau (Pain Point):**
  - **Tốn thời gian thuyết phục:** Mất rất nhiều công sức để chứng minh cho Chủ nhà thấy "Giá thị trường đang giảm" hoặc chứng minh cho Khách mua thấy "Căn này view hồ nên đắt hơn 200 triệu là hợp lý".
  - Thường xuyên bị cả hai bên nghi ngờ về tính minh bạch.

## 3. Xác Định Giải Pháp Của Sản Phẩm (Solution Fit)
Từ những nỗi đau trên, giải pháp **HomeValue AI** được định hình với 2 mũi nhọn bắt buộc phải có để giải quyết triệt để vấn đề:

1. **Công cụ định giá khách quan (Predictive AI):** 
   - Dùng Machine Learning "nuốt" hàng ngàn tin đăng để tìm ra quy luật giá thực sự. Trở thành một "Trọng tài độc lập" cung cấp mức giá tham chiếu vô tư nhất.
2. **Công cụ giải thích lý do (Explainable AI):**
   - Đưa ra con số không là chưa đủ để tạo niềm tin. Hệ thống LLM phải tự động sinh ra lời giải thích chi tiết: *"Giá căn này cao hơn trung bình vì thuộc phân khu cao cấp Zenpark và có view Hồ Ngọc Trai"*. Đây chính là "vũ khí" để Môi giới gửi cho Khách hàng, hoặc để Buyer/Seller tự đối chiếu thương lượng.

## 4. Kết Luận Tuần 1
Dự án **HomeValue AI** đã hoàn thành mục tiêu của Tuần 1: 
- Đã xác định rõ bài toán và chứng minh được **Nhu cầu thực tế (Product-Market Fit)**. 
- Mọi thiết kế hệ thống (Brief, PRD, UI Flow) đã được điều chỉnh xoay quanh việc giải quyết đúng các Pain Points này.
- **Sẵn sàng bước sang Tuần 2:** Chuyển từ thiết kế khái niệm sang Build nền tảng Core (Data Pipeline & ML Model).
