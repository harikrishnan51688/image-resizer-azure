from flask import Flask, request, jsonify, send_file, send_from_directory
from flask import render_template
from azure.storage.blob import BlobServiceClient
from PIL import Image
import io
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Azure Storage configuration
AZURE_CONNECTION_STRING = os.getenv("AZURE_CONNECTION_STRING")
UPLOAD_CONTAINER = "upload"
DOWNLOAD_CONTAINER = "download"
blob_service_client = BlobServiceClient.from_connection_string(AZURE_CONNECTION_STRING)


@app.route('/resize', methods=['POST'])
def resize_image():
    file = request.files['image']
    width = int(request.form['width'])
    height = int(request.form['height'])

    # Upload original image
    upload_blob = blob_service_client.get_blob_client(container=UPLOAD_CONTAINER, blob=file.filename)
    upload_blob.upload_blob(file, overwrite=True)

    # Resize the image
    file.seek(0)
    image = Image.open(file)
    resized_image = image.resize((width, height))

    # Save resized image to Azure
    output = io.BytesIO()
    resized_image.save(output, format=image.format)
    output.seek(0)
    download_blob = blob_service_client.get_blob_client(container=DOWNLOAD_CONTAINER, blob=file.filename)
    download_blob.upload_blob(output, overwrite=True)

    # Generate download URL
    download_url = download_blob.url

    return jsonify({"message": "Image resized successfully", "download_url": download_url})

    
@app.route('/')
def serve_frontend():
    return send_from_directory('templates', 'index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
