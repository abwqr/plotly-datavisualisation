import boto3
import os
from s3_info import AWS_REGION, S3_BUCKET_NAME

client = boto3.client("s3", region_name=AWS_REGION)
resource = boto3.resource('s3')
response = client.list_buckets()
print("Listing Amazon S3 Buckets:")
for bucket in response['Buckets']:
    print(f"-- {bucket['Name']}")

s3_resource = boto3.resource("s3", region_name=AWS_REGION)
s3_bucket = s3_resource.Bucket(S3_BUCKET_NAME)
print('Listing Amazon S3 Bucket objects/files:')

for s3_object in s3_bucket.objects.all():
    path, filename = os.path.split(s3_object.key)
    print(path, filename)
    s3_bucket.download_file(s3_object.key, "data/"+filename)
