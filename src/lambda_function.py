import json
from bid_adjuster import adjust_bids

def lambda_handler(event, context):
    result = adjust_bids()
    return {
        'statusCode': 200,
        'body': json.dumps(result)
    }
