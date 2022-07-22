class Content:
    def __init__(self, text, from_char, to_char):
        self.text = text
        self.from_char = from_char
        self.to_char = to_char


class Execute(Content):

    def execute(self):
        self.text = self.text.replace(self.from_char, self.to_char)


class Undo(Content):

    def undo(self):
        self.text = self.text.replace(self.to_char, self.from_char)


class WorkWithChar(Execute, Undo):
    pass


class History:
    def __init__(self):
        self._command = []

    def execute(self, command):
        self._command.append(command)
        command.execute()

    def undo(self):
        if len(self._command) > 0:
            self._command.pop().undo()


c = WorkWithChar('ala bala', 'a', 'A')
h = History()
h.execute(c)
# h.undo()
print(c.text)
