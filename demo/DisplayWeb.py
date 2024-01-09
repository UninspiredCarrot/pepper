import argparse
import sys
import qi
import time

def display():
    
    tabletService = session.service("ALTabletService")

    tabletService.enableWifi()

    tabletService.showWebview("https://xxlaram.github.io/pepper_last_ditch/")

    time.sleep(30)

    tabletService.hideWebview()


def main(session):
    display()


if __name__ == "__main__":
    # parser = argparse.ArgumentParser()
    # parser.add_argument("--ip", type=str, default="10.1.32.201",
    #                     help="Robot IP address. On robot or Local Naoqi: use '10.1.32.201")
    # parser.add_argument("--port", type=int, default=9559,
    #                     help="Naoqi port number")

    # args = parser.parse_args()
    session = qi.Session()
    session.connect("tcp://10.1.32.201:9559")
    main(session)
