import boto3
from werkzeug.utils import secure_filename
from config import Config

s3 = boto3.client("s3")


def upload_file_to_s3(file, bucket_name=None, acl="public-read"):
    """
    Docs: http://boto3.readthedocs.io/en/latest/guide/s3.html
    """
    if bucket_name is None:
        bucket_name = Config.BUCKET_NAME
    filename = secure_filename(file.filename)
    try:
        s3.upload_fileobj(
            file,
            bucket_name,
            filename,
            ExtraArgs={
                "ACL": acl,
                "ContentType": file.content_type    #Set appropriate content type as per the file
            }
        )
    except Exception as e:
        print("Something Happened: ", e)
        return e
    return f"https://{bucket_name}.s3.{Config.S3_LOCATION}.amazonaws.com/{filename}"
