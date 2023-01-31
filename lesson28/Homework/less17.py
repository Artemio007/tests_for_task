
history = []


class History:
    def __init__(self, element: dict):
        self.element = element
        self.all_in_dict = {}
        history.append(*self.element.keys())

    def set_value(self, key: str, val: int):
        self.all_in_dict.update({key: val})
        history.append(key)
        if len(history) >= 10:
            history.pop(0)

    @staticmethod
    def get_value():
        return history

