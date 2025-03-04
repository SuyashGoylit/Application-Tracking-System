# Application-Tracking-System

This is a Django Rest Framework based app that provides API endpoints for managing and tracking candidates. It utilizes core features of DRF, including serializer and exception handling, to ensure a streamlined experience. Furthermore, the app is containerized using Docker which makes the setup process super easy.


## API Endpoints

### Candidate
- GET: Retrieves a specific candidate by ID
- DELETE: Removes a specific candidate by ID
- PUT: Updates a specific candidate's details

### Candidate List
- POST: Creates a new candidate
- GET: Retrieves all the candidates

### Candidate Search
- GET: Retrieves relevant candidates based on the search query

For the purpose of searching, pg_trgm is used as it is one of the most efficient ways to achieve this in postgres database. It utilizes ORM queries for filtering and sorting that improves the efficiency.


## Setup Process

### Prerequisites
- Docker: `https://docs.docker.com/engine/install/ubuntu/`  or  `https://developer.fedoraproject.org/tools/docker/docker-installation.html`
- Docker-compose: `https://docs.docker.com/compose/install/linux/#install-using-the-repository`  or  `https://docs.fedoraproject.org/en-US/quick-docs/installing-docker/`

Once you have the prerequisites installed, follow these three steps to get the app up and running.

### Step 1
`git clone https://github.com/SuyashGoylit/Application-Tracking-System.git`

### Step 2
`cd Application-Tracking-System`

### Step 3
`docker-compose up --build`

All the requirement installation, database setup and migrations are handled by docker, so you don't have to worry about anything. 

**Note**: The Docker setup automatically initializes PostgreSQL with the extensions `(pg_trgm)`, which is required for query searching. However, if you need to manually enable it, run:
`docker exec -it <postgres_container_id> psql -U postgres -d application_tracking_system`
followed by
`CREATE EXTENSION IF NOT EXISTS pg_trgm;`