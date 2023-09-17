from pyPS4Controller.controller import Controller
from gpiozero import Robot

class PS4Controller(Controller):

    def __init__(self, **kwargs):
        Controller.__init__(self, **kwargs)
        self.rob = Robot(left=(7,8), right=(9,10))

    def on_L3_up(self, value):
        print(-value/2**16)
        self.rob.left(-value/2**16)
        #self.rob.forward()

    def on_L3_y_at_rest(self):
        self.rob.stop()

    def on_R3_up(self, value):
        print(-value/2**16)
        self.rob.right(-value/2**16)
        #self.rob.forward()

    def on_R3_y_at_rest(self):
        self.rob.stop()

if __name__ == "__main__":
    controller = PS4Controller(interface="/dev/input/js0", connecting_using_ds4drv=False)
    controller.listen()
