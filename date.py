class Task_5:
    def __init__(self, dd, mm, yyyy):
        self.dd = dd
        self.mm = mm
        self.yyyy = yyyy

    def IsExistDate(self):
        if self.dd <= 30 and self.mm == 1 or self.mm == 4 or self.mm == 6 or self.mm == 9 or self.mm == 11:
            return True
        elif self.dd <= 29 and self.mm == 2 and self.yyyy % 4 == 0:
            return True
        elif self.dd <= 31 and self.mm == 3 or self.mm == 5 or self.mm == 7 or self.mm == 8 or self.mm == 10:
            return True
        elif self.dd <= 28 and self.mm == 2 and self.yyyy % 4 != 0:
            return True
        else:
            return False
