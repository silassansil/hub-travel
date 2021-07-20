import os

import boto3

from utils import response_util, logger_util

logging = logger_util.logger('list_all_agencies')
table_name = os.environ.get('TABLEAGENCY', 'Agency')
region = os.environ.get('REGION', 'sa-east-1')
dynamodb = boto3.resource(
    'dynamodb',
    region_name=region
)


def lambda_handler(message, context):
    logging.info(f'message received list_all_agencies {message}')

    table = dynamodb.Table(table_name)
    response = table.scan()['Items']

    logging.info(f'list agencies that was found ... {response}')

    response = {
        r['id']: r for r in response
    }

    return response_util.ok(response)
