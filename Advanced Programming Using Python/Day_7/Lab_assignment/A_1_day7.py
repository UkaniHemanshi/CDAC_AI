class SmartDevice:

    _name = ""
    _status = ""

    def turn_on(self):
        pass
    def turn_off(self):
        pass
    def set_temperature(self, temperature):
        pass
    def device_info(self):
        pass

class SmartThermostat(SmartDevice):
    # def __init__(self):
    #     super().__init__()

    def turn_on(self):
        name_device = input("Please enter device name you want to turn on: ")
        self.name = name_device
        self.status = "ON"
        print(f'Smart thermostat is {self.status}')

    def turn_off(self):
        self.status = "OFF"

    def set_temperature(self, temperature):
        print(f'Temperature set to {temperature} C')

    def device_info(self):
        print(f'Name of Device: {self.name} and Status of Device: {self.status}')


objsub = SmartThermostat()
objsub.turn_on()
objsub.device_info()
objsub.turn_off()
objsub.device_info()




