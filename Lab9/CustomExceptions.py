class InvalidHypotenuse(Exception):
    def __init__(self, value):
        self.value = value


class LengthNotDefined(Exception):
    def __init__(self, value):
        self.value = value