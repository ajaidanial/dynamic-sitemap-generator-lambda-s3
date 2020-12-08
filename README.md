# dynamic-sitemap-generator-lambda

Consider you are hosting your site using AWS S3. The site contains plain HTML files.
You want to update your sitemap.xml as soon as your uploaded file goes into production.
This repo helps you by automating the process.

## Using Locally
1. Create the virtual environment, install the requirements and activate the venv.
2. Update your configurations in `config.json`.
3. Run the app using `python lambda_function.py`.

## Production

The app is configured in a way to be deployed using AWS lambda. Just push the app and create an
AWS lambda function. Add a trigger to the function saying this has to be called when a new HTML file
is to be uploaded in the bucket. This functions does the rest. Remember to add the trigger only for
.html files or it might cause a recursive loop.

## Other Links
1. [python-sitemap](https://github.com/c4software/python-sitemap)
2. [Boto Upload](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/s3-uploading-files.html)
3. [Setting Up Lambda](https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/RunLambdaSchedule.html)
