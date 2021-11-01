import transformers
from transformers import ViTFeatureExtractor
from data_loader import Load_Data

def ViT_Feature_Extractor(images):

    feature_extractor = ViTFeatureExtractor.from_pretrained('google/vit-base-patch16-224-in21k')
    image_features = []
    for image in images:
        features = feature_extractor(image)
        image_features.append(features)
    return image_features

image_directory = '/Users/aysanaghazadeh/University/Pitt/Research/Diagram_Summarization/ai2d-rst-v1-1/images'
images, filenames, summary = Load_Data(image_directory)
ViT_Feature_Extractor(images)
