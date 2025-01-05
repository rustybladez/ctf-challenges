import boto3
from botocore.client import Config

# Define the custom endpoint (MinIO or S3 service running on a custom port)
endpoint_url = 'http://challenge.ctf.games:31744'

# Create a session without needing actual AWS credentials (assuming public buckets)
s3 = boto3.resource('s3', endpoint_url=endpoint_url, config=Config(signature_version='s3v4'))

# List all available buckets
for bucket in s3.buckets.all():
    print(f"Bucket found: {bucket.name}")

    # List objects in each bucket
    for obj in bucket.objects.all():
        print(f" - {obj.key}")

        # Optionally, download an object if you find something interesting (like flag.txt)
        if "flag.txt" in obj.key:
            s3.Bucket(bucket.name).download_file(obj.key, 'flag.txt')
            print("Flag downloaded as flag.txt!")
