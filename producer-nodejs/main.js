const fs = require('fs');
const path = require('path');

var Minio = require('minio')

var minioClient = new Minio.Client({
    endPoint: 'localhost',
    port: 9000,
    useSSL: false,
    accessKey: 'accessKey',
    secretKey: 'secretKey'
});
const bucketName = 'hello-bucket';
const region = 'us-east-1';
const metaData = {
        'Content-Type': 'application/octet-stream',
        'X-Amz-Meta-Testing': 1234,
        'example': 5678
}

minioClient.bucketExists(bucketName, function(err, exists) {
  if (err) {
    return console.log(err)
  }
  if (exists) {
      console.log(`Bucket:${bucketName} already exists.`)
  }else{
    minioClient.makeBucket(bucketName, region, function(err) {
      if (err)
        console.log(err);
      else
        console.log(`Bucket:${bucketName} created successfully in "${region}".`);
    });
  }
})

const uploadFile = (sourcePath, destFile) => {
    return new Promise((resolve, reject) => {
      minioClient.fPutObject(bucketName, destFile, sourcePath, metaData, function(err, etag) {
      if (err) reject(err);
      return resolve(sourcePath);
    })
  })
}

const createEmptyFileOfSize = (fileName, sizeMB) => {
    return new Promise((resolve, reject) => {
        fh = fs.openSync(fileName, 'w');
        size = 1024*1024*sizeMB;
        fs.writeSync(fh, 'ok', Math.max(0, size - 2));
        fs.closeSync(fh);
        resolve(true);

        console.log(`+ ${fileName} (${sizeMB}MB)`);
    });
};

for (let i=0; i<20; i++){
  var filePath = `/tmp/nodejs-producer-${i}.dat` ;
  var mb = Math.floor(Math.random() * 4) + 1;
  createEmptyFileOfSize(filePath, mb);
  uploadFile(filePath, path.basename(filePath))
    .then(filePath => { fs.unlinkSync(filePath); })
    .catch(error => { console.log(error); })
}

