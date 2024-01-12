import faceDetection
import gestures
import listen
import textProcess
import navigation
import move

path = "/home/nao/demo/maps/map.explo"

def main():
    move.execute(move.read('reset'))
    headShiftCount = 0
    while True:
        if faceDetection.recognise():
            gestures.wave("Hi, can I help you?")
            question = listen.listenToText()
            # question = raw_input('listening: ')
            while True:
                if textProcess.needHelp(question):
                    # print("listening")
                    # question = listen.listenToText()
                    # print("stoppped listening")
                    # question = raw_input('listening1: ')
                    item = textProcess.isWhere(question)
                    if item:
                        # print(item)
                        navigation.navigate_to_location(path, item)
                        # move.execute(move.read('mvsssss'))
                    else:
                        textProcess.GPTreply(question)

                    listen.speak('Do you need any more help?')
                    question = listen.listenToText()
                    # question = raw_input('listening: ')
                else:
                    navigation.navigate_to_location(path, 'home')
                    gestures.wave('Ok I hope I was able to help you, Bye!')
                    break
                




        else:
            gestures.scan(headShiftCount)
            headShiftCount += 1

        





if __name__ == "__main__":
    main()