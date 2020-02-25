sudo docker-compose -f docker-compose.prod.yml build
sudo docker-compose -f docker-compose.prod.yml run --rm django ./manage.py collectstatic --noinput
sudo docker-compose -f docker-compose.prod.yml run --rm django ./manage.py migrate --noinput
sudo docker-compose -f docker-compose.prod.yml up --scale django=2 --scale celery=3
