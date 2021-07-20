import json
import os
import uuid

import boto3

from utils import response_util, logger_util
from domain.enum import reservation_status as rs

logging = logger_util.logger('pre_reservation_excursion')
table_name = os.environ.get('TABLERESERVATION', 'Reservation')
region = os.environ.get('REGION', 'sa-east-1')
dynamodb = boto3.resource(
    'dynamodb',
    region_name=region,
)


def lambda_handler(message, context):
    logging.info(f'message received pre_reservation_excursion {message}')

    agency_id = message['pathParameters']['agencyId']
    excursion_id = message['pathParameters']['excursionId']
    pre_reservation = json.loads(message['body'])

    table = dynamodb.Table(table_name)
    params = {
        'id': str(uuid.uuid4()),
        'excursionId': excursion_id,
        'who': pre_reservation['who'],
        'amount': pre_reservation['amount'],
        'status': rs.PRE_RESERVED,
        'externalAgency': agency_id != pre_reservation['who']
    }

    table.put_item(
        TableName=table_name,
        Item=params
    )

    logging.info(f'success to pre reserve {excursion_id}')
    return response_util.created(params)
