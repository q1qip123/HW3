from PyQt5 import QtWidgets,uic
from PyQt5.QtWidgets import *
import os
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import numpy as np
import random,math
#from mpl_toolkits.mplot3d import Axes3D
path = os.getcwd()
#from  Main_Window import Ui_MainWindow
dpath = path  + os.sep + "Hopfield_dataset" + os.sep
mpath = path +os.sep+"ui"+os.sep +"Main_Window.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(mpath)
W=[]
theta=[]
size=0
a=0
class MainUi(QtWidgets.QMainWindow, Ui_MainWindow):  # Python的多重繼承 MainUi 繼承自兩個類別
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        self.retranslateUi(self)
        self.title = 'HW'
        self.iniGuiEvent()
    
      
     
    # 定義事件觸發時要啟動的函式
    def iniGuiEvent(self):
        self.setWindowTitle(self.title)
        self.load.clicked.connect(self.load_onClick)
        self.clear_layout.clicked.connect(self.clear_layout_onClick)
        self.start.clicked.connect(self.plot3d)

        
    # 點擊按鈕，讀取所選的文字檔
    def load_onClick(self):
        global W,theta,size,a
        p=[]
        w=[]
        f=open(dpath+self.menu.currentText(),'r') 
        line=f.readline()
        while line:
            if (line=='\n'):
                line=f.readline()
                continue
            for i in range(len(line)-1):
                if (line[i]=='1'):
                    p.append(1)
                else:
                    p.append(-1)
            w.append(np.array(p))
            p=[]                    
            line=f.readline()
        
        
        if(self.menu.currentText()=='Basic_Training.txt'):
            size=108
            a=9
        elif(self.menu.currentText()=='Bonus_Training.txt'):
            size=100
            a=10
        w=np.array(w)                
        w1=w.reshape((-1,size))
        W=np.zeros((size,size))
        for i in range(len(w1)):
            for j in range(len(w1[0])):
                for k in range(len(w1[0])):
                    W[j][k]=W[j][k]+w1[i][j]*w1[i][k]
                    
        W=1/size*W-3/size*np.eye(size)
    
        for i in range(len(w1[0])):
            sum=0
            for j in range(len(w1[0])):
                sum=sum+W[j][i]
            theta.append(sum)
            
        figure = plt.figure()
        canvas = FigureCanvas(figure)
        self.test.addWidget(canvas)
        plt.imshow(w,cmap='gray')
        plt.ylabel('X2')
        plt.xlabel('X1')
        
 
   
    #清除layout內的widget及初始化向量in_array,d
    def clear_layout_onClick(self):
        for i in reversed(range(self.ltest.count())): 
            self.ltest.itemAt(i).widget().setParent(None)
        
        for i in reversed(range(self.test.count())): 
            self.test.itemAt(i).widget().setParent(None)

        
    #在LAYOUT裡畫圖
    def plot3d(self):
        global W,theta,size,a
        figure = plt.figure()
        canvas = FigureCanvas(figure)
        self.ltest.addWidget(canvas)
        
        
        p=[]
        w=[]
        f=open(dpath+self.menu_2.currentText(),'r') 
        line=f.readline()
        while line:
            if (line=='\n'):
                line=f.readline()
                continue
            for i in range(len(line)-1):
                if (line[i]=='1'):
                    p.append(1)
                else:
                    p.append(-1)
            w.append(np.array(p))
            p=[]                    
            line=f.readline()
        
        w=np.array(w)

        if (self.all.isChecked() == True):
            for k in range(int(self.learn.text())):
                if ((k+1)**2<int(self.learn.text())+1<=(k+2)**2):
                    sizeoffig=k+2
                    break
            if (int(self.learn.text())==0):
                sizeoffig=1
            plt.subplot(sizeoffig,sizeoffig,1)                              
            plt.imshow(w,cmap='gray')
            plt.title("0 times")
                    
            x=w.reshape((-1,size))
            for i in range(int(self.learn.text())):
                for j in range(len(x)):
                    plt.subplot(sizeoffig,sizeoffig,i+2)                              
                    w=x.reshape((-1,a))
                    plt.imshow(w,cmap='gray')
                    plt.title("%d times" %(i+1))        
                    xtemp=[]
                    for k in range(len(x[0])):
                        xtemp.append(self.sgn(W[k].dot(x[j]),theta[k]))
                    x[j]=xtemp
        
        if (self.one.isChecked() == True):
            x=w.reshape((-1,size))
            for i in range(int(self.learn.text())):
                for j in range(len(x)):
                    xtemp=[]
                    for k in range(len(x[0])):
                        xtemp.append(self.sgn(W[k].dot(x[j]),theta[k]))
                    x[j]=xtemp  
         
                             
            w=x.reshape((-1,a))
            plt.imshow(w,cmap='gray') 
                    
                    
    def sgn(self,u,theta):
        if (u>theta):
            return 1
        elif (u==theta):
            return u
        elif(u<theta):
            return -1
        

        
        

        