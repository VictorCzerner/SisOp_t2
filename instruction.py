class instruction:
    def __init__(self, type, id, size):
        self.type = type
        self.id = id
        self.size = size

    def __str__(self):
        if self.size is None:
            return f"{self.type}({self.id})"
        return f"{self.type}({self.id}, {self.size})"

    __repr__ = __str__
