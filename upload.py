import boto3
from config import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_ENDPOINT, AWS_DEFAULT_REGION, AWS_BUCKET


def uploadFileToS3(chain, filename):
  if filename is None:
    raise ValueError("Please enter a valid and complete file path")

  session = boto3.Session(
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name=AWS_DEFAULT_REGION
  )
  s3 = session.client("s3")
  s3.upload_file(Filename=filename, Key=f"{chain}/{filename}", Bucket=AWS_BUCKET)


if __name__ == "__main__":
  uploadFileToS3()