import json
import os
import uuid

import boto3

from utils import response_util, logger_util
import time

logging = logger_util.logger('booking_excursion')
table_name = os.environ.get('TABLEEXCURSION', 'Excursion')
region = os.environ.get('REGION', 'sa-east-1')
dynamodb = boto3.resource(
    'dynamodb',
    region_name=region
)


def lambda_handler(message, context):
    logging.info(f'message received {message}')

    agency_id = message['pathParameters']['agencyId']
    logging.info(f'booking excursion to {agency_id}')

    table = dynamodb.Table(table_name)
    excursion = json.loads(message['body'])

    params = {
        'id': str(uuid.uuid4()),
        # 'date': excursion['date'],
        'date': int(round(time.time() * 1000)),
        'agencyId': agency_id,
        'destination': excursion['destination'],
        'totalVacancies': excursion['totalVacancies']
    }

    table.put_item(
        TableName=table_name,
        Item=params
    )

    logging.info(f'destination was booked to {params["destination"]} at {params["date"]}')
    return response_util.ok(params)
