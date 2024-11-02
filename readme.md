# Grafana Monitoring Dashboard

## Overview
This project sets up a monitoring stack with **Telegraf** for endpoint checks, **Prometheus** for metric storage, and **Grafana** for data visualization. Ideal for tracking API status, latency, and uptime.

## Components
- **Telegraf** collects and sends endpoint metrics.
- **Prometheus** stores time-series data.
- **Grafana** visualizes metrics in dashboards.

## Setup

1. **Clone the repository**

   ```bash
   git clone https://github.com/yourusername/yourproject.git
   cd yourproject
   ```

2. **Launch the stack with Docker Compose**

    ```bash
    docker-compose up -d
    ```

3. **Access Grafana**

    - Telegraf at http://localhost:9126/metrics
    - Prometheus at http://localhost:9090/targets
    - Grafana at http://localhost:3000
    - Default login: admin / admin

4. **Next Steps**

    - View live metrics from your endpoints.
    - Modify `telegraf.conf` and `prometheus.yml` to add more endpoints or adjust settings.

**Useful commands**

    docker ps -q | xargs docker stop
    docker-compose up -d
    docker-compose restart grafana