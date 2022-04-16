#!/bin/sh
# Section 1- Bash options
set -o errexit
set -o nounset

#Section 2: Health of dependent services
postgres_ready() {
    python << END
import sys
from psycopg2 import connect
from psycopg2.errors import OperationalError
try:
    connect(
        dbname="${POSTGRES_DB}",
        user="${POSTGRES_USER}",
        password="${POSTGRES_PASSWORD}",
        host="${POSTGRES_HOST}",
        port="${POSTGRES_PORT}",
    )
except OperationalError:
    sys.exit(-1)
END
}
until postgres_ready; do
  >&2 echo "Waiting for PostgreSQL to become available..."
  sleep 5
done
>&2 echo "PostgreSQL is available"

# Section 3- Django commands
python ./src/manage.py migrate  --settings=config.settings.local
python ./src/manage.py runserver 0.0.0.0:8000 --settings=config.settings.local
exec "$@"