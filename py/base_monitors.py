import os
import logging
from abc import abstractmethod
from s3 import S3

logging.basicConfig(filename='/logs/monitoring.log', level=logging.INFO)


class BaseS3MonitoringSystem(object):
    def __init__(self, bucket_name, aws_access_key_id, aws_secret_access_key):
        self.s3 = S3(bucket_name, aws_access_key_id, aws_secret_access_key, logging)
        self.key = os.urandom(32)

    @abstractmethod
    def run(self):
        pass
