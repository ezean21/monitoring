import boto3


class S3(object):
    def __init__(self, bucket_name, aws_access_key_id, aws_secret_access_key, logging):
        self.bucket_name = bucket_name
        self.client = boto3.client('s3',
                                   aws_access_key_id=aws_access_key_id,
                                   aws_secret_access_key=aws_secret_access_key)
        self.logging = logging

    def put_object(self, body, key):

        try:
            res = self.client.put_object(self.bucket_name, Body=body, Key=key)
            self.logging.info(res)
        except Exception as e:
            self.logging.critical(e)

    def list_objects(self):

        try:
            res = self.client.list_objects(Bucket=self.bucket_name)
            self.logging.info(res)
        except Exception as e:
            self.logging.critical(e)

    def get_object(self, key):

        try:
            res = self.client.get_object(Key=key, Bucket=self.bucket_name)
            self.logging.info(res)
        except Exception as e:
            self.logging.critical(e)

    def delete(self, key):
        try:
            res = self.client.delete_object(Key=key, Bucket=self.bucket_name)
            self.logging.info(res)
        except Exception as e:
            self.logging.critical(e)
