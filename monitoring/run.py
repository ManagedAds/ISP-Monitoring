import os
import sys
sys.path.append(os.getcwd())

from monitoring import config
from monitoring.scheduler import app

if not config.CLIENT_TOKEN:
    raise RuntimeError('please provide your client token to launch monitoring app')

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
