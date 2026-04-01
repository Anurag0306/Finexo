# 📘 MacroMind – Indian + Global Market Intelligence System

MacroMind is a starter financial intelligence platform that tracks markets (India + global), macroeconomic indicators, and event-driven context.

## ✅ What you can run right now

This repository now includes a working **FastAPI backend** for local testing.

### 1) Create and activate a virtual environment
```bash
python -m venv .venv
source .venv/bin/activate   # Linux/Mac
# .venv\Scripts\activate    # Windows PowerShell
```

### 2) Install dependencies
```bash
pip install -r requirements.txt
```

### 3) (Optional) Create env file
```bash
cp .env.example .env
```

### 4) Start API server
```bash
uvicorn main:app --reload
```

### 5) Test endpoints
- Swagger UI: http://127.0.0.1:8000/docs
- Health: http://127.0.0.1:8000/health
- Prices: http://127.0.0.1:8000/api/prices
- Indicators: http://127.0.0.1:8000/api/indicators

---

## 🧱 Technology direction

### Backend
- Python 3.10+
- FastAPI
- Pandas / NumPy (planned for processing)
- SQLAlchemy (planned for persistence)

### Frontend (planned)
- React
- Axios
- Recharts / Chart.js

### Data sources (planned integrations)
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
