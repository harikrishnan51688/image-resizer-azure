# Image Resizer Web Application

A Flask-based web application that allows users to upload and resize images using Azure Blob Storage.

## Features

- Upload images through a web interface
- Specify custom width and height for resizing
- Azure Blob Storage integration for image storage
- Containerized application ready for deployment
- Kubernetes deployment support

## Prerequisites

- Python 3.9 or higher
- Azure Storage Account
- Docker (for containerization)
- Kubernetes cluster (for deployment)

## Azure Configuration
The application requires two blob containers:

 - upload - For storing original images
 - download - For storing resized images

## Installation

1. Clone the repository
2. Create a virtual environment and activate it:

```sh
python -m venv env
source env/bin/activate  # For Unix
env\Scripts\activate     # For Windows
```
Install dependencies:
```
pip install -r requirements.txt
```
Create a .env file with your Azure Storage credentials:
```
AZURE_CONNECTION_STRING=your_azure_storage_connection_string
```
Kubernetes Deployment:

1. Push the image to Azure Container Registry:
```
docker build -t imageresizer.azurecr.io/imageresizer:v1 .
docker push imageresizer.azurecr.io/imageresizer:v1
```

2. Deploy to Kubernetes:
Create a Kubernetes cluster in Azure (if you don’t already have one): then
```
kubectl apply -f deployment.yaml
```
