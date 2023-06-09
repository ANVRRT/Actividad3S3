import json
import base64
from s3_manager import S3Manager

# Create a function that sends an image in base64 via POST request:

def send_image(image_path, image_name):
    import requests
    import base64

    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode('utf-8')

    payload = {
        "image": encoded_string,
        "image_name": image_name
    }

    url = "https://dv4d6d7smmnxnqqgxfncmdmk4m0gpsxz.lambda-url.us-east-1.on.aws/"
    response = requests.post(url, json=payload)

    with open(f"{image_name}.json", "w") as outfile:
        outfile.write(response.text)

def download_image(remote_path, local_path):

    s3_manager = S3Manager()

    s3_manager.download_file_from_bucket("drimteam", remote_path, local_path)

    

if __name__ == "__main__":
    image_name = "imagetest"
    image_path = "./image.jpg"
    send_image(image_path, image_name)

    # Reads json with imagename
    with open(f"{image_name}.json", "r") as json_file:
        data = json.load(json_file)

    download_image(data["remote_path"], f"./downloaded_image.jpg")

    # Pull image from S3 bucket:
    # import boto3
