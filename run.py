# run.py

import os

from app import create_app
# todo: rename FLASK_ENV
config_name = os.getenv('FLASK_ENV')

app = create_app(config_name)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
