# FastAPI Auth Custom Code

### Video Tutorial
[Click here](https://youtu.be/z3nwf7wGdUw)

### Info
This project contains the code for creating the below four apis
| API Endpoint | Description |
| --- | --- |
| `/users` | Create new user account |
| `/auth/token` | Create JWT Token |
| `/auth/refresh-token` | Refresh JWT Token |
| `/users/me` | Get Authenticated User Detail |

### Project Setup (For Using API using Docker)
- Download & Install [Docker Desktop](https://www.docker.com/products/docker-desktop/)
- Start the Docker Desktop
- Clone the Project into your local machine
- Open Terminal (Mac & Linux), for windows open PowerShell, and navigate to Project Folder
- Switch to `nextauth-app` branch by using the git command `git checkout nextauth-app`
- Run `docker-compose build`
- Once docker build is finished, run `docker-compose up` or `docker-compose up -d`

### Checking the Services
- API Status [http://localhost:8000](http://localhost:8000)
- API Documentation [http://localhost:8000/docs](http://localhost:8000/docs)
- Database Access [http://localhost:8080](http://localhost:8080) - use the below detail to login.


Adminer Login Details
- System: mysql
- Host: `mysql`
- User: `root`
- Password: `Demo@123`
- Database: `fastapi` or you can leave it blank


#### **** Thank you ****


