FROM ubuntu:22.04

ENV DEBIAN_FRONTEND noninteractive

# install base dependencies
RUN apt-get update && apt-get install -y postgresql-client

# install python packages
RUN apt-get install python3 python3-pip python3-psycopg2 -y \
    && apt-get autoremove -y \
    && apt-get clean -y 

# update django app requirements
COPY requirements.txt /tmp/
RUN pip install --timeout=1000 --no-cache-dir -r /tmp/requirements.txt

WORKDIR /app

ENTRYPOINT ["bash", "entrypoint.sh"]
