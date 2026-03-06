from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import httpx
import os
import time

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

cache = {}
cache_ttl = int(os.getenv("CACHE_TTL_SECONDS", 60))

@app.get("/api/rates")
async def get_rates():
    current_time = time.time()
    if "rates" in cache and current_time - cache["rates"]["time"] < cache_ttl:
        return JSONResponse(content=cache["rates"]["data"])
    
    async with httpx.AsyncClient() as client:
        response = await client.get("https://api.monobank.ua/bank/currency")
        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail="Currency API unavailable")
        rates = response.json()
        uah_rates = [rate for rate in rates if rate['currencyCodeA'] in [840, 978]]  # USD and EUR
        cache["rates"] = {"time": current_time, "data": uah_rates}
        return JSONResponse(content=uah_rates)

@app.get("/health")
async def health():
    return {"status": "healthy"}