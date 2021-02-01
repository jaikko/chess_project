class MenuEntry:

    def __init__(self, option, controller):
        self.option = option
        self.controller = controller

    def __str__(self):
        return str(self.controller)

    def __repr__(self):
        return f"MenuEntry({self.option}, {self.controller})"


class Menu:

    def __init__(self):
        self._entries = {}

    def add(self, key, option, controller):
        self._entries[str(key)] = MenuEntry(option, controller)

    def clear(self):
        self._entries.clear()

    def items(self):
        return self._entries.items()

    def __contains__(self, choice):
        return str(choice in self._entries)

    def __getitem__(self, choice):
        return self._entries[choice]
