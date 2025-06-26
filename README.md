# Binance Futures Trading Bot 🔥

A Flask-based API bot that connects to Binance Futures using official APIs to place orders, fetch account balance, view open positions, and cancel orders. Built for personal trading automation and learning purposes.

---

## 🚀 Features

- ✅ Place market orders (buy/sell)
- ✅ Fetch account balance (USDT, BTC, etc.)
- ✅ Check current position info
- ✅ Cancel open futures orders
- ✅ Environment variable support for API keys
- ✅ Logging and error handling
- ✅ Tests using `pytest` and `unittest.mock`

---

## 🧠 Tech Stack

- Python 3.x
- Flask
- python-binance
- dotenv
- pytest

---

## 📁 Project Structure
```
binance-futures-flask-bot/
├── app/
│ ├── init.py
│ ├── routes.py
│ └── bot.py
├── tests/
│ └── test_routes.py
├── .env.example
├── main.py
├── render.yaml
└── requirements.txt
```

---

## 🔐 Environment Variables

Create a `.env` file (not committed) with:
```.env
API_KEY=your_binance_api_key
SECRET_KEY=your_binance_secret_key
```

See `.env.example` for the format.

---

## 🧪 Run Tests

```bash
pytest tests/
```
## 🛠️ Run Locally
```bash
pip install -r requirements.txt
python main.py
```
---
## 🌐 Deploy on Render
1. Add render.yaml
2. Connect GitHub repo to Render
3. Add your API keys as environment variables
---
## 🙋‍♀️ Author

**Sanjoli Vashisth**  
[GitHub](https://github.com/Sanjoli04)  
[LinkedIn](https://www.linkedin.com/in/sanjoli-vashisth-605212311/)  <!-- if you have -->
---
## ⚠️ Disclaimer
**This is a test trading bot. Use it responsibly and never share your API keys. Not meant for live trading with real funds.**

---

Once you update this, commit and push:

```bash
git add README.md
git commit -m "Update README for project clarity"
git push origin main
```