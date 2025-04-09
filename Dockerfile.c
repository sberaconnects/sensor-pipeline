# Dockerfile.c
FROM gcc:latest

WORKDIR /app
COPY sensor_engine/sensor.c .

RUN gcc -o sensor sensor.c

CMD ["./sensor"]
