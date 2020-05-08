import atexit as atexit

import sentry_sdk
from flask import Flask, jsonify
from sentry_sdk.integrations.flask import FlaskIntegration
from apscheduler.schedulers.background import BackgroundScheduler

from monitoring import config
from monitoring.monitor import schedule_isp_check

sentry_sdk.init(
    dsn=config.REPORT_EXCEPTIONS_ENDPOINT,
    integrations=[FlaskIntegration()]
)

app = Flask(__name__)
scheduler = BackgroundScheduler()
scheduler.add_job(func=schedule_isp_check, trigger="interval", minutes=1)
scheduler.start()
atexit.register(lambda: scheduler.shutdown())


@app.route("/", methods=["GET"])
def index_route():
    return jsonify({"message": "service up and running"})
