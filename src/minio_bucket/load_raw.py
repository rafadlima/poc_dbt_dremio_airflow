from minio import Minio
from dotenv import load_dotenv
import os


load_dotenv()


LOCAL_FILE_PATH = os.environ.get('LOCAL_FILE_PATH')
ACCESS_KEY = os.environ.get('ACCESS_KEY')
SECRET_KEY = os.environ.get('SECRET_KEY')
MINIO_API_HOST = "http://localhost:9000"
MINIO_CLIENT = Minio(endpoint="localhost:9000", access_key=ACCESS_KEY, secret_key=SECRET_KEY, secure=False)


def main() -> None:
    found = MINIO_CLIENT.bucket_exists(bucket_name="raw")

    if not found:
        MINIO_CLIENT.make_bucket(bucket_name="raw")
    else:
        print("Bucket already exists")

    MINIO_CLIENT.fput_object(bucket_name="raw", object_name="<pic.jpg>", file_path=LOCAL_FILE_PATH,)
    print("It is successfully uploaded to bucket")