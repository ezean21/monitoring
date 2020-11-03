#!/usr/bin/env python

import click
from base_monitors import BaseS3MonitoringSystem


@click.group()
def cli():
    pass


class S3E2EMonitoring(BaseS3MonitoringSystem):
    def __init__(self, bucket_name, aws_access_key_id, aws_secret_access_key):
        super().__init__(bucket_name, aws_access_key_id, aws_secret_access_key)

    def run(self):
        self.s3.put_object(b'E2E Monitoring System', self.key)
        self.s3.get_object(self.key)
        self.s3.delete(self.key)


class S3ListAll(BaseS3MonitoringSystem):
    def __init__(self, bucket_name, aws_access_key_id, aws_secret_access_key):
        super().__init__(bucket_name, aws_access_key_id, aws_secret_access_key)

    def run(self):
        self.s3.list_objects()


@cli.command()
@click.option('--monitor-name', '-m', help="Monitor name to run")
@click.option('--resource-name', '-r', help="Resource Name to monitor")
@click.option('--aws-access-key-id', envvar='AWS_ACCESS_KEY_ID', help="AWS_ACCESS_KEY_ID")
@click.option('--aws-secret-access-key', envvar='AWS_SECRET_ACCESS_KEY', help="AWS_SECRET_ACCESS_KEY")
def run(monitor_name, resource_name, aws_access_key_id, aws_secret_access_key):
    globals()[monitor_name](resource_name, aws_access_key_id, aws_secret_access_key).run()


if __name__ == "__main__":
    cli()
