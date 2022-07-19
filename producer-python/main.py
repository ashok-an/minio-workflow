#!/usr/bin/env python3

import os
import random
import tempfile

import minio_helper

def create_file(sizeMB=1):
  with tempfile.NamedTemporaryFile(prefix='producer-python', suffix='.dat', dir='/tmp') as tf:
    tf.seek(sizeMB * 1024 * 1024 - 1)
    tf.write(b'0')
    tf.seek(0)
    print("+ {} ({}MB)".format(tf.name, sizeMB))
    minio_helper.upload_file(sourcePath=tf.name, bucketName='hello-bucket', fileName=os.path.basename(tf.name))
# end


if __name__ == '__main__':
  minio_helper._create_bucket(bucketName='hello-bucket')
  for i in range(30):
    create_file(sizeMB=random.randrange(1, 5))
