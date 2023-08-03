class Man:
    """
    class Man

    """

    def __init__(self, name):
        self.name = name

    def callname(self):
        return f"Hello {self.name}"


akash = Man("Akash")

abarna = Man("Abarna")

print(abarna.callname())
