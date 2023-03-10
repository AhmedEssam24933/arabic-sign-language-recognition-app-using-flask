import numpy as np
from flask import request
import os
import cv2
import tensorflow as tf
from tensorflow import keras
from gtts import gTTS
from playsound import playsound

model = keras.models.load_model(r'Models\best_sign_model.h5')

def img_to_text(path):
    if request.method == 'POST':
        img = cv2.imread(path ,cv2.IMREAD_GRAYSCALE)  
        img = cv2.resize(img, (200, 200)) 
        img = tf.expand_dims(img,0)
        predict_prob = model.predict([img])
        predict_classes = np.argmax(predict_prob,axis=1)
        labels =['أخ','منتصف','هلال','صديق','يتزوج']
        text = labels[predict_classes[0]]
        ##tts = gTTS(text, lang='ar')
        ##if os.path.exists(r"templates\voice.mp3"):
            ##os.remove(r"templates\voice.mp3")
        ##tts.save(r"templates\voice.mp3")
        ##speech = playsound(r"speech\voice.mp3")
        return text
    return ''


def resized_image(path):
    if request.method == 'POST':
        img = cv2.imread(path)
        h, w = img.shape[:2]  
        r = 600/h
        h = int(h*r)
        w = int(w*r)
        image = cv2.resize(img, (w,h))
        cv2.imwrite(r'static\uploads\2.jpg', image) 
        return 
    return ''

