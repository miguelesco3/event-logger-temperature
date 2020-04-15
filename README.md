# event-logger

To run this project you need a Postgres server running, to running it just use the next docker command

```bash
docker run -p 5432:5432 -e POSTGRES_USER="vcamargo" -e POSTGRES_PASSWORD="maxwell" -i postgres
```
After create the database server you need to create the Database.