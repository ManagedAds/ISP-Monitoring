import os
import sys
sys.path.append(os.getcwd())

from monitoring.scheduler import app

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
