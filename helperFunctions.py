import pyrebase
from config import firebaseConfig
from face_lib import face_lib
import cv2

FL = face_lib()

def fireBaseConfigSetup():
    firebase = pyrebase.initialize_app(firebaseConfig)
    auth = firebase.auth()
    return firebase, auth

def getFace(x, y, w, h, img):
    roi = img[y:y + h, x:x + w]
    no_of_faces, faces_coors = FL.faces_locations(roi)
    # print(faces_coors,no_of_faces)
    return faces_coors

def getFileNames():
    classFile = 'additional Files//coco.names'
    with open(classFile, 'rt') as f:
        classNames = f.read().rstrip('\n').split('\n')
    return classNames

def nnSetup():
    configPath = 'additional Files//ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
    weightsPath = 'additional Files//frozen_inference_graph.pb'

    net = cv2.dnn_DetectionModel(weightsPath, configPath)

    return net