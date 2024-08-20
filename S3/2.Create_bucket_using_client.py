import boto3

client = boto3.client('s3')

response = client.create_bucket(
    Bucket='arun-s3-client-bucket'
)

print(response)
