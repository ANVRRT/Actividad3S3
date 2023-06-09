import json
import boto3
import base64
from s3_manager import S3Manager

def upload_image(image64, filename):
    try:
        s3_manager = S3Manager()

        bucket = "drimteam"
        filepath = f"dreamteam/{filename}.jpg"

        imageBytes = base64.b64decode(image64)

        with open(f"/tmp/{filename}.jpg","wb") as img:
            img.write(imageBytes)
        
        s3_manager.upload_file_to_bucket(bucket, f"/tmp/{filename}.jpg", filepath)

        url = f"https://drimteam.s3.amazonaws.com/{filepath}"
        
        data = {
            "remote_path": filepath,
            "url": url
        }

        return data
    except:
        data = {
                "url": None
                }
        return data

def lambda_handler(event, context):

    body = json.loads(event["body"])

    image = body["image"]
    image_name = body["image_name"]

    data = upload_image(image, image_name)

    return {
        "statusCode": 200,
        "body": data,
        "isBase64Encoded": False
    }
