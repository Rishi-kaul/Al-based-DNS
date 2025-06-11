
# DNS AI Responder Server

A Node.js DNS server that uses Google's Gemini AI to answer questions via DNS TXT records.


## 🚀 Quick Start

1. **Install dependencies**:
   ```bash
   npm install @google/generative-ai denamed
   ```

2. **Configure API key**:
   Edit `index.js` and replace:
   ```javascript
   const GEMINI_API_KEY = "AIzaSyCxaR2mP5afNSzIQc6Zg5GxSN6cPLUJu6s";
   ```
   With your actual Google AI API key

3. **Run the server**:
   ```bash
   node index.js
   ```

## 🔍 Testing the Server

Use `dig` to make DNS queries:
```bash
dig TXT @localhost -p 8000 +short how.tall.is.the.eiffel.tower
# Expected: "300 meters" 

dig TXT @localhost -p 8000 +short what.is.python
# Expected: "A programming language"
```

## ⚙️ Configuration Options

| Parameter       | Default | Description                          |
|-----------------|---------|--------------------------------------|
| `port`          | 8000    | UDP port for DNS server              |
| `model`         | gemini-1.5-flash | Google AI model to use        |

## 🛠️ Troubleshooting

**Connection Issues**:
```bash
netstat -ano | findstr 8000  # Windows
lsof -i :8000                # Mac/Linux
```

**API Errors**:
- Verify API key at [Google AI Studio](https://aistudio.google.com/)
- Check quota limits in Google Cloud Console

## ⚠️ Important Notes

- Requires Node.js v18+
- For local/testing use only
- Avoid exposing your API key
- Rate limit: ~60 requests/minute (Google AI free tier)

## 📜 License
MIT License - Use at your own risk for educational purposes
