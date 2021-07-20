import json
import os

import boto3

from domain.agency import Agency
from utils import response_util, logger_util

logging = logger_util.logger('registration_agency')
table_name = os.environ.get('TABLEAGENCY', 'Agency')
region = os.environ.get('REGION', 'sa-east-1')
dynamodb = boto3.resource(
    'dynamodb',
    region_name=region
)


def lambda_handler(message, context):
    logging.info('starting agency.py registration process...')
    logging.info(f'message received {message}')

    table = dynamodb.Table(table_name)
    agency = json.loads(message['body'], object_hook=Agency.to_domain)

    response = table.put_item(
        TableName=table_name,
        Item=agency.to_dict()
    )
    logging.info(f'agency.py save with success ... {response}')

    return response_util.created(agency.to_dict())
