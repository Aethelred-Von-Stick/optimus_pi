from pyPS4Controller.controller import Controller
from gpiozero import Motor

class PS4Controller(Controller):

    def __init__(self, **kwargs):
        Controller.__init__(self, **kwargs)
        self.lmot = Motor(8, 7)
        self.rmot = Motor(9, 10)

    def on_L3_up(self, value):
        print(-value/2**16)
        self.lmot.forward(-value/2**16)

    def on_L3_down(self, value):
        print(-value/2**16)
        self.lmot.backward(value/2**16)

    def on_L3_y_at_rest(self):
        self.lmot.stop()

    def on_R3_up(self, value):
        print(-value/2**16)
        self.rmot.forward(-value/2**16)

    def on_R3_down(self, value):
        print(-value/2**16)
        self.rmot.backward(value/2**16)

    def on_R3_y_at_rest(self):
        self.rmot.stop()

if __name__ == "__main__":
    controller = PS4Controller(interface="/dev/input/js0", connecting_using_ds4drv=False)
    controller.listen()
