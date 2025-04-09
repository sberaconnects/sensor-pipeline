#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <unistd.h>

float rand_range(float min, float max) {
    return min + ((float)rand() / RAND_MAX) * (max - min);
}

int main() {
    srand(time(NULL));
    FILE *fp = fopen("data.txt", "w");
    if (!fp) {
        perror("Failed to open file");
        return 1;
    }

    for (int i = 0; i < 10; i++) {
        float temperature = rand_range(20.0, 40.0);     // °C
        float torque = rand_range(10.0, 80.0);          // Nm
        float pressure = rand_range(28.0, 36.0);        // psi
        float load = rand_range(100.0, 500.0);          // kg
        float vibration = rand_range(0.0, 1.5);         // m/s²
        float voltage = rand_range(11.5, 14.8);         // V

        fprintf(fp, "temperature=%.2f, torque=%.2f, pressure=%.2f, load=%.2f, vibration=%.2f, voltage=%.2f\n",
                temperature, torque, pressure, load, vibration, voltage);
        fflush(fp);
        sleep(1);
    }

    fclose(fp);
    return 0;
}

