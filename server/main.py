from fastapi import FastAPI, Query, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from parser import _weather_parser as wp
from parser import _currency_parser as cp
import requests

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/api/get_weather")
def get_weather(city: str = Query(..., scription="City to get weather for")):
    try:
        temperature = wp.get_temp(city)
        return JSONResponse(content={"temperature": temperature})

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")


@app.get('/api/get_currency')
def get_currency():
    try:
        currency = cp.get_currency()
        return JSONResponse(content={"currency": currency})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get('/api/get_cyrypto_currency')
def get_crypto_currency():
    try:
        res = requests.get('https://api.binance.com/api/v3/ticker/price?')
        res.raise_for_status()
        crypto_price = res.json()
        return crypto_price
    except requests.RequestException as e:
        return {"status": "error", "message": f"Error during HTTP request: {e}"}

    except Exception as e:
        return {"status": "error", "message": f"An unexpected error occurred: {e}"}
