# Problem-Statement :


# vpc-lambda
> AWS Lambda – VPC & Subnet Provisioning with DynamoDB Storage

>     Creates a VPC in a user-specified region
> 
>     Creates multiple subnets using user-provided CIDR blocks
> 
>     Stores VPC and subnet metadata in DynamoDB
> 
>     Retrieves stored VPC information from Dynamodb

# Services used:

    - AWS Lambda
    - AWS EC2 - VPC
    - AWS DynamoDB

# Features

 - Create VPC with custom CIDR
 - Create multiple subnets
 - Store infrastructure metadata in DynamoDB
 - Retrieve VPC information by VPC ID
 - JSON-based input structure

# IAM Role for Lambda:

# Lambda Runtime

    Python 3.14
    Boto3

# Input Parameters - POST
Resource path : /create
| Field        | Type   | Required | Description          |
| ------------ | ------ | -------- | -------------------- |
| region       | string | Yes      | AWS region           |
| vpc_cidr     | string | Yes      | CIDR block for VPC   |
| subnet_cidrs | list   | Yes      | List of subnet CIDRs |
| x-api-key    | Header | Yes      | Authenticate api     |

# Event Payload Examples
```python
    {
  "region": "us-east-1",
  "vpc_cidr": "10.0.0.0/16",
  "subnet_cidrs": [
    "10.0.1.0/24",
    "10.0.2.0/24",
    "10.0.3.0/24"
  ]
}
```


# Input Parameters - GET
Resource path : /getALL

# Input Parameters - GET
Resource path : /get
| Field        | Type   | Required | Description          |
| ------------ | ------ | -------- | -------------------- |
| region       | string | Yes      | AWS region           |
| vpc_id       | string | Yes      | CIDR block for VPC   |
| x-api-key    | Header | Yes      | Authenticate api     |
# Event Payload Examples
```python
    {
  "region": "us-east-1",
  "vpc_id": "vpc-******"
}
# Deployment Steps :
    # Codepipeline - https://us-east-1.console.aws.amazon.com/codesuite/codepipeline/pipelines/vpc-lambda-pipeline/view?region=us-east-1
    ![alt text](image.png)

# Integration Testing :
    - aws Apigateway - https://p4mhyzuwvh.execute-api.us-east-1.amazonaws.com/Dev
    ![alt text](image-1.png)


