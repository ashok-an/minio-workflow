from flask import Flask, request, jsonify
from minio import Minio

client = Minio('127.0.0.1:9000', access_key='accessKey', secret_key='secretKey', secure=False)
app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def main():
    payload = request.get_json()
    a = client.get_object('json-files', payload['Records'][0]['s3']['object']['key'])
    print(a.read())
    return jsonify(payload)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8082, debug=True)
