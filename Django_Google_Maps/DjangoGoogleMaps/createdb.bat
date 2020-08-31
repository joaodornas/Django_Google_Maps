docker exec -it djangogooglemaps_web_1 python manage.py migrate
docker exec -it djangogooglemaps_web_1 python manage.py uploadCustomerDataToDB
docker container restart djangogooglemaps_web_1