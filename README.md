# vpc-lambda
> AWS Lambda – VPC & Subnet Provisioning with DynamoDB Storage

>     Creates a VPC in a user-specified region
> 
>     Creates multiple subnets using user-provided CIDR blocks
> 
>     Stores VPC and subnet metadata in DynamoDB
> 
>     Retrieves stored VPC information from Dynamo

# Services used:

    AWS Lambda
    AWS EC2
    AWS DynamoDB

# Features

Create VPC with custom CIDR
Create multiple subnets
Store infrastructure metadata in DynamoDB
Retrieve VPC information by VPC ID
JSON-based input structure
Multi-region support

# IAM Role for Lambda:

# Lambda Runtime

    Python 3.14
    Boto3

# Input Parameters - POST

| Field        | Type   | Required | Description          |
| ------------ | ------ | -------- | -------------------- |
| httpMethod   | string | Yes      | Must be `"POST"`   |
| region       | string | Yes      | AWS region           |
| vpc_cidr     | string | Yes      | CIDR block for VPC   |
| subnet_cidrs | list   | Yes      | List of subnet CIDRs |

# Event Payload Examples
```python
    {
  "httpMethod": "post",
  "region": "us-east-1",
  "vpc_cidr": "10.0.0.0/16",
  "subnet_cidrs": [
    "10.0.1.0/24",
    "10.0.2.0/24",
    "10.0.3.0/24"
  ]
}
```


# Input Parameters - GETALL

# Input Parameters - GET by ID

# Deployment Steps :
    # Codepipeline - 

