# Text Summarizer Lambda Function

This SAM application deploys a Lambda function that generate text using Amazon Bedrock's Nova Lite model, exposed via API Gateway.

## Deployment

1. Install SAM CLI if not already installed
2. Build the package to be deployed to Lambda
   ```bash
   sam build
   ```
2. Deploy the template
   ```bash
   sam deploy --guided
   ```

## Usage

Send a POST request to the API endpoint with JSON body:

```json
{
  "customer": "John Doe",
  "name": "Bob",
  "title": "Customer Service Manager",
  "target": "Support Engineer"
}
```

Example using curl:
```bash
curl -X POST https://your-api-id.execute-api.region.amazonaws.com/Prod/generate_email \
  -H "Content-Type: application/json" \
  -d '{ "customer": "John Doe", "name": "Bob", "title": "Customer Service Manager", "target": "Support Engineer" }'
```

## Response

Success response:
```json
{
  "email": "Generated email text..."
}
```
