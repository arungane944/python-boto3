import boto3

'''

buckets = boto3.client('s3')

response = buckets.list_buckets()

for bucket in response["Buckets"]:
    print(bucket["Name"])

'''


resource = boto3.resource('s3')

response = resource.buckets.all()

for bucket in response:
    print(bucket.name)