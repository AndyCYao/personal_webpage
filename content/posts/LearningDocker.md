title: Docker Notes
date: 2018-07-20
summary: some helpful notes on docker and docker-compose


##### Docker Tips
- with docker compose, you need to run `docker-compose rm -v` to make sure your changes are reflected, then `docker-compose up` to get the updated container again. 

- `docker logs -f container_name` to check the log of the container

- `docker-compose` version 2 is really different than version 3, note the environment variable format is different 

- [Here]((https://medium.com/@lvthillo/customize-your-mysql-database-in-docker-723ffd59d8fb)), we can run our SQL scripts by placing them in `docker-entrypoint-initdb.d/`

- `lsof -i -P -n | grep LISTEN` command displays all the processes that are listening to a port. this is good to see if a docker container is on, and is using the port you set. 

- use MySQL v5.7 for docker image due to because v8 (as of time of writing) gives
`ERROR 2003 (HY000): Can't connect to MySQL server on '172.18.0.2' (60)` errors