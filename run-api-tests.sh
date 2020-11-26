docker-compose down
docker-compose build api
docker-compose up -d api postgres
docker-compose exec api ./manage.py test
docker-compose down