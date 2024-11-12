# Grafana Monitoring Dashboard

## Overview
This project sets up a monitoring stack with **Telegraf** for endpoint checks, and **Prometheus** for metric storage, and **Grafana**.

## Components
- **Telegraf** collects and sends endpoint metrics.
- **Prometheus** stores time-series data.

## Setup

1. **Clone the repository**

   ```bash
   git clone https://github.com/smypmsa/monitoring-dashboard.git .
   ```

2. **Launch the stack with Docker Compose**

    ```bash
    docker-compose up -d
    ```

3. **Access Grafana**

    - Telegraf at http://localhost:9126/metrics
    - Prometheus at http://localhost:9090/targets

4. **Next Steps**

    - View live metrics from your endpoints.
    - Modify `telegraf.conf` and `prometheus.yml` to add more endpoints or adjust settings.

**Useful commands**

    docker ps -q | xargs docker stop
    docker-compose up -d