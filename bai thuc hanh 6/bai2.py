class Hinhchunhat(object):
    def __init__(self, dai, rong):
        self.dai = dai
        self.rong = rong
    def dien_tich(self):
        return self.dai * self.rong
hcn = Hinhchunhat(5, 3)
print(hcn.dien_tich())
