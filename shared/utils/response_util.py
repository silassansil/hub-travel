import json

from utils import encoder_util


def bad_request():
    return {
        'statusCode': 400,
        'headers': {
            "Access-Control-Allow-Headers" : "*",
            "Access-Control-Allow-Origin": "*",  
            "Access-Control-Allow-Methods": "*" 
        },
        'body': json.dumps({'message': 'bad request'})
    }


def created(_body):
    return {
        'statusCode': 201,
        'headers': {
            "Access-Control-Allow-Headers" : "*",
            "Access-Control-Allow-Origin": "*",  
            "Access-Control-Allow-Methods": "*" 
        },
        'body': json.dumps(_body)
    }


def ok(_body):
    return {
        'statusCode': 200,
        'headers': {
            "Access-Control-Allow-Headers" : "*",
            "Access-Control-Allow-Origin": "*",  
            "Access-Control-Allow-Methods": "*" 
        },
        'body': json.dumps(_body, cls=encoder_util.DecimalEncoder)
    }


def not_found(_id):
    return {
        'statusCode': 404,
        'headers': {
            "Access-Control-Allow-Headers" : "*",
            "Access-Control-Allow-Origin": "*",  
            "Access-Control-Allow-Methods": "*" 
        },
        'body': json.dumps({'message': f'resource not found {_id}'})
    }
