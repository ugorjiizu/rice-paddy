from msilib.schema import Condition
from fastapi import FastAPI, File, UploadFile, Depends
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import numpy as np
from io import BytesIO
import cv2
from PIL import Image
import tensorflow as tf
import os
import h5py

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


MODEL = tf.keras.models.load_model('basemodel.h5')
# MODEL.summary()


CLASS_NAMES = ['Bacterial leaf blight',
'Bacterial leaf streak',
'Bacterial panicle blight',
'Blast',
'Brown spot',
'Dead heart',
'Downy mildew',
'Hispa',
'Normal',
'Tungro']

@app.get('/ping')
async def ping():
    return 'First Step'

def read_file_as_image(data) -> np.ndarray:
    image = np.array(Image.open(BytesIO(data)))
    return image


@app.post("/predict")
async def predict(
    file: UploadFile = File(...)
):
    if not file:
        print( {"message": "No upload file sent"} )
    else:
        print( {"filename": file.filename} )
    img = read_file_as_image(await file.read())
    img = cv2.resize(img, (400,400))
    img_batch = np.expand_dims(img, 0)
    prediction = MODEL.predict(img_batch)
    predicted_class = CLASS_NAMES[np.argmax(prediction[0])]
    confidence = np.max(prediction[0])
    confidence = round((confidence*100), 2)
    accuracy = ('{}%'.format(confidence))
    return {
        'class': predicted_class,
        'confidence': accuracy
    }

if __name__ == '__main__':
    uvicorn.run("main:app", host='localhost', port=8000)  