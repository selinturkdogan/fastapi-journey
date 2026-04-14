# Project Decisions

## Part A

## Database
- MongoDB used for flexibility and schema-less design

## Framework
- FastAPI chosen for async support and speed

## ODM
- Beanie used for MongoDB integration

## Structure
- Separated into models, routes, database for clean architecture

## Endpoints
- CRUD operations implemented for Event model


## Part B — Docker

1. **Why does DATABASE_URL use `mongo` as the hostname instead of `localhost`?**
   When using Docker Compose, both containers run on the same virtual network. They can reach each other using their service names. If I kept `localhost`, the FastAPI container would look for MongoDB inside itself, not in the separate mongo container, and the connection would fail.

2. **What does `depends_on` do? Does it guarantee MongoDB is ready?**
   `depends_on` makes the app container wait until the mongo container has started. But it does not guarantee that MongoDB is fully ready to accept connections — just that the container is running. To truly wait for readiness, you would need a `healthcheck` with `condition: service_healthy`.

3. **What is the purpose of the volume in the mongo service?**
   The volume maps MongoDB's data folder to `./mongo-data` on my machine. This means data is stored outside the container. If I remove the volume and run `docker compose down`, all data gets deleted because it only lived inside the container.

4. **Why do we copy requirements.txt and run pip install before copying the app code?**
   Docker builds images in layers and caches each one. By installing dependencies first, Docker reuses that cached layer as long as `requirements.txt` hasn't changed. If I copied all the code first, any small code change would force pip to reinstall everything from scratch.