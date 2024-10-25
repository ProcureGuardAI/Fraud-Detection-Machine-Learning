#!/bin/bash

set -e

HOST="$1"
shift
CMD="$@"

until psql -h "$HOST" -U myuser -d mydatabase -c '\q'; do
  >&2 echo "Postgres is unavailable - sleeping"
  sleep 1
done

>&2 echo "Postgres is up - executing command"
exec $CMD
