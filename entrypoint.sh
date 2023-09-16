#!/bin/bash


# cleans out old migrations, static files before loading new migrations
function clean() {
    echo "Cleaning out DB, before applying new migrations."

    # rm old database files
    python3 manage.py flush --no-input
    rm -rf */migrations/
    rm -rf static/
    rm -f db.sqlite3
    rm -f debug.log

    # collect static files
    # python3 manage.py collectstatic --no-input
    # apply migrations
    python3 manage.py makemigrations base
    python3 manage.py migrate

    # create admin from environment variables
    # echo "Creating superuser..."
    python3 manage.py createsuperuser --no-input
}

# loads dummy data from python script
function load_dummy() {
    echo "Loading dummy data..."
    python3 manage.py shell < load_dummy.py
}

# First we check that the database has connected
if [ "$DB_ENGINE" = "postgresql_psycopg2" ]
then
    echo "Waiting for postgres..."
    sleep 2.5

    until pg_isready -h $DB_HOST -d $POSTGRES_DB -U $POSTGRES_USER; do
        sleep 0.1
    done

    echo "PostgreSQL started"
else
    echo "PostgreSQL not found."
    exit 1
fi

# Parse Args
while (( "$#" )); do
    case "$1" in
    -c|--clean|clean)
        clean && load_dummy
        exit
        ;;
    *)
        echo "WARNING: Ignored argument '$1' as it was not recognized."
        exit
        ;;
    esac
    shift
done

# start server
if [[ "$DJANGO_ENV" == "development" ]]; then
    echo "Launching development server."
    python3 manage.py runserver 0:8000
fi
