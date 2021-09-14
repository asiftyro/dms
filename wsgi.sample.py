import os
import sys

path = '/home/your-username/your-project-directory-name'
if path not in sys.path:
    sys.path.append(path)

os.environ['FLASK_ENV'] = 'production'  # development

from run import app as application
