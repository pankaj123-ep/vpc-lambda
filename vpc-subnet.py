import json
import boto3
import uuid
from datetime import datetime

DYNAMODB_TABLE = "VpcMetadata"

def lambda_handler(event, context):
    print(json.dumps(event)) # event logging for debugging
    action = event.get("httpMethod")
    path = event.get("path")

    if action == "POST" and path == "/create":
        return create_vpc_and_subnets(event)
    elif action == "GET" and path == "/getALL":
        return get_vpc_from_dynamodb(event)
    elif action == "GET" and path == "/get/{id}":
        return get_vpc_from_dynamodb(event)
    else:
        return response(400, {"message": "Invalid action. Use 'create' or 'get'."})


def create_vpc_and_subnets(event):
    print(event)
    body = json.loads(event.get("body"))
    region = body["region"]
    vpc_cidr = body["vpc_cidr"]
    subnet_cidrs = body["subnet_cidrs"]  # list expected
    print(f"Received parameters - Region: {region}, VPC CIDR: {vpc_cidr}, Subnet CIDRs: {subnet_cidrs}")

    if not region or not vpc_cidr or not subnet_cidrs:
        return response(400, {"message": "region, vpc_cidr and subnet_cidrs are required fields and subnet_cidrs should be a list."})

    ec2 = boto3.client("ec2", region_name=region)
    dynamodb = boto3.resource("dynamodb", region_name=region)
    table = dynamodb.Table(DYNAMODB_TABLE)

    try:
        # Create VPC
        vpc_response = ec2.create_vpc(CidrBlock=vpc_cidr)
        vpc_id = vpc_response["Vpc"]["VpcId"]

        subnets = []
        for cidr in subnet_cidrs:
            subnet_response = ec2.create_subnet(
                VpcId=vpc_id,
                CidrBlock=cidr
            )
            subnet_id = subnet_response["Subnet"]["SubnetId"]

            subnets.append({
                "SubnetId": subnet_id,
                "CidrBlock": cidr
            })

        # Store metadata in DynamoDB
        item = {
            "VpcId": vpc_id,
            "VpcCidr": vpc_cidr,
            "Region": region,
            "Subnets": subnets,
            "CreatedAt": datetime.datetime.now().isoformat()
        }

        table.put_item(Item=item)

        return response(200, {
            "message": "VPC and subnets created successfully",
            "VpcId": vpc_id,
            "Subnets": subnets
        })

    except Exception as e:
        return response(500, {"error": str(e)})


def get_vpc_from_dynamodb(event):
    region = event.get("region")
    vpc_id = event.get("vpc_id")

    if not region or not vpc_id:
        return response(400, {"message": "region and vpc_id are required"})

    dynamodb = boto3.resource("dynamodb", region_name=region)
    table = dynamodb.Table(DYNAMODB_TABLE)

    try:
        result = table.get_item(Key={"VpcId": vpc_id})

        if "Item" not in result:
            return response(404, {"message": "VPC not found in DynamoDB"})

        return response(200, result["Item"])

    except Exception as e:
        return response(500, {"error": str(e)})


def response(status_code, body):
    return {
        "statusCode": status_code,
        "body": json.dumps(body)
    }
