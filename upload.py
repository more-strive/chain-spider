import boto3
from config import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_ENDPOINT, AWS_DEFAULT_REGION


session = boto3.Session(
   aws_access_key_id=AWS_ACCESS_KEY_ID,
   aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
   region_name='ap-east-1' #这个必须加，不然会报错，此处根据自己的 s3 地区位置改变
)


def get_file(s3, bucket_name, filename):
	return s3.get_object(
		Bucket=bucket_name,
		Key=filename,
	)


def put_file(s3, bucket_name, filename, upfile):
	return s3.put_object(
		Bucket=bucket_name,
		Body=open(upfile, 'rb'),
		Key=filename,
	)


def have_bucket(s3, bucket_name):
	buckets = s3.list_buckets()['Buckets']
	for bucket in buckets:
		if bucket_name == bucket['Name']:
			return True
	
	return False




