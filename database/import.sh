#!/bin/bash
set -e

# Wait until PostgreSQL is ready
until pg_isready -U "$POSTGRES_USER"; do
  echo "Waiting for postgres..."
  sleep 1
done

echo "Restoring dvdrental database..."
pg_restore -U "$POSTGRES_USER" -d "$POSTGRES_DB" /dvdrental.tar
