import json
import os
import random
import time
import datetime

import psutil
import requests

NODE_ID = 1
API = 'http://59.106.215.39:8000/tala/api/v1/nodes/{0}/metrics/'.format(NODE_ID)
HEADER = {'Content-Type': 'application/json'}


def datetime_handler(x):
    if isinstance(x, datetime.datetime):
        return x.isoformat()
    raise TypeError("Unknown type")


while 1:
    date = datetime.datetime.now()
    time.sleep(1)
    la_1m, la_5m, la_15m = os.getloadavg()
    memory = psutil.virtual_memory()

    requests.post(API, headers=HEADER, data=json.dumps({'date': date,
                                                        'metrics_type': 'cpu_load_average_1m',
                                                        'value': la_1m,
                                                        'unit': 'VALUE'},
                                                       default=datetime_handler))
    requests.post(API, headers=HEADER, data=json.dumps({'date': date,
                                                        'metrics_type': 'cpu_load_average_5m',
                                                        'value': la_5m,
                                                        'unit': 'VALUE'},
                                                       default=datetime_handler))
    requests.post(API, headers=HEADER, data=json.dumps({'date': date,
                                                        'metrics_type': 'cpu_load_average_15m',
                                                        'value': la_15m,
                                                        'unit': 'VALUE'},
                                                       default=datetime_handler))
    requests.post(API, headers=HEADER, data=json.dumps({'date': date,
                                                        'metrics_type': 'memory_total',
                                                        'value': memory.total,
                                                        'unit': 'VALUE'},
                                                       default=datetime_handler))
    requests.post(API, headers=HEADER, data=json.dumps({'date': date,
                                                        'metrics_type': 'memory_used',
                                                        'value': memory.used,
                                                        'unit': 'VALUE'},
                                                       default=datetime_handler))
    requests.post(API, headers=HEADER, data=json.dumps({'date': date,
                                                        'metrics_type': 'memory_free',
                                                        'value': memory.free,
                                                        'unit': 'VALUE'},
                                                       default=datetime_handler))
    requests.post(API, headers=HEADER, data=json.dumps({'date': date,
                                                        'metrics_type': 'memory_free',
                                                        'value': memory.free,
                                                        'unit': 'VALUE'},
                                                       default=datetime_handler))

    requests.post(API, headers=HEADER, data=json.dumps({'date': date,
                                                        'metrics_type': 'disk_read',
                                                        'value': random.uniform(1, 20000),
                                                        'unit': 'VALUE'},
                                                       default=datetime_handler))

    requests.post(API, headers=HEADER, data=json.dumps({'date': date,
                                                        'metrics_type': 'disk_write',
                                                        'value': random.uniform(1, 20000),
                                                        'unit': 'VALUE'},
                                                       default=datetime_handler))

    requests.post(API, headers=HEADER, data=json.dumps({'date': date,
                                                        'metrics_type': 'network_incoming',
                                                        'value': random.uniform(1, 20000),
                                                        'unit': 'VALUE'},
                                                       default=datetime_handler))

    requests.post(API, headers=HEADER, data=json.dumps({'date': date,
                                                        'metrics_type': 'network_outgoing',
                                                        'value': random.uniform(1, 20000),
                                                        'unit': 'VALUE'},
                                                       default=datetime_handler))


    #disk = psutil.disk_io_counters()
    #print(disk.read_count)

    #network = psutil.net_io_counters()
    #print(network)
