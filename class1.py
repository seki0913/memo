class base():
    def a(self):
        print("base.a")
        self.b()
    def b(self):
        print("base.b")

class der(base):
    def b(self):
        print("D")

b = base()
d = der()
#b.a()

d.a()