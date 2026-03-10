import csv
from random import randint as rnd
import atexit
import os
import tempfile
import shutil

class Handle:

    def __init__(self,file):

        self.success=False
        self.file=file
        try:
            with open(file, 'r'):
                pass
        except FileNotFoundError:
            with open(file, 'w',newline='') as o:
                csv.writer(o).writerow(["input", "output", "data","process"])

        temp=tempfile.NamedTemporaryFile(mode='w+t', suffix='.csv', newline='', delete=False)
        with open(file, 'r', newline='') as src_file:
            shutil.copyfileobj(src_file, temp)
        temp.flush()
        temp.seek(0)
        temp.close()
        self.temp=temp



    def stream(self,print=True):
        self.i = open(self.file, 'r')
        self.r = csv.reader(self.i)
        header = next(self.r)
        self.out = str(rnd(1000000, 9999999)) + ".csv"
        self.o = open(self.out, 'w', newline='')
        self.w = csv.writer(self.o)
        self.w.writerow(header)

        atexit.register(self.delete)
        while True:
            try:
                t = next(self.r)
                self.printed=not print
                data=list(map(float,t))
                yield data
                if not self.printed: self.print(data)
            except StopIteration:
                break

    def local_stream(self):
        with open(self.file,'r') as r:
            next(r)
            for rows in r:
                yield list(map(float,rows.split(',')))

    def print(self,data):
        self.w.writerow(data)
        self.printed=True

    def close(self):
        for rows in self.r:
            self.print(rows)
        self.i.close()
        self.o.close()
        os.remove(self.file)
        os.rename(self.out,self.file)

    def delete(self):
        if not self.success:
            self.i.close()
            shutil.move(self.temp.name, self.file)
        try:
            self.o.close()
            os.remove(self.out)
            os.remove(self.temp.name)
        except FileNotFoundError:
            pass

    def search(self,t,i=0):
        with open(self.file,'r') as f:
            next(f)
            for rows in f:
                r=rows.split(',')
                if float(r[i])==t:
                    return list(map(float,rows.split(',')))
        return None

    def add(self,x):
        with open(self.file,'a',newline='') as f:
            f.write(str(x))

    def read(self):
        rows=[]
        for r in self.local_stream():
            rows.append(r)
        return rows

