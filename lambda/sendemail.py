import boto3
import json 

print('Loading function') 
dynamo = boto3.client('dynamodb')
ses = boto3.client('ses') # ,region_name='us-east-2')


def respond(err, res=None):
    return {
        'statusCode': '400' if err else '200',
        'body': err.message if err else json.dumps(res),
        'headers': {
            'Content-Type': 'application/json',
        },
    }
    
def send_email(body) :
    response = ses.send_email(
    Destination={
        'ToAddresses': ['akash.gogate@gmail.com']
    },
    Message={
        'Body': {
            'Text': {
                'Charset': 'UTF-8',
                'Data': f"""Request to string the racket with following details :
                        Name : {body['name']}
                        Email : {body['email']}
                        phone : {body['phone']}
                        String Type : {body['stringType']}
                        Racket : {body['racketType']}
                        Model : {body['racketModel']}
                        expedited : {body['expedited']}
                        Strings supplied : {body['stringSupplied']}"""
            }
        },
        'Subject': {
            'Charset': 'UTF-8',
            'Data': 'Stringing order', 
        },
    },
    #Source= body['email']
    Source = 'nandan.gogate@gmail.com'
    )
    
    print("ses send_email response = ",response)


def lambda_handler(event, context):
    print("event = ",event)
    print("context = ", context)
    '''Demonstrates a simple HTTP endpoint using API Gateway. You have full
    access to the request and response payload, including headers and
    status code.

    To scan a DynamoDB table, make a GET request with the TableName as a
    query string parameter. To put, update, or delete an item, make a POST,
    PUT, or DELETE request respectively, passing in the payload to the
    DynamoDB API as a JSON body.
    '''
    #print("Received event: " + json.dumps(event, indent=2))

    operations = {
        'DELETE': lambda dynamo, x: dynamo.delete_item(**x),
        'GET': lambda dynamo, x: dynamo.scan(**x),
        'POST': lambda dynamo, x: dynamo.put_item(**x),
        'PUT': lambda dynamo, x: dynamo.update_item(**x),
    }
    
    operation = event['httpMethod']
    if operation == 'OPTIONS' :
        return {
            'statusCode': '200',
            'body':  json.dumps("OPTIONS OK"),
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': '*',
                'Access-Control-Allow-Headers': '*',
            }
        }
    send_email(json.loads(event['body']))
    return {
            'statusCode': '200',
            'body':  json.dumps("Email Sent"),
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': '*',
                'Access-Control-Allow-Headers': '*',
            }
        }
        
    # if operation in operations:
    #     payload = event['queryStringParameters'] if operation == 'GET' else json.loads(event['body'])
    #     print("payload = ",payload)
    #     return respond(None, operations[operation](dynamo, payload))
    # else:
    #     return respond(ValueError('Unsupported method "{}"'.format(operation)))

