# Vinhomes Hanoi Valuation MVP

MVP này crawl listing công khai từ Batdongsan, OneHousing, VinhomesLand và VinhomesOnline theo URL trong `config/projects.yaml`, tự follow pagination/filter links tìm thấy trong snapshot, lưu raw snapshot, chuẩn hóa dữ liệu vào MongoDB hoặc SQLite local fallback/CSV, rồi expose API/chatbot định giá bán/thuê bằng comparable listings + weighted quantile.

## Quick Start

```bash
cd /home/anonymous/VINUNI/buildphase/data_analysis
cp .env.example .env
python3 scripts/crawl.py --limit 8
python3 scripts/crawl.py --source onehousing --limit 31
python3 scripts/crawl.py --source vinhomesland --limit 4
pytest -q
python3 scripts/serve.py
```

API chạy local tại `http://127.0.0.1:8000`. Mặc định service chỉ listen trên localhost để không mở API ra LAN/public.

## Environment

Backend tự load `data_analysis/.env` trước khi đọc config. Không đưa key vào frontend hoặc source code.

```bash
OPENAI_API_KEY=...
MODEL=...
VALUATION_LLM_ENABLED=1
VALUATION_HOST=127.0.0.1
VALUATION_PORT=8000
VALUATION_STORAGE_BACKEND=auto
MONGODB_URI=
MONGODB_DB=homevalue_market
```

Storage backend:

- `VALUATION_STORAGE_BACKEND=auto` dùng MongoDB khi có `MONGODB_URI`, nếu không có thì fallback SQLite local.
- `VALUATION_STORAGE_BACKEND=mongo` bắt buộc có `MONGODB_URI`.
- `VALUATION_STORAGE_BACKEND=sqlite` ép dùng `data/market.sqlite`.

MongoDB chỉ thay lớp lưu trữ; thuật toán định giá hiện vẫn là comparable listings + weighted quantile. Chất lượng định giá vẫn phụ thuộc dữ liệu giao dịch thật/listing đã crawl.

Khi `OPENAI_API_KEY` và `MODEL` có trong `.env`, chatbot dùng OpenAI để viết lại phần giải thích từ dữ liệu valuation/trend/snapshot đã tính. Nếu thiếu key/model hoặc OpenAI lỗi, API tự fallback về câu trả lời deterministic.

Prompt nằm ở `prompts/`:

- `chatbot_system.md`: persona, guardrails, luật không bịa giá.
- `chatbot_user.md`: template truyền intent, tin nhắn người dùng và context JSON vào model.
- `fallback_answers.yaml`: câu trả lời dự phòng khi tắt LLM hoặc OpenAI lỗi.
- `intent_rules.yaml`: rule nhận diện intent đơn giản, tách khỏi code.

Có thể đổi prompt bằng env:

```bash
VALUATION_PROMPT_DIR=prompts
VALUATION_SYSTEM_PROMPT_PATH=
VALUATION_USER_PROMPT_PATH=
VALUATION_FALLBACK_PROMPT_PATH=
VALUATION_INTENT_RULES_PATH=
```

## Dữ Liệu Đầu Ra

- Raw crawl snapshots: `data/raw_html/*.md`
- Market DB local fallback: `data/market.sqlite`
- CSV đã chuẩn hóa: `data/processed/listings.csv`
- Bảng giá tham khảo: `data/processed/price_snapshots.csv`
- Candidate chưa map vào scope Vinhomes Hà Nội: `data/processed/property_candidates.csv`
- Config dự án/URL/ngưỡng chất lượng: `config/projects.yaml`

Hiện crawler đã lấy được data mới từ Batdongsan qua reader fallback vì direct `requests` bị Cloudflare 403. Crawler không bypass CAPTCHA; URL nào bị block sẽ được ghi `blocked=true` trong bảng `raw_fetch`.

OneHousing được crawl trực tiếp từ HTML public và parse `__NEXT_DATA__` structured inventory; không gọi các endpoint disallow trong `robots.txt`.

