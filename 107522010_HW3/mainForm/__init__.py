from PyQt5 import QtWidgets,uic
from PyQt5.QtWidgets import *
import os
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtWidgets import QMessageBox
import numpy as np
import random,math
#from mpl_toolkits.mplot3d import Axes3D
path = os.getcwd()
#from  Main_Window import Ui_MainWindow
dpath = path  + os.sep + "Hopfield_dataset" + os.sep
mpath = path +os.sep+"ui"+os.sep +"Main_Window.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(mpath)
w=[]


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
        global w
        p=[]

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
        w=np.array(w)        
        self.listWidget.insertItem(0,self.menu.currentText())
        
        w1=w.reshape((-1,108))
        W=np.zeros((108,108))
        for i in range(len(w1)):
            W=W+1/108*(w1[i].T.dot(w1[i]) - np.eye(108))
 
   
    #清除layout內的widget及初始化向量in_array,d
    def clear_layout_onClick(self):
        for i in reversed(range(self.ltest.count())): 
            self.ltest.itemAt(i).widget().setParent(None)
        #self.listWidget.removeItemWidget(self.listWidget.takeItem(0))
        self.listWidget.clear()
        self.label.setText("")
        self.label_2.setText("")
        self.label_3.setText("")
        self.label_4.setText("")

        
    #在LAYOUT裡畫圖
    def plot3d(self):
        global w
        figure = plt.figure()
        canvas = FigureCanvas(figure)
        self.ltest.addWidget(canvas)
        plt.imshow(w,cmap='gray')
        plt.ylabel('X2')
        plt.xlabel('X1')
      

        figure = plt.figure()
        canvas = FigureCanvas(figure)
        self.test.addWidget(canvas)
        plt.imshow(w,cmap='gray')
        plt.ylabel('X2')
        plt.xlabel('X1')

        


        