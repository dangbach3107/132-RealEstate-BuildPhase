# HomeValue AI UI

Repo này hiện có frontend chạy được tại `frontend/`. UI gọi API định giá thật trong `/home/anonymous/VINUNI/buildphase/data_analysis`, không dùng lại các CSV cũ trong thư mục `data/` của repo này.

## Chạy nhanh

```bash
cd /home/anonymous/VINUNI/buildphase/data_analysis
python3 scripts/serve.py
```

```bash
cd /home/anonymous/VINUNI/buildphase/132-RealEstate-BuildPhase/frontend
python3 -m http.server 5173 --bind 127.0.0.1
```

Mở `http://127.0.0.1:5173`.