VinhomesLand được lưu vào `price_snapshot` vì nguồn này chủ yếu là bảng giá/range theo loại hình hoặc phân khu, không phải từng căn cụ thể. VinhomesOnline được lưu vào `property_candidate` nếu project name chưa match alias hiện tại, tránh hard-code mapping sai vào valuation.

Crawler có cache reuse: URL đã fetch sẽ đọc lại raw snapshot cũ, chỉ gọi mạng với URL mới. Các lần crawl sau sẽ đi sâu hơn mà không tốn thời gian tải lại trang đã có.

## API Chính

```bash
curl -X POST http://localhost:8000/valuation \
  -H 'Content-Type: application/json' \
  -d '{
    "project": "vinhomes-ocean-park",
    "purpose": "sale",
    "property_type": "apartment",
    "area_m2": 55,
    "bedrooms": 2,
    "furniture": "full"
  }'
```

Chatbot endpoint có thể nhận tiếng Việt tự nhiên hoặc structured `property`:

```bash
curl -X POST http://localhost:8000/chat \
  -H 'Content-Type: application/json' \
  -d '{"message":"Định giá bán căn hộ Vinhomes Smart City 54.2m2 2PN full nội thất"}'
```

```bash
curl -X POST http://localhost:8000/chat \
  -H 'Content-Type: application/json' \
  -d '{"message":"Xu hướng giá Vinhomes Ocean Park căn hộ bán thế nào?"}'
```

```bash
curl 'http://localhost:8000/market-trends?project=vinhomes-ocean-park&purpose=sale&property_type=apartment'
```

```bash
curl 'http://localhost:8000/price-snapshots?project=vinhomes-smart-city&property_type=apartment'
```

```bash
curl -X POST http://localhost:8000/verified-transactions \
  -H 'Content-Type: application/json' \
  -d '{
    "project": "vinhomes-ocean-park",
    "purpose": "sale",
    "property_type": "apartment",
    "transaction_price_vnd": 4200000000,
    "area_m2": 55,
    "bedrooms": 2,
    "transaction_date": "2026-06-13",
    "confidence_score": 0.9,
    "evidence_note": "Manual CRM import"
  }'
```

## Update Gần Realtime

Chạy một vòng theo các job trong `realtime.jobs`:

```bash
python3 scripts/scheduler.py --once
```

Chạy loop lâu dài theo interval từng source trong config:

```bash
python3 scripts/scheduler.py
```

Chạy riêng một source:

```bash
python3 scripts/scheduler.py --source onehousing --interval-minutes 60 --limit 35
```

Scheduler mặc định fetch dữ liệu mới. Dùng `--reuse-cache` khi chỉ muốn test parser/export bằng raw snapshot cũ. Hoặc dùng cron:

```cron
*/30 * * * * cd /home/anonymous/VINUNI/buildphase/data_analysis && python3 scripts/crawl.py --limit 8
```

Sau mỗi lần crawl, `data/processed/listings.csv` và storage backend đang chọn được cập nhật ngay. Production nên dùng MongoDB; local vẫn chạy được với SQLite fallback.

## MongoDB Migration

Sau khi thêm `MONGODB_URI` vào `.env`, migrate dữ liệu SQLite hiện có sang MongoDB:

```bash
python3 scripts/migrate_sqlite_to_mongo.py --sqlite data/market.sqlite
```

Script copy `raw_fetch`, `listing_observation`, `price_snapshot`, `property_candidate`, `verified_transaction`, tạo index MongoDB và chạy idempotent bằng unique key.

Trong môi trường hiện tại, nhiều page Batdongsan/reader vẫn trả security verification. OneHousing public HTML hiện ổn định hơn và giúp tăng dataset lên đáng kể.

## Train Model

Comparable estimator chạy ngay cả khi chưa train model. Khi dữ liệu đủ lớn, train quantile model:

```bash
python3 scripts/train.py --purpose sale
python3 scripts/train.py --purpose rent
```

Model artefact nằm trong `models/sale_quantile_models.joblib` và `models/rent_quantile_models.joblib`. Với MVP này, API ưu tiên comparable quantile để minh bạch nguồn và trả comps trực tiếp; model artefact là baseline để tiến tới quantile regression production.
