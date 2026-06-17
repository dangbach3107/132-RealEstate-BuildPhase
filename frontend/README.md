# HomeValue AI Frontend

Static UI cho MVP định giá Vinhomes Hà Nội. UI này không giữ dataset riêng và không hard-code giá; mọi dữ liệu dự án, định giá, trend và comps đều lấy từ API trong `/home/anonymous/VINUNI/buildphase/data_analysis`.

## Chạy local

Terminal 1:

```bash
cd /home/anonymous/VINUNI/buildphase/data_analysis
python3 scripts/serve.py
```

Terminal 2:

```bash
cd /home/anonymous/VINUNI/buildphase/132-RealEstate-BuildPhase/frontend
python3 -m http.server 5173 --bind 127.0.0.1
```

Mở `http://127.0.0.1:5173`.

## Chat UI

- `Enter`: gửi tin nhắn.
- `Shift+Enter`: xuống dòng.
- Lịch sử chat lưu trong `localStorage` của trình duyệt bằng key `homevalue_chat_history`.

## API

Mặc định UI gọi `http://127.0.0.1:8000`. API URL không hiển thị trên giao diện; nếu cần đổi môi trường, cập nhật `LOCAL_API_BASE` hoặc `PRODUCTION_API_BASE` trong `app.js`.
