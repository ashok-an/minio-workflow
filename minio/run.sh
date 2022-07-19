docker run \
  -d \
  -p 9000:9000 \
  -p 9001:9001 \
  --name minio \
  -v ${PWD}/data:/data \
  -e "MINIO_ROOT_USER=accessKey" \
  -e "MINIO_ROOT_PASSWORD=secretKey" \
  quay.io/minio/minio server /data --console-address ":9001"

