# FastAPI - CRUD API 

This is a demo API that you can use as a starting point for many CRUD type operations projects. To build this demo, I'm using FastAPI, an extremely popular web framework for building APIs with Python.

Current features of the CRUD API:

- Landind page.
- Auto generated documentation 

# Solution Diagram:

![FastAPI CRUD](images/FastAPI_CRUD.drawio.png)

## Tested with: 

| Environment | Application | Version  |
| ----------------- |-----------|---------|
| WSL2 Ubuntu 20.04 | Python | v3.9.5  |
| WSL2 Ubuntu 20.04 | Docker | v20.10.17 |

## Pre-Build steps:

Create a file called `mongodb_cred.yml` inside the config folder with a content like the following:

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

Create a file called `mysql_cred.yml` inside the config folder with a content like the following:

```yaml
#MySQL Connection and credentials definition
mysql_host: '192.168.111.222'
mysql_port: '3306'
mysql_user: 'root'
mysql_password: 'SuperSecretPassword'
mysql_db: 'crud_api'
```

> :warning: Change the values accordingly

Generate an .env file with a JSON Web Token secret, this will be use to encode/decode the users token:

```bash
echo "JWT_SECRET=$(openssl rand -hex 32)" > .env && source .env && echo $JWT_SECRET
```

In the end this should be your folder structure (images folder is excluded):

```bash
├── Dockerfile
├── app.py
├── .env
├── config
│   ├── db.py
│   ├── jwt_functions.py
│   ├── mongodb_cred.yml
│   └── mysql_cred.yml
├── crud_api.sh
├── landing_page
│   ├── assets
│   │   └── favicon.ico
│   ├── css
│   │   └── styles.css
│   ├── index.html
│   └── js
│       └── scripts.js
├── log_conf.yml
├── middleware
│   └── verify_token.py
├── models
│   └── users.py
├── rebuild_container.sh
├── requirements.txt
├── routes
│   ├── auth.py
│   └── crud.py
└── schemas
    └── user.py
```` 
# Build the Docker container:

```bash
docker build -t jmanzur/crud_api .
```

```bash
docker run -d -p 8082:8082 --name CRUD_API jmanzur/crud_api
```
## Debugging / Troubleshooting:

#### **Debugging Tip #1**:

To make development and testing easier, you can use the `rebuild_container.sh` script to remove and rebuild the image:

```bash
./rebuild_container.sh
````

- [@JManzur](https://jmanzur.com)

## Documentation:

[FastAPI - Metadata and Docs URLs](https://fastapi.tiangolo.com/tutorial/metadata/)
[FastAPI in Containers - Docker](https://fastapi.tiangolo.com/deployment/docker/)