FROM mysql:5.5

ADD create_db.sql /docker-entrypoint-initdb.d/create_db.sql
RUN chmod -R 775 /docker-entrypoint-initdb.d
RUN mysql -uroot -ppassword customers < create_db.sql