from minio import Minio
from minio.error import S3Error

client = Minio("localhost:9000", access_key='accessKey', secret_key='secretKey', secure=False)
bucketName = 'hello-bucket'

def _create_bucket(bucketName):
  found = client.bucket_exists(bucketName)
  if not found:
    client.make_bucket(bucketName)
  else:
    print(f"Bucket:{bucketName} already exists")
#end


def upload_file(sourcePath, bucketName, fileName):
  try:
    client.fput_object(bucketName, fileName, sourcePath) 
    print(f"Uploaded: {sourcePath} -> {bucketName}/{fileName}")
  except S3Error as exc:
    print("error occurred.", exc)
#end

if __name__ == '__main__':
  _create_bucket(bucketName)

  upload_file("/tmp/test.txt", "hello-bucket", "fileA.txt")
  upload_file("/tmp/test.txt", "hello-bucket", "fileB.txt")
  upload_file("/tmp/test.txt", "hello-bucket", "fileC.txt")
  upload_file("/tmp/test.txt", "hello-bucket", "fileD.txt")
