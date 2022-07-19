##### Commands to enable notification
# add an alias
mc config host add myminio http://localhost:9000 accessKey secretKey --api S3v4

# add notification channel
mc admin config set myminio notify_webhook endpoint="http://173.39.52.48:8082"

# reset
mc admin service restart myminio

# enable notification
mc event add myminio/hello-bucket arn:minio:sqs::_:webhook --event put

# list event notification config
mc event list myminio/hello-bucket
