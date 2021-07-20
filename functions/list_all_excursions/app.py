import os
from collections import defaultdict

import boto3

from utils import response_util, logger_util

logging = logger_util.logger('list_all_excursions')
table_name = os.environ.get('TABLEEXCURSION', 'Excursion')
region = os.environ.get('REGION', 'sa-east-1')
dynamodb = boto3.resource(
    'dynamodb',
    region_name=region,
)


def lambda_handler(message, context):
    logging.info(f'message received list_all_excursions {message}')

    table = dynamodb.Table(table_name)
    response = table.scan()['Items']

    logging.info(f'list excursions that was found ... {response}')

    dictionary = defaultdict(list)
    for r in response:
        agency_id = r['agencyId']
        dictionary[agency_id].append(r)

    return response_util.ok(dictionary)
