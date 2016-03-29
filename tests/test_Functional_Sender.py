import os

from unittest import TestCase, skipIf
from time import time as now

from pyzabbix import ZabbixMetric, ZabbixSender, ZabbixResponse


@skipIf('TRAVIS' not in os.environ.keys(), "Travis CI test")
class FunctionalSender(TestCase):
    def test_sendMetricsToServer(self):
        cur_date_unix = int(now())
        m = [
            ZabbixMetric('host2', 'key3', 'IDDQD'),
            ZabbixMetric('host1', 'key1', 33.1, cur_date_unix)
        ]

        z = ZabbixSender('127.0.0.1', 10051).send(m)
        print(z.__repr__())
        self.assertIsInstance(z, ZabbixResponse)
