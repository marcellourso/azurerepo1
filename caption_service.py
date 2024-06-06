import os
from flask import Flask, request, jsonify
from azure.ai.vision.imageanalysis import ImageAnalysisClient
from azure.ai.vision.imageanalysis.models import VisualFeatures
from azure.core.credentials import AzureKeyCredential
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Set the values of your computer vision endpoint and computer vision key
endpoint = "https://cvisione1.cognitiveservices.azure.com/"
key = "5f1171a73d6949e0a3bade140ff89bef"

# Create an Image Analysis client for synchronous operations
client = ImageAnalysisClient(endpoint=endpoint, credential=AzureKeyCredential(key))

@app.route('/analyze', methods=['POST'])
def analyze_image():
    data = request.get_json()
    image_url = data.get('image_url')
    
    if not image_url:
        return jsonify({"error": "No image URL provided"}), 400

    try:
        # Get a caption for the image. This will be a synchronously (blocking) call.
        result = client.analyze_from_url(
            image_url=image_url,
            visual_features=[VisualFeatures.CAPTION],
            gender_neutral_caption=True,  # Optional (default is False)
        )
        
        # Check and return the result
        if result.caption is not None:
            return jsonify({
                "caption": result.caption.text,
                "confidence": result.caption.confidence
            }), 200
        else:
            return jsonify({"error": "No caption found"}), 400

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
