import boto3


def upload_to_aws(local_file, bucket, s3_file, aws_access_key, aws_secret_key):
    """Uploads the given file to AWS S3 using the given credentials and config."""

    s3 = boto3.client(
        "s3", aws_access_key_id=aws_access_key, aws_secret_access_key=aws_secret_key
    )
    s3.upload_file(local_file, bucket, s3_file)
    print("File Upload Successful")
