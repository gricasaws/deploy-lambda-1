import json

def lambda_handler(event, context):
    print(json.dumps(event))
    return {
        'status': 200,
        'headers': {
            'Content-Type': 'application/json'
        },
    # This is a comment by Gregory from ZiyoTek
        'body': json.dumps({'message': 'OK-Tested'})
    }
