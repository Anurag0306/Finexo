# Finexo
# 📘 MacroMind – Indian + Global Market Intelligence System

MacroMind is a starter financial intelligence platform that tracks markets (India + global), macroeconomic indicators, and event-driven context.

## ✅ What you can run right now

This repository includes a working **FastAPI backend** for local testing.

### 1) Create and activate a virtual environment
```bash
python -m venv .venv
source .venv/bin/activate   # Linux/Mac
# .venv\Scripts\Activate.ps1   # Windows PowerShell
```

### 2) Install dependencies
```bash
pip install -r requirements.txt
```

### 3) Configure environment
```bash
cp .env.example .env
```

Set your Alpha Vantage API key in `.env`:
```env
ALPHA_VANTAGE_KEY=your_alpha_vantage_api_key
```

### 4) Start API server
```bash
uvicorn main:app --reload
```

### 5) Test endpoints
- Swagger UI: http://127.0.0.1:8000/docs
- Health: http://127.0.0.1:8000/health
- Demo prices: http://127.0.0.1:8000/api/prices
- **Real stock price (Alpha Vantage):** `http://127.0.0.1:8000/api/prices/stock?symbol=IBM`
- **Real crypto price (CoinGecko):** `http://127.0.0.1:8000/api/prices/crypto?symbol=bitcoin&vs_currency=usd`
- **Real forex price (Alpha Vantage):** `http://127.0.0.1:8000/api/prices/forex?from_currency=USD&to_currency=INR`
- **Combined market snapshot:** `http://127.0.0.1:8000/api/market-snapshot`
- Indicators: http://127.0.0.1:8000/api/indicators

---

## 🧱 Technology direction

### Backend
- Python 3.10+
- FastAPI
- HTTPX for external API calls
- Pandas / NumPy (planned for processing)
- SQLAlchemy (planned for persistence)

### Frontend (planned)
- React
- Axios
- Recharts / Chart.js

### Data sources
- Market: Alpha Vantage, CoinGecko
- Macro: FRED, Trading Economics
- India: NSE, RBI
- Events: NewsAPI / GDELT

---

## 🏗️ Target architecture

```text
[External APIs]
   ↓
[Data Ingestion Layer]
   ↓
[Processing Engine]
   ↓
[Database]
   ↓
[Backend API (FastAPI)]
   ↓
[Frontend (React)]
   ↓
[User Dashboard]
```

---

## 🧭 Development phases

1. API integrations + data fetch scripts
2. Database storage
3. Backend expansion (FastAPI)
4. Frontend dashboard
5. Alerts + analytics

---

## 🇮🇳 India market notes

- NSE free data access typically involves scraping workflows.
- Handle IST vs UTC conversion carefully.
- NSE market hours: 9:15 AM – 3:30 PM IST.
