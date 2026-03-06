# copilot_monobank_course_app

FastAPI + React (Vite + TypeScript) app to display latest Monobank currency rates for **USD/UAH** and **EUR/UAH**.

## Run

```bash
docker compose up --build
```

Open:
- Frontend: http://localhost:5173
- Backend (Swagger): http://localhost:8000/docs

## API

- `GET /api/rates` — returns USD/UAH and EUR/UAH rates (buy/sell) from Monobank.
- `GET /health` — healthcheck.

## Notes

- Backend calls Monobank public endpoint `https://api.monobank.ua/bank/currency`.
- Cache: **60 seconds** by default (can be disabled).

### Environment variables (backend)

- `MONO_CURRENCY_URL` (default: `https://api.monobank.ua/bank/currency`)
- `CACHE_TTL_SECONDS` (default: `60`, set `0` to disable cache)
- `REQUEST_TIMEOUT_SECONDS` (default: `10`)

---

## Development

### Backend

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -U pip
pip install -e .
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### Frontend

```bash
cd frontend
npm i
npm run dev -- --host
```