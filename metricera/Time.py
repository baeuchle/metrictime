class Time:
    def __init__(self, *args):
        if len(args) == 0:
            self.tycs_ = 0
            self.whyle_ = 0
            self.tyc_ = 0
            return
        if len(args) == 1:
            self.tycs_ = args[0]
            self.whyle_ = int(self.tycs_ / 1000)
            self.tyc_ = self.tycs_ % 1000
            return
        if len(args) == 2:
            self.whyle_ = args[0]
            self.tyc_ = args[1]
            self.tycs_ = self.whyle_ * 1000 + self.tyc_
            return
        raise ValueError("Too many arguments")

    def set_tycs_(self):
        self.tycs_ = self.whyle_ * 1000 + self.tyc_

    def get_tyc(self):
        return self.tyc_
    def set_tyc(self, value):
        if 0 <= value < 1000:
            self.tyc_ = value
            self.set_tycs_()
            return
        raise ValueError("Tic must be in [0,1000), got {}".format(value))
    tyc = property(get_tyc, set_tyc)

    def get_whyle(self):
        return self.whyle_
    def set_whyle(self, value):
        if 0 <= value < 100:
            self.whyle_ = value
            self.set_tycs_()
            return
        raise ValueError("Whyle must be in [0,100), got {}".format(value))
    whyle = property(get_whyle, set_whyle)

    tycs = property(lambda self: self.tycs_)

    def next_whyle(self):
        if self.tyc == 0:
            return Time(self)
        nw = Time(self.whyle + 1, 0)
        return nw

    def __sub__(a, b):
        tycdiff = (a.tycs - b.tycs) % 100000
        return Time(tycdiff)

    def __str__(self):
        return "{:02d}:{:03d}".format(self.whyle, self.tyc)

    def seconds(self):
        return self.tycs * 0.864
