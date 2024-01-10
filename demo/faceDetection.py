import naoqi

myBroker = naoqi.ALBroker("myBroker", "0.0.0.0", 0, "10.1.32.201", 9559)
memoryProxy = naoqi.ALProxy("ALMemory", "10.1.32.201", 9559)
memoryProxy.subscribeToEvent("FaceDetected", "Test_Face", "is_face_detected")



def recognise():
    if len(memoryProxy.getData("FaceDetected")) != 0:
        return True
    return False