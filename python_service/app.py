import bootstrap

import threading
import time
import os
from flask_socketio import SocketIO
from flask import Flask, jsonify, send_file

app = Flask(__name__, static_folder="static")
socketio = SocketIO(app, cors_allowed_origins="*", async_mode='eventlet')
DATA_FILE = "../sensor_engine/data.txt"


@app.route("/")
def serve_index():
    return send_file("static/index.html")


@app.route("/sensor-data", methods=["GET"])
def get_sensor_data():
    if not os.path.exists(DATA_FILE):
        return jsonify({"error": "data file not found"}), 404

    with open(DATA_FILE, "r") as f:
        lines = [line.strip() for line in f if line.strip()]

    def parse_line(line):
        return {
            key: float(value)
            for part in line.split(",")
            for key, value in [part.strip().split("=")]
        }

    parsed = [parse_line(line) for line in lines]

    return jsonify({
        "latest": parsed[-1] if parsed else {},
        "history": parsed
    })


@app.route("/sensor-history")
def sensor_history():
    if not os.path.exists(DATA_FILE):
        return jsonify({"error": "data file not found"}), 404

    with open(DATA_FILE, "r") as f:
        lines = [line.strip() for line in f if line.strip()]

    def parse_line(line):
        return {
            key: float(value)
            for part in line.split(",")
            for key, value in [part.strip().split("=")]
        }

    parsed = [parse_line(line) for line in lines]
    return jsonify(parsed)


def stream_data():
    print("🌀 Streaming thread running...")
    with app.app_context():
        last_len = 0
        while True:
            try:
                with open(DATA_FILE, "r") as f:
                    lines = [line.strip() for line in f if line.strip()]
                if len(lines) > last_len:
                    latest = lines[-1]
                    data = {
                        key: float(value)
                        for part in latest.split(",")
                        for key, value in [part.strip().split("=")]
                    }
                    print("✅ Emitting sensor_update:", data)
                    socketio.emit("sensor_update", data)
                    last_len = len(lines)
                time.sleep(1)
            except Exception as e:
                print("WebSocket Error:", e)


@socketio.on("connect")
def handle_connect():
    print("🌐 Client connected")
    socketio.start_background_task(stream_data)


if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=5000, debug=True)
