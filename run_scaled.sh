sudo docker-compose -f docker-compose.prod.yml up --scale django=2 --scale celery=3