from tensorflow.keras.applications.inception_v3 import InceptionV3, preprocess_input
from tensorflow.keras.preprocessing import image
import numpy as np

# Load pre-trained InceptionV3 model trained on ImageNet
model = InceptionV3(weights='imagenet')
def preprocess_image(img_path):
    img = image.load_img(img_path, target_size=(299, 299))
    img = image.img_to_array(img)
    img = np.expand_dims(img, axis=0)
    img = preprocess_input(img)
    return img

# Load and preprocess an example image
img_path = 'example_image.jpg'  # Replace with your image file path
img = preprocess_image(img_path)
def extract_features(img):
    features = model.predict(img)
    return features

# Extract features from the image
img_features = extract_features(img)
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.models import load_model

# Load the tokenizer and captioning model
tokenizer = Tokenizer()
tokenizer = load_model('tokenizer_model.h5')  # Replace with your tokenizer model path
captioning_model = load_model('captioning_model.h5')  # Replace with your captioning model path
def generate_caption(img_features):
    # Generate an initial caption
    initial_caption = 'startseq'
    for i in range(max_length):
        sequence = tokenizer.texts_to_sequences([initial_caption])[0]
        sequence = pad_sequences([sequence], maxlen=max_length)
        predicted = captioning_model.predict([img_features, sequence], verbose=0)
        predicted_word = reverse_word_map[np.argmax(predicted)]
        initial_caption += ' ' + predicted_word
        if predicted_word == 'endseq':
            break
    return initial_caption

# Generate caption for the image
max_length = 35  # Maximum length of the caption
reverse_word_map = dict(map(reversed, tokenizer.word_index.items()))
caption = generate_caption(img_features)
print('Generated Caption:', caption)

