import boto3

client = boto3.client('s3')
bucket_name = 'arun-boto3-test'

with open('S3/sample_files/file1.txt', 'rb') as f:
    data = f.read()

response = client.put_object(
    Body=data,
    Bucket=bucket_name,
    Key='file1.txt'
)

print(response)
