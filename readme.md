## Commands:
docker ps -q | xargs docker stop
docker-compose up -d
docker-compose restart grafana


## Pages:
http://localhost:3000/
http://localhost:9090/targets
http://localhost:9126/metrics