import naoqi
import time
import move

# Initialize NAOqi SDK and proxies
myBroker = naoqi.ALBroker("myBroker", "0.0.0.0", 0, "10.1.32.201", 9559)
alm = naoqi.ALProxy("ALMotion")

def wave(text):
    # Raising right arm for a fist bump
    alm.setAngles("HeadPitch", -0.2, 0.3)
    alm.setAngles("RHand", 0.0, 0.3)
    alm.setAngles("RShoulderPitch", 0.0122, 0.5)
    alm.setAngles("RShoulderRoll", -0.626, 0.5)
    alm.setAngles("RElbowRoll", 1.45, 0.3)
    alm.setAngles("RElbowYaw", 1.71, 0.3)
    alm.setAngles("RWristYaw", -0.9, 0.9)
    time.sleep(0.7)
    if text:
        naoqi.ALProxy("ALAnimatedSpeech").say(text)
    move.reset()

def scan(headShiftCount):
    if (headShiftCount//10)%2 == 0:
            direction = 'd'
    else:
        direction = 'a'
    # move.execute(move.read("hd"+direction))
    headShiftCount += 1