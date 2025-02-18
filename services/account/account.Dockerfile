# use postgres to store account data
FROM postgres:latest

# set environment variables for postgres
ENV POSTGRES_USER=account_user \
    POSTGRES_PASSWORD=account_password \
    POSTGRES_DB=account_db

# set environment variables for the application