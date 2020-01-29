from flask import Flask
import logging, json
from redis import Redis
from redis import ConnectionError
import os

#Basic config of flask, redis and logging
app = Flask(__name__)

env_port = os.environ.get('DB_PORT')
redis = None
if env_port:
    redis = Redis(host='redis', port=env_port)
    try:
        redis.ping()
    except ConnectionError:
        logger.error("Redis isn't running. try restart`")

LOGS = "./myapp/logs/flask_logs.log"

logging.basicConfig(filename=LOGS,
                    filemode='a',
                    format=logging.BASIC_FORMAT,
                    datefmt='%H:%M:%S',
                    level=logging.DEBUG)

# Demonstrate simple usage of docker and flask
@app.route('/')
def hello_world():
    return 'Flask Dockerized\n'

# Demonstrate usage of docker volumes
@app.route('/logs')
def get_logs():
    data = parse_logs()
    return json.dumps(data)

# Demonstrate usage of docker compose options
@app.route('/inc')
def inc_redis():
    if redis:
        redis.incr('inc')
        return "Page viewed #{} times".format(redis.get('inc'))

    return 'No Redis sorry man :('

# Simple function to parse logs for docker volumes
def parse_logs():
    data = {}
    with open(LOGS, "r") as f:
        for line in f.readlines():
            if "- -" in line:
                parts = line.split(" ")
                r = parts[-4]

                if r in data:
                    data[r] = data[r] + 1
                else:
                    data[r] = 1

    return data



if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
