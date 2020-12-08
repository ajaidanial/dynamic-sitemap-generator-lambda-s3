import json
import os

import boto3


def upload_to_aws(local_file, bucket, s3_file, aws_access_key, aws_secret_key):
    """Uploads the given file to AWS S3 using the given credentials and config."""

    s3 = boto3.client(
        "s3", aws_access_key_id=aws_access_key, aws_secret_access_key=aws_secret_key
    )
    s3.upload_file(local_file, bucket, s3_file, ExtraArgs={"ACL": "public-read"})
    print("File Upload Successful")


def generate_sitemap():
    """
    This function uses the third party library `https://github.com/c4software/python-sitemap`
    to generate the sitemap in the project root. This uses the configuration from `config.json`.
    Visit the link to find more docs about the config file.
    """

    os.system("python libraries/python-sitemap/main.py --config config.json")
    print("Sitemap generated")


def get_configurations():
    """This function returns the defined configuration in the project root in `config.json`."""

    config_data = open("config.json", "r")
    config = json.load(config_data)
    config_data.close()
    return config


def lambda_handler(event, context):
    """
    This is the main function called in AWS lambda. This calls the other
    child functions to get the job done. The event and context are given by lambda.
    """

    config = get_configurations()  # all defined configurations
    generate_sitemap()  # generates the temp sitemap
    upload_to_aws(
        local_file=config["output"],
        bucket=config["s3_bucket_name"],
        s3_file=config["output"],
        aws_access_key=config["aws_access_key"],
        aws_secret_key=config["aws_secret_key"],
    )  # uploads the sitemap
    os.remove(config["output"])  # removes the temp sitemap


if __name__ == "__main__":
    lambda_handler(None, {})
