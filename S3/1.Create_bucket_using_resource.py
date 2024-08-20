import boto3

bucket = boto3.resource('s3')

response = bucket.create_bucket(
    Bucket = "arun-boto3-test"
)

print(response)
