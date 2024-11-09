from transformers import pipeline
from PIL import Image

# Initialize the image classification pipeline
# classifier = pipeline("image-classification")
# Alternatively you can define what model should the pipeline use, sometimes it requires that you login with your token
classifier = pipeline("image-classification", model="ind4rk/mushrooms", token="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")

#print(classifier.model)

def classify_image(image):
    results = classifier(image)
    # Get the top prediction
    top_result = results[0]
    label = top_result['label']
    score = top_result['score']
    return f"Label: {label}, Confidence: {score:.2f}"

image = Image.open("/mnt/boletus-rex-veris-300x300.png")

print("Predicted class:", classify_image(image))