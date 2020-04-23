import boto3
from botocore.exceptions import NoCredentialsError


def upload_to_aws(local_file, bucket, s3_file):
    s3 = boto3.client('s3')

    try:
        s3.upload_file(local_file, bucket, s3_file)
        print("Upload Successful")
        return True
    except FileNotFoundError:
        print("The file was not found")
        return False
    except NoCredentialsError:
        print("Credentials not available")
        return False

local_file = 'C:\\Users\\revam\\Downloads\\tripdata_2019-01.csv'

uploaded = upload_to_aws(local_file, 'db-task-01', 'tripdata_2019-01.csv')