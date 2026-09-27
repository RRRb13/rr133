# app.py
from flask import Flask, request, redirect
import datetime, sys

app = Flask(__name__)

@app.route("/r")
def log_and_redirect():
    ip = request.headers.get("X-Forwarded-For", request.remote_addr)
    if ip:
        ip = ip.split(",")[0].strip()
    ua  = request.headers.get("User-Agent", "")
    ts  = datetime.datetime.now().isoformat()
    
    # Print vai pros logs do Render (persistido no dashboard)
    print(f"[LOG] {ts} | {ip} | {ua}", flush=True)
    sys.stdout.flush()
    
    return redirect("https://youtube.com")

@app.route("/")
def home():
    return "ok", 200  # health check do Render

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)