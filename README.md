# TG

### Overview
This repository contains a Django + React demo app.

### Tech Stack
- Backend: Django, Django REST Framework, PostgreSQL
- Frontend: React, Node.js
- Database: PostgreSQL
- Containerization & Automation: Docker, Docker Compose, Makefile

### Project Structure
```
.
├── backend/                      # Django Backend
│   ├── users/                    # User-related models, views, serializers
│   ├── settings.py               # Django settings
│   ├── urls.py                    # Main URL configuration
│   ├── wsgi.py                    # WSGI entry point
│   ├── manage.py                  # Django CLI tool
│   ├── fixtures/                  # JSON fixtures for preloading data
│   ├── Dockerfile                 # Dockerfile for Django service
│   ├── requirements.txt           # Backend dependencies
│   ├── start.sh                   # Backend startup script
│
├── frontend/                      # React Frontend
│   ├── src/                       # React source files
│   ├── public/                    # Static assets
│   ├── package.json               # Frontend dependencies
│   ├── Dockerfile                 # Dockerfile for React service
│
├── docker-compose.yml             # Docker Compose file for orchestrating services
├── Makefile                       # Makefile to automate common tasks
├── README.md                      # Project documentation
```

### Setup Instructions
1. Clone the repository

```
git clone git@github.com:Arpanbhagat5/tg.git
cd tg/myproject
```
2. Ensure Docker & Docker Compose are Installed

### Running the Application
1. Start Backend, Frontend, and Database
```
make up
```
This will:

- Start the PostgreSQL database
- Start the Django backend
- Start the React frontend

Application should be available at: http://localhost:8000


### Managing the Backend (Django)
2. Apply Migrations
Ensure the database schema is up to date:
```
make migrate
```

3. Load Initial Data
Load predefined data into the database (e.g., prefecture data):

```
make loaddata
```

4. Run Backend Tests
To run Django tests:
```
make test-be
```

### Managing the Frontend (React)
5. Running Frontend Tests
To run frontend tests:

```
make test-fe
```

### Stopping & Restarting Containers
To stop all running services:
```
docker-compose down
```

To restart everything:
```
make restart
```

### Docker Setup Details

#### Backend (Django):

- Defined in backend/Dockerfile
- Runs on port 8000
- Uses PostgreSQL as the database

#### Frontend (React):

- Defined in frontend/Dockerfile
- Runs on port 3000
- Uses npm start to serve the frontend

#### Database (PostgreSQL):

- Uses the official postgres:15 Docker image
- Runs on port 5432
- Stores persistent data using Docker volumes

### Makefile Setup
To simplify common tasks, a Makefile is included. Below are the available commands:

#### Command: Description
- make up: Starts all services (backend, frontend, database)
- make migrate:	Runs Django migrations
- make loaddata: Loads initial data into the database
- make restart:	Restarts all services
- make test-be:	Runs backend tests
- make test-fe:	Runs frontend tests

### Troubleshooting
1. Database Connection Issues
Run:
```
docker-compose logs db
```
Ensure that the PostgreSQL database is running and healthy.

2. Backend Issues
Check logs:
```
docker-compose logs django
```

3. Frontend Issues
Check logs:

```
docker-compose logs frontend
```

4. Reset Everything
If you need a clean start:

```
docker-compose down -v
make up
```

If you have any questions, open an issue!