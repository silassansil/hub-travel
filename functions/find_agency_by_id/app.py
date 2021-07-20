import os

import boto3
from boto3.dynamodb.conditions import Key

from utils import response_util, logger_util

logging = logger_util.logger('find_agency_by_id')
table_name = os.environ.get('TABLEAGENCY', 'Agency')
region = os.environ.get('REGION', 'sa-east-1')
dynamodb = boto3.resource(
    'dynamodb',
    region_name=region
)


def lambda_handler(message, context):
    logging.info(f'message received {message}')

    table = dynamodb.Table(table_name)

    agency_id = message['pathParameters']['agencyId']
    response = table.query(
        KeyConditionExpression=Key('id').eq(agency_id)
    )['Items']

    if response:
        logging.info(f'list with agencies found ... {response}')
        return response_util.ok(response[0])
    else:
        logging.error(f'agency.py was not found ... {agency_id}')
        return response_util.not_found(agency_id)
