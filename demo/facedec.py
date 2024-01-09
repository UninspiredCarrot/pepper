import naoqi
import random
import time
import move

# Initialize NAOqi SDK and proxies
myBroker = naoqi.ALBroker("myBroker", "0.0.0.0", 0, "10.1.32.201", 9559)
alm = naoqi.ALProxy("ALMotion")
alas = naoqi.ALProxy("ALAnimatedSpeech")
tts = naoqi.ALProxy("ALTextToSpeech")
auto = naoqi.ALProxy("ALAutonomousLife")

memoryProxy = naoqi.ALProxy("ALMemory", "10.1.32.201", 9559)
memoryProxy.subscribeToEvent("FaceDetected", "Test_Face", "is_face_detected")




def wave():
    # Raising right arm for a fist bump
    alm.setAngles("HeadPitch", -0.2, 0.3)
    alm.setAngles("RHand", 0.0, 0.3)
    alm.setAngles("RShoulderPitch", 0.0122, 0.5)
    alm.setAngles("RShoulderRoll", -0.626, 0.5)
    alm.setAngles("RElbowRoll", 1.45, 0.3)
    alm.setAngles("RElbowYaw", 1.71, 0.3)
    alm.setAngles("RWristYaw", -0.9, 0.9)
    time.sleep(0.7)

    # Speak a random greeting
    greetings = [
        " Hi, I am Pepper ",
        " How's your day? ",
        " Hello",
        " Good day",
        " What's up"
    ]
    random_speech = random.choice(greetings)
    alas.say(random_speech)
    move.reset()

def recognise():
    if len(memoryProxy.getData("FaceDetected",)) != 0:
        return True
    return False

def main():
    n = 0
    while True:
        if len(memoryProxy.getData("FaceDetected",)) != 0:
            wave()
            time.sleep(5)
        else:
            n+=1
            time.sleep(1)
        if n >= 5:
            move.execute(move.read("hd"))
                
               

if __name__ == "__main__":
    main()
