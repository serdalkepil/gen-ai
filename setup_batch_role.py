import boto3
import json

def create_bedrock_batch_role():
    """Create IAM role for Bedrock batch inference"""
    
    iam = boto3.client('iam')
    
    # Trust policy for Bedrock
    trust_policy = {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Principal": {
                    "Service": "bedrock.amazonaws.com"
                },
                "Action": "sts:AssumeRole"
            }
        ]
    }
    
    # Permissions policy
    permissions_policy = {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Action": [
                    "s3:GetObject",
                    "s3:PutObject",
                    "s3:PutObjectAcl",
                    "s3:ListBucket"
                ],
                "Resource": [
                    "arn:aws:s3:::*",
                    "arn:aws:s3:::*/*"
                ]
            },
            {
                "Effect": "Allow",
                "Action": [
                    "bedrock:InvokeModel"
                ],
                "Resource": "*"
            }
        ]
    }
    
    try:
        # Create role
        role_response = iam.create_role(
            RoleName='BedrockBatchRole',
            AssumeRolePolicyDocument=json.dumps(trust_policy),
            Description='Role for Bedrock batch inference jobs'
        )
        
        # Attach policy
        iam.put_role_policy(
            RoleName='BedrockBatchRole',
            PolicyName='BedrockBatchPolicy',
            PolicyDocument=json.dumps(permissions_policy)
        )
        
        print(f"Created role: {role_response['Role']['Arn']}")
        return role_response['Role']['Arn']
        
    except iam.exceptions.EntityAlreadyExistsException:
        role = iam.get_role(RoleName='BedrockBatchRole')
        print(f"Role already exists: {role['Role']['Arn']}")
        return role['Role']['Arn']

if __name__ == "__main__":
    create_bedrock_batch_role()