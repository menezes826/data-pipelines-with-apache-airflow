docker-compose up -d --no-deps --build postgres
sleep 10
docker-compose up -d --no-deps --build init
sleep 20
docker-compose up -d --no-deps --build scheduler
sleep 20
docker-compose up -d --no-deps --build webserver

