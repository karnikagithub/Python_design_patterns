class SmartPhone:
    max_vinput_voltage = 5

    def outcome(cls,input_voltage):
        if input_voltage > cls.max_vinput_voltage:
            print("It's Burning")
        else:
            print("It's Charging")

    def charge(self, input_voltage):
        self.outcome(input_voltage)


class Socket:
    output_voltage = None

class EUSocket:
    output_voltage=230

class EUAdapter:
    input_voltage = EUSocket.output_voltage
    output_voltage = 5



sm=SmartPhone()
sm.charge(EUSocket.output_voltage)
## output: It's burning
sm.charge(EUAdapter.output_voltage)
## output: It's Charging