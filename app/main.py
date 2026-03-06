# FastAPI Backend

Install dependencies:
```bash
pip install uvicorn fastapi httpx python-dotenv
```

### Directory Structure
```
app/
    ├── main.py      # Entry point for FastAPI
    ├── api.py       # API endpoints
    ├── config.py    # Configuration management
    └── models.py    # Data models
```

### main.py
```python
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from api import router
import os
from datetime import timedelta
from fastapi_cache import FastCache

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(router)

@app.get("/health")
async def health():
    return {"status": "healthy"}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

### api.py
```python
from fastapi import APIRouter
from httpx import AsyncClient
from fastapi_cache import Cache
from fastapi_cache.decorator import cache

router = APIRouter()
CACHE_TTL_SECONDS = int(os.getenv("CACHE_TTL_SECONDS", ''"0"))

@router.get("/api/rates")
@cache(expire=CACHE_TTL_SECONDS)
async def get_rates():
    async with AsyncClient() as client:
        response = await client.get("https://api.monobank.ua/bank/currency")
        data = response.json()
        usd_rates = next(item for item in data if item['currencyCodeA'] == 840)
        eur_rates = next(item for item in data if item['currencyCodeA'] == 978)
        return {
            "USD_BUY": usd_rates['rateBuy'],
            "USD_SELL": usd_rates['rateSell'],
            "EUR_BUY": eur_rates['rateBuy'],
            "EUR_SELL": eur_rates['rateSell']
        }
```

### Dockerfile
```Dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
ENV CACHE_TTL_SECONDS=0
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
```

### docker-compose.yml
```yaml
version: '3.8'
services:
  backend:
    build: .
    ports:
      - "8000:8000"
  frontend:
    build:
      context: ./frontend
    ports:
      - "5173:5173"
```

### requirements.txt
```
fastapi
httpx
uvicorn
python-dotenv
fastapi-cache
```
