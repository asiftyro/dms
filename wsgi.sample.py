import os
import sys
import time

path = '/home/your-username/your-project-directory-name'
if path not in sys.path:
    sys.path.append(path)

os.environ['FLASK_ENV'] = 'production'  # options: development, production
os.environ["TZ"] = "Asia/Dhaka"

time.tzset()
from run import app as application

