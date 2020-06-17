import json
import os
from datetime import datetime

from ping3 import ping

from monitoring import config
from monitoring.reporter import Reporter


def check_latency():
    host = '8.8.8.8'
    unit = 'ms'
    latency = round(ping(host, unit=unit), 2)
    payload = {
        'host': host,
        'latency': latency,
        'latency_measurement': unit
    }
    Reporter().report_latency(payload)


def check_speed():
    speed_test_results_raw = os.popen("speedtest-cli --json").read()
    payload = json.loads(speed_test_results_raw)
    Reporter().report_speed(payload)


def schedule_isp_check():
    now = datetime.now()
    check_latency()
    if now.minute == 0 and now.hour % config.EVERY_X_HOUR == 0:
        check_speed()
