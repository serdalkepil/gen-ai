import json
import boto3

# Initialize Bedrock client
bedrock_client = boto3.client('bedrock-runtime')

def lambda_handler(event, context):
    # Parse the request body
    body = json.loads(event['body'])
    customer = body.get('customer', '')
    name = body.get('name', '')
    title = body.get('title', '')
    target = body.get('target', '')

    prompt = f"""
    Command: Write an email from {name}, {title}, AnyCompany to the customer "{customer}" 
    who provided negative feedback on the service provided by our {target}.
    """
    
    # Create request body for Nova Lite
    request_body = json.dumps({
        "messages": [
            {
                "role": "user",
                "content": [{"text": prompt}]
            }
        ],
        "inferenceConfig": {
            "maxTokens": 2048,
            "temperature": 0,
            "topP": 0.9
        }
    })
    
    # Invoke the model
    response = bedrock_client.invoke_model(
        body=request_body,
        modelId='amazon.nova-lite-v1:0'
    )
    
    # Parse response
    response_body = json.loads(response.get('body').read())
    email = response_body.get('output').get('message').get('content')[0].get('text')
    
    return {
        'statusCode': 200,
        'body': json.dumps({'email': email})
    }
