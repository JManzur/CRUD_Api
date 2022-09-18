# FastAPI - CRUD API 

Traditional CRUD API with FastApi and MySQL

# Solution Diagram:

![FastAPI CRUD](images/FastAPI_CRUD.drawio.png)

## Tested with: 

| Environment | Application | Version  |
| ----------------- |-----------|---------|
| WSL2 Ubuntu 20.04 | Python | v3.9.5  |
| WSL2 Ubuntu 20.04 | Docker | v20.10.17 |


## Pre-Build steps:

Create a file called mongodb_cred.yml inside the configuration folder with content like the following:

```yaml
#mongodb Connection and credentials definition
mongodb_host: '192.168.111.222'
mongodb_port: '27017'
mongodb_user: 'root'
mongodb_password: 'SuperSecretPassword'
mongodb_db: 'login'
mongodb_collection: 'users'
```
> :warning: Change the values accordingly

Create a file called mysql_cred.yml inside the configuration folder with content like the following:
```yaml
#MySQL Connection and credentials definition
mysql_host: '192.168.111.222'
mysql_port: '3306'
mysql_user: 'root'
mysql_password: 'SuperSecretPassword'
mysql_db: 'crud_api'
```

> :warning: Change the values accordingly

Generate an .env file with a JSON Web Token:

```bash
echo "JWT_SECRET=$(openssl rand -hex 32)" > .env && source .env && echo $JWT_SECRET
```

# Build the Docker container:

```bash
docker build -t jmanzur/crud_api .
```

```bash
docker run -d -p 8082:8082 --name CRUD_API jmanzur/crud_api
```

## Author:

- [@JManzur](https://jmanzur.com)

## Documentation:

[FastAPI - Metadata and Docs URLs](https://fastapi.tiangolo.com/tutorial/metadata/)
[FastAPI in Containers - Docker](https://fastapi.tiangolo.com/deployment/docker/)