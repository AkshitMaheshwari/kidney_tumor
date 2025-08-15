import streamlit as st
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array

from PIL import Image
import io


model = load_model('kidney_classification.h5')

class_names = ['Cyst', 'Normal', 'Stone', 'Tumor']  


st.title("Kidney Ultrasound Classification")
st.write("Upload a kidney ultrasound image to classify it as one of the following categories:")
st.write(", ".join(class_names))


uploaded_file = st.file_uploader("Choose a kidney image", type=['jpg', 'jpeg', 'png'])

if uploaded_file is not None:

    img = Image.open(uploaded_file)
    if img.mode != "RGB":
        img = img.convert("RGB")
    st.image(img, caption='Uploaded Image', use_column_width=True)

 
    img = img.resize((224, 224))
    img_array = img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = img_array / 255.0

 
    predictions = model.predict(img_array)
    predicted_class = class_names[np.argmax(predictions)]

 
    st.markdown(f"### 🧠 Prediction: `{predicted_class}`")
    st.bar_chart(predictions[0])
