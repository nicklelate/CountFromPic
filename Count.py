import cvlib as cv
import datetime
import time
import pyrebase
from firebase import firebase
import cv2
from cv2 import *
# python -m pip install

url = 'https://cmudigitaltwin-default-rtdb.asia-southeast1.firebasedatabase.app/'
messenger = firebase.FirebaseApplication(url)

config = {
      "apiKey": "AIzaSyB0jEE81f2tyALy-yu-UIPVhBtZmmVoNM0",
      "authDomain": "cmudigitaltwin.firebaseapp.com",
      "databaseURL": "https://cmudigitaltwin-default-rtdb.asia-southeast1.firebasedatabase.app",
      "projectId": "cmudigitaltwin",
      "storageBucket": "cmudigitaltwin.appspot.com",
      "messagingSenderId": "195899095238",
      "appId": "1:195899095238:web:66d615df634083ca78bfc7",
      "measurementId": "G-C09PYE5SVR",
      "serviceAccount":{
        "type": "service_account",
        "project_id": "cmudigitaltwin",
        "private_key_id": "f72855b76b9914726477110264f7a82cd7035c60",
        "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCe5UA9O14Ow4k6\ndVS345I0QJkmi5EZnouAqljl54qDOEZBKXMfnuUdB1F7pniH5+ODK1wz2cWAT1Vk\nFaCpgWDAuXe67QCZeEtAuPK32mK0S4srmWK+2TVYxrqlwhyY5HigiFSG70yG4DrC\nqgB7AoakoP8GTO2JlfGq/srSvh77Jw4el8ARExURQPJ6Q+EK4QJlO4AALWk82rtJ\n4jTGbVPP8pOJJwvUb02tqJmoePONb8GYQxNEcVq4SisqwA4h4Tvw5LodVitBBLuo\nq9BJ1g3Yix+X7rN9bcYrSlcvADsKqS1Y9RAYOmLt5P5Syu62p3lg6873jC2iNzwB\n+baxSgTxAgMBAAECggEAHPx+TQ1M+c2C9bacx1UNAVo9dhIk3LMXCNhKklo8Yva7\nnjyFA2I1sqd4nmF+gHB1iSK6Vb0m8eLHFZR6dCGleFL9PAzrPJP8ymhS4uZEdlaH\no2L+aAlw2WqbdwyjseKP/N0R6nGyGLLEFWn033vU+yhhjZEwDhbb+NE1R9+mADPU\nhVZ0lLtemnL2tEqoItrd8wP458MGR56HMt1p1Qlpk7BWwU3AqFJJUZNrN75e/np5\nCootOrkMXIdEMVCjCo6daFmliOlrScnnYcBcfIvyx1Fm/JjmCcxJPlglvmRHGNTp\nmh4+a3r8wcpnc8Ew5glm8O3iCN9DnLjlWoVmr9d9XwKBgQDVJcFHxHxG8j7wJIZE\nBMLZU5aND6lxGC9591E02fDP33u4nJcjaGDhN9lBFGcrRhm0YNjTMr9q4QDWzMJj\nR0Z/rCsyM6RSo9eWL8ayyczhaRtaKC8n74XKjHnkR/PP/v7axSbY++9AHJf/PH/E\nEeash+scZI9vaHyOn2iATGPZTwKBgQC+10Na/ei2YNcCUZmsc5ciyWu8X/Woy5Xb\nZnIbjBo3wCiwbWyAtTmRPVFsD32XI7+2Xbp9HnY5xE0i5Cqw1apbVW+rjZl5YxcW\nbS1QW3xVxFLTTSBT63kQY0+CmOQ8xTIfosQAJmGB2iFMbS72dLJN4mraG3n0UziM\n6hU/6ugtvwKBgQDIIODvX59Ihd9uXvzqFIZWw9MRs2jm1UyOehZ3R0KCC1YBKpYG\nGtUL4gJMxrlvuiwcXup2sqlj0suU40CJMr0Q1zjfs/lP1qJvU4B/ElcaNjQGXMCa\nAJ1gZrF0E9LqsoPcKUymYzZqve5BKi7Ui/JIgH3SdODwO+znhOj7vb3qpQKBgHDs\n+BJTxOyGiTP6DTEahQg0n+er8LWdImPdTxA16x2qO2mKlnXixtnGqvOChxJ0OPE0\nrTF0YQj1u5813H0fMdsxxw6Aj5xgojzHBdVTDVPDBC+8p7CA2fZ0jYv95LCBD5Pg\nwJJGI9Suup16zhtQGmIz5H6DW7rTs9bOfRyBaDoJAoGAUgnkKu/iZ24YHC3nIF53\n39a8KuS1tUdQccMy1akESWMIojXS0eoAN2ysA0w8u54OgwZUtXiRdZ24jBBGeoCf\nEt81A1OW1+IQeA3PBSv+4cbMu0VNavzOka/tyoKVX3Ih+AqdHEjsUvFR7knTEWrp\nf0Z5E5yzRaFHsI2IrrLXufg=\n-----END PRIVATE KEY-----\n",
        "client_email": "firebase-adminsdk-1xuaj@cmudigitaltwin.iam.gserviceaccount.com",
        "client_id": "113916274742424122908",
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-1xuaj%40cmudigitaltwin.iam.gserviceaccount.com",
        "universe_domain": "googleapis.com"
        }
}

firebase = pyrebase.initialize_app(config)
storage = firebase.storage()
storage.child("818_room.png").download("818_room.png","818_room.png")

b = True
while b:
    x = datetime.datetime.now()
    if True:
        img = cv2.imread("818_room.png")
        box,label,count = cv.detect_common_objects(img)
        count = 0
        for i in label:
            if i == 'person':
                count += 1
        print("there are " + str(count) + " people.")
        engineer = {'Timestamp':x,'People':count}
        result = messenger.put('/818 room','CCTV',engineer)
        print("Engineer 1", result)
    else:
        print("No image detected. Please! try again")

    time.sleep(300)

