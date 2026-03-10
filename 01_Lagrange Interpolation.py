from Handler import Handle
import numpy as np
import matplotlib.pyplot as plt

class Model:

    def __init__(self,file):
        self.model=file+".csv"
        self.File = Handle(self.model)

    def run(self):

        File = self.File

        r = File.stream()

        x = float(input("Input: "))

        ed = File.search(x)  # Seacrh for existing data
        if ed is not None:
            print(f"Output: {ed[2]}")
            return

        P = 1  # Calculating (x - xi)
        for rows in File.local_stream():
            P *= x - rows[0]

        S = 0
        for rows in r:
            if len(rows) > 3:
                S += rows[2] * P / (x - rows[0]) * rows[3]
                rows[3] /= rows[0] - x
                File.print(rows)

        print(f"Output: {S}")
        data = float(input("True Data: "))
        try:
            print(f"Accuracy: {(1 - abs(data - S) / data) * 100}%")
        except ZeroDivisionError:
            print(f"Accuracy: {100 if S == 0 else 0}%")

        File.print([x, S, data, 1/P])

        File.close()

    def f(self,x):
        File = self.File
        ed = File.search(x)  # Search for existing data
        if ed is not None:
            return ed[2]

        P = 1  # Calculating (x - xi)
        for rows in File.local_stream():
            P *= x - rows[0]

        S = 0
        for rows in File.local_stream():
            if len(rows)>3: S += rows[2] * P / (x - rows[0]) * rows[3]
        return S

    def plot(self,a,b):
        x=np.linspace(a,b,1000)
        y=np.array(list(map(self.f,x)))
        plt.plot(x,y)
        data = np.transpose(np.array(Handle(self.model).read()))
        plt.scatter(data[0],data[2])
        plt.xticks(np.linspace(np.min(x),np.max(x),5))
        plt.yticks(np.linspace(np.min(y), np.max(y), 5))
        plt.grid()
        plt.show()

    def add(self,x,y):
        File = self.File

        r = File.stream()

        ed = File.search(x)  # Seacrh for existing data
        if ed is not None:
            return

        P = 1  # Calculating (x - xi)
        for rows in File.local_stream():
            P *= x - rows[0]

        S = 0
        for rows in r:
            if len(rows) > 3:
                S += rows[2] * P / (x - rows[0]) * rows[3]
                rows[3] /= rows[0] - x
                File.print(rows)

        File.print([x, S, y, 1/P])

        File.close()

    def feed(self,data):
        for i in Handle(data+".csv").local_stream():
            self.add(*i)


m=Model("Example/curve")
m.feed("Example/sinrad")
m.plot(10,40)
#m.run()
m.File.success=True
