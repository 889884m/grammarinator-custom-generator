import boto3
import re
import json

# Function to parse the ARN and identify the resource type
def parse_arn(arn):
    arn_regex = r"^arn:([a-zA-Z0-9\-]+):([a-zA-Z0-9\-]+):([a-zA-Z0-9\-]+):([0-9]{12}):([a-zA-Z0-9\-]+)(/.*)?$"
    match = re.match(arn_regex, arn)
    if not match:
        raise ValueError(f"Invalid ARN format: {arn}")

    return match.groups()

# Function to check S3 bucket permissions
def check_s3_permissions(bucket_name):
    s3_client = boto3.client('s3')
    try:
        # Get the bucket policy (if any)
        bucket_policy = s3_client.get_bucket_policy(Bucket=bucket_name)
        policy = json.loads(bucket_policy['Policy'])
        print(f"Bucket {bucket_name} has a policy: {policy}")
    except s3_client.exceptions.NoSuchBucketPolicy:
        print(f"Bucket {bucket_name} has no policy.")

    # Check for public access block
    public_access = s3_client.get_bucket_policy_status(Bucket=bucket_name)
    print(f"Public access blocked for bucket {bucket_name}: {public_access}")

# Function to check EC2 instance permissions (basic example)
def check_ec2_permissions(instance_id, region):
    ec2_client = boto3.client('ec2', region)
    try:
        instance = ec2_client.describe_instances(InstanceIds=[instance_id])
        if instance['Reservations']:
            print(f"Instance {instance_id} exists.")
        else:
            print(f"Instance {instance_id} does not exist.")
    except Exception as e:
        print(f"Error describing EC2 instance {instance_id}: {e}")

# Function to check IAM role permissions (basic example)
def check_iam_role_permissions(role_name):
    iam_client = boto3.client('iam')
    try:
        role_policy = iam_client.list_role_policies(RoleName=role_name)
        print(f"Role {role_name} has the following inline policies: {role_policy['PolicyNames']}")
    except iam_client.exceptions.NoSuchEntityException:
        print(f"Role {role_name} does not exist.")

# Main function to handle ARN and perform checks
def audit_arn(arn):
    try:
        # Parse ARN and extract components
        partition, service, region, account_id, resource_type, resource_id = parse_arn(arn)
        print(f"Auditing ARN: {arn}")
        print(f"Service: {service}, Resource Type: {resource_type}, Resource ID: {resource_id}")

        # Perform audits based on the resource type
        if service == 's3' and resource_type == 'bucket':
            check_s3_permissions(resource_id)
        elif service == 'ec2' and resource_type == 'instance':
            check_ec2_permissions(resource_id, region)
        elif service == 'iam' and resource_type == 'role':
            check_iam_role_permissions(resource_id)
        else:
            print(f"Audit for resource type {resource_type} not implemented.")

    except ValueError as e:
        print(f"Error: {e}")

# Example custom ARNs for testing
arn_examples = [
    'arn:aws:s3:::my-secure-bucket',
    'arn:aws:ec2:us-west-2:123456789012:instance/i-0abcdef1234567890',
    'arn:aws:iam::123456789012:role/AdminRole',
]

# Main loop for auditing multiple ARNs
if __name__ == '__main__':
    for arn in arn_examples:
        audit_arn(arn)

