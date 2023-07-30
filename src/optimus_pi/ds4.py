from pyPS4Controller.controller import Controller

class PS4Controller(Controller):

    def __init__(self, **kwargs):
        Controller.__init__(self, **kwargs)

if __name__ == "__main__":
    controller = PS4Controller(interface="/dev/input/js0", connecting_using_ds4drv=False)
    controller.listen()
