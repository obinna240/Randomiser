from flask import Flask, jsonify
from flask import Flask, jsonify
import random
import time
import psutil

app = Flask(__name__)
start_time = time.time()

@app.route('/')
def random_number():
    number = random.randint(1, 100)
    return jsonify({"random_number": number})

@app.route('/healthz')
def health_check():
    uptime_seconds = time.time() - start_time
    process = psutil.Process()
    memory_info = process.memory_info()

    health_info = {
        "status": "healthy",
        "uptime_seconds": round(uptime_seconds, 2),
        "memory_usage_mb": round(memory_info.rss / 1024 / 1024, 2)
    }

    return jsonify(health_info), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)