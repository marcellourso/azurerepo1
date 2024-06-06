import os
from azure.ai.vision.imageanalysis import ImageAnalysisClient
from azure.ai.vision.imageanalysis.models import VisualFeatures
from azure.core.credentials import AzureKeyCredential

# Set the values of your computer vision endpoint and computer vision key
# as environment variables:
try:
    # endpoint = os.environ["VISION_ENDPOINT"]
    # key = os.environ["VISION_KEY"]
    endpoint = "https://cvisione1.cognitiveservices.azure.com/"
    key = "5f1171a73d6949e0a3bade140ff89bef"
    
except KeyError:
    print("Missing environment variable 'VISION_ENDPOINT' or 'VISION_KEY'")
    print("Set them before running this sample.")
    exit()

try:
    # Create an Image Analysis client for synchronous operations
    client = ImageAnalysisClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(key)
)
    
except KeyError:
    print("no valid key")
    exit()

try:
    # Get a caption for the image. This will be a synchronously (blocking) call.
    result = client.analyze_from_url(
    image_url="https://aka.ms/azsdk/image-analysis/sample.jpg",
    visual_features=[VisualFeatures.CAPTION],
    gender_neutral_caption=True,  # Optional (default is False)
    )
except Exception as e:
    print(e)

try:
    # Print caption results to the console
    print("Image analysis results:")
    print(" Caption:")
    if result.caption is not None:
        print(f"   '{result.caption.text}', Confidence {result.caption.confidence:.4f}")

except:
    print("no caption")
    exit()