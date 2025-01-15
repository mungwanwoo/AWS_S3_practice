import boto3

from dotenv import load_dotenv
import os
load_dotenv()
import mimetypes
# AWS 액세스 키와 시크릿 키를 설정합니다.
AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')


s3=boto3.client('s3',aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_SECRET_ACCESS_KEY)

# 파일 업로드
def upload_file(file_name, bucket_name, object_name=None):
    """파일을 S3 버킷에 업로드합니다."""
    if object_name is None:
        object_name = file_name
    content_type=mimetypes.guess_type(file_name)[0]

    try:
        s3.upload_file(file_name, bucket_name, object_name, ExtraArgs={"ContentType":content_type})
    except Exception as e:
        print(e)
        return False
    return True

# 파일 다운로드
def download_file(bucket_name, object_name, file_name=None):
    """S3 버킷에서 파일을 다운로드합니다."""
    if file_name is None:
        file_name = object_name

    try:
        s3.download_file(bucket_name, object_name, file_name)
    except Exception as e:
        print(e)
        return False
    return True

# 파일 업로드 예시
upload_file('fox.jpg', 'likelionmgw')
# 파일 다운로드 예시
download_file('likelionmgw', 'fox.jpg', './media/animal/tiger.jpg')