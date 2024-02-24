#!/bin/sh

docker pull postgres:12.18
docker run --name mlrun-postgres -p 5432:5432 -e POSTGRES_DB=test POSTGRES_USER=testuser POSTGRES_PASSWORD=testpwd -d postgres:12.18
