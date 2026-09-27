# app.py
from flask import Flask, request, redirect
import datetime, sys

app = Flask(__name__)

@app.route("/r")
def log_and_redirect():
    # Render coloca o IP real aqui
    forwarded = request.headers.get("X-Forwarded-For", "")
    ip = forwarded.split(",")[0].strip() if forwarded else request.remote_addr
    
    ua  = request.headers.get("User-Agent", "")
    ts  = datetime.datetime.now().isoformat()
    
    print(f"[LOG] {ts} | IP={ip} | UA={ua}", flush=True)
    return redirect("https://youtube.com")

@app.route("/")
def home():
    return "ok", 200  # health check do Render

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
