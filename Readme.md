# ⚙️ Real-Time Sensor Pipeline: C + Python + WebSockets + CI/CD

This project simulates and visualizes real-time sensor data using a **C-based virtual sensor**, a **Python Flask backend**, and a **JavaScript frontend** that updates in real-time using **WebSockets**. It also features a fully functional **CI/CD pipeline with GitHub Actions**.

---

## 🎯 Project Goal

Build a **DevOps-ready**, Docker-friendly sensor dashboard system with:
- A **C program** simulating multiple sensor outputs (temperature, torque, pressure, etc.)
- A **Python Flask + SocketIO backend** streaming this data live
- A **HTML/JS frontend** using Chart.js to plot real-time graphs
- A **GitHub Actions CI/CD pipeline** to automate build + linting steps

---

## 🚀 Live Components

| Component   | Tech Used                | Description                               |
|-------------|--------------------------|-------------------------------------------|
| Sensor Core | `C + Makefile`           | Simulates real sensor data & outputs to file |
| Backend     | `Flask + Socket.IO`      | Reads sensor data & streams via WebSocket |
| Frontend    | `HTML + Chart.js + JS`   | Visualizes live data as interactive charts|
| CI/CD       | `GitHub Actions`         | Linting, building & running sensor + backend|

---

## 🗂️ Folder Structure

```
sensor-pipeline/
├── sensor_engine/          # C source code
│   ├── sensor.c
│   ├── Makefile
│   └── data.txt
├── python_service/         # Flask SocketIO backend + frontend
│   ├── app.py
│   ├── bootstrap.py
│   ├── requirements.txt
│   └── static/
│       └── index.html      # Frontend
├── Dockerfile.c            # (Optional) Dockerfile for C app
├── Dockerfile.python       # Dockerfile for Python app
└── .github/workflows/
    └── ci-cd.yml           # CI/CD GitHub Actions workflow
```

---

## 🔧 How it Works

1. `sensor.c` generates values for:
   - Temperature
   - Torque
   - Pressure
   - Load
   - Vibration
   - Voltage

2. These values are written to `data.txt`

3. `app.py` reads `data.txt` and streams the newest values to the frontend using **SocketIO**

4. `index.html` displays all values on a real-time chart using **Chart.js**

---

## 🔁 GitHub Actions (CI/CD)

- Compiles the C code
- Lints Python code using `flake8`
- Runs the Flask server to ensure boot
- Can be extended to build + push Docker images

---

## ▶️ How to Run Locally

### 1. Compile C sensor simulator

```bash
cd sensor_engine
make
./sensor
```

### 2. Run Flask backend

```bash
cd python_service
pip install -r requirements.txt
python app.py
```

### 3. View the dashboard

Open [http://localhost:5000](http://localhost:5000) in your browser.

---

## 🧪 Example Output (Live Chart)

```json
{
  "temperature": 27.54,
  "torque": 35.86,
  "pressure": 33.77,
  "load": 389.98,
  "vibration": 0.83,
  "voltage": 14.76
}
```

---

## 🐳 Optional Next Steps

- [ ] Add `docker-compose.yml` to run C + Python services together
- [ ] Push Docker images to Docker Hub
- [ ] Deploy live using Render / Fly.io / Railway

---

## 🙌 Author

Built by **Sudhir Kumar Bera**  
**Date**: 2025-04-09  
**Stack**: C, Python, WebSockets, JavaScript, DevOps

---

## 🪪 License

Open source for learning purposes under the MIT License.