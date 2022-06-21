class ElectronicDevive:
    def __init__(self, voltage, height, weight, color) -> None:
        self.voltage = voltage
        self.height = height
        self.weight = weight
        self.color = color 

class Computer(ElectronicDevive):
    def __init__(self, voltage, height, weight, color, memory, disk) -> None:
        super().__init__(voltage, height, weight, color)
        self.memory = memory
        self.disk = disk

class TV(ElectronicDevive):
    def __init__(self, voltage, height, weight, color, has_remote_control) -> None:
        super().__init__(voltage, height, weight, color)
        self.has_remote_control= has_remote_control

class Desktop(Computer):
    def __init__(self, voltage, height, weight, color, memory, disk, has_inmalambric_mouse) -> None:
        super().__init__(voltage, height, weight, color, memory, disk)
        self.brand_name= brand_name

class Laptop(Computer):
    def __init__(self, voltage, height, weight, color, memory, disk, has_speaker) -> None:
        super().__init__(voltage, height, weight, color, memory, disk)
        self.has_speaker = has_speaker