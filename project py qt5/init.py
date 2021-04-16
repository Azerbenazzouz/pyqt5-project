from PyQt5.uic import loadUi
from PyQt5.QtWidgets import *

#show func
def show(self):
    self.show()
    menu.close()
#close func
def close(self):
    self.close()
    menu.show()
#def pgcd
def calc_pgcd(self):
    if (pgcd.nb1.text() and pgcd.nb2.text())=='':
        QMessageBox.warning(self, "Attention", "enter a number")
    else:
        a=int(pgcd.nb1.text())
        b=int(pgcd.nb2.text())
        while (a!=b):
            if a>b :
                a=a-b
            else:
                b=b-a
        pgcd.res.setText(str(a))
#PPCM
def calc_ppcm(self):
    if (pgcd.nb1.text() and pgcd.nb2.text())=='':
        QMessageBox.warning(self, "Attention", "enter a number")
    else:
        a=int(ppcm.nb1.text())
        b=int(ppcm.nb2.text())
        p=a*b
        while(a!=b):
            if (a<b): b-=a
            else: a-=b
        ppcm.res.setText(str(int(p/a)))
#factorial
def d(n):
    if n == 0:
        return 1
    else:
        j=d(n-1)
        r=n * j
        return r
def ff(self):
    if (pgcd.nb1.text())=='':
        QMessageBox.warning(self, "Attention", "enter a number")
    else:
        n=int(factorial.nb1.text())
        x=d(n)
        factorial.res.setText(str(x))
#decomposition en facteur premier python
def facteurs(self):
    if (pgcd.nb1.text())=='':
        QMessageBox.warning(self, "Attention", "enter a number")
    else:
        a=int(df.nb1.text())
        b=2
        while(b<=a):
            if a%b==0:
                a=a/b
            else:
                b=b+1
        df.res.setText(str(b))
#unnuler
def ann(self,i):
    if i==2 :
        self.res.setText('')
        self.nb1.setText('')
        self.nb2.setText('')
    else:
        self.res.setText('')
        self.nb1.setText('')

#app
app=QApplication([])
menu=loadUi("menu.ui")
pgcd=loadUi("pgcd.ui")
ppcm=loadUi("ppcm.ui")
factorial=loadUi("factorial.ui")
df=loadUi("df.ui")
menu.show()
#menu
menu.pgcd.clicked.connect(lambda: show(pgcd))
menu.ppcm.clicked.connect(lambda: show(ppcm))
menu.factorial.clicked.connect(lambda: show(factorial))
menu.df.clicked.connect(lambda: show(df))
#pgcd
pgcd.menu.clicked.connect(lambda: close(pgcd))
pgcd.clc.clicked.connect(lambda:calc_pgcd(pgcd))
pgcd.unn.clicked.connect(lambda: ann(pgcd,2))
#ppcm
ppcm.menu.clicked.connect(lambda: close(ppcm))
ppcm.clc.clicked.connect(lambda:calc_ppcm(ppcm))
ppcm.unn.clicked.connect(lambda: ann(ppcm,2))
#factorial
factorial.menu.clicked.connect(lambda: close(factorial))
factorial.clc.clicked.connect(lambda: ff(factorial))
factorial.unn.clicked.connect(lambda: ann(factorial,1))
#df
df.menu.clicked.connect(lambda: close(df))
df.clc.clicked.connect(lambda:facteurs(df))
df.unn.clicked.connect(lambda: ann(df,1))

app.exec_()
