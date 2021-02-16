class Value:

    @staticmethod
    def _prepare_value(commission, value):
        return value - (commission * value)

    def __set__(self, obj, value):
        self._amount = self._prepare_value(obj.commission, value)

    def __get__(self, obj, obj_type):
        return self._amount


class Account:

    def __init__(self, commission=0):
        self.commission = commission

    amount = Value()
