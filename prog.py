# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 16:50:40 2017

@author: bnc
"""

import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from BrokerBenchmark02 import Ui_BrokerBenchmarkTester
 
class MyFirstGuiProgram(QMainWindow, Ui_BrokerBenchmarkTester):
    def __init__(self, parent=None, name=None):
        super(MyFirstGuiProgram, self).__init__(parent)
        self.setupUi(self)
        
        # Set Forms now
        self.comboBox_2.addItem("MQTT")
        self.comboBox_2.addItem("Apollo")
        self.comboBox_2.addItem("rabbitMQ")
        self.comboBox_2.addItem("Mosquitto")
        self.comboBox.addItem("MongoDB")
        self.comboBox.addItem("MySQL")
        self.comboBox.addItem("NoSQL")
        self.comboBox.setDisabled(True)
        self.radioButton_2.setChecked(True)
        self.label_7.setText("<html><head/><body><p>MQTT ist ein von OASIS standardisiertes <br> M2M-Kommunikationsprotokoll. Die IANA <br>reserviert für MQTT die Ports 1883 und 8883. <br>MQTT-Nachrichten können mit dem <br>TLS-Protokoll verschlüsselt werden.</p></body></html>")
        self.label_2.setDisabled(True)
        self.label_4.setDisabled(True)
        self.label_8.setDisabled(True)
        self.label_8.setText("<html><head/><body><p>Schema-freie, dokumentenorientierte NoSQL-<br>Datenbank, die in der Programmiersprache <br>C++ geschrieben ist.</p></body></html>")
        
        #Action's for Elements
        self.radioButton.clicked.connect(self.checkRadioButton)
        self.radioButton_2.clicked.connect(self.checkRadioButton2)
        self.comboBox_2.currentIndexChanged.connect(self.setDescriptionBroker)
        self.comboBox.currentIndexChanged.connect(self.setDescriptionDB)
        self.pushButton.clicked.connect(self.onClickStart)
        
        
        
    def setDescriptionBroker(self, i):
        if i == 0:
            self.label_7.setText("<html><head/><body><p>MQTT ist ein von OASIS standardisiertes <br> M2M-Kommunikationsprotokoll. Die IANA <br>reserviert für MQTT die Ports 1883 und 8883. <br>MQTT-Nachrichten können mit dem <br>TLS-Protokoll verschlüsselt werden.</p></body></html>")
        if i == 1:
            self.label_7.setText("Apollo")
        if i == 2:
            self.label_7.setText("rabbitMQ")
        if i == 3:
            self.label_7.setText("Mosquitto")
        
        
    #def checkOptions(self):
        

    def setDescriptionDB(self, i):
        if i == 0:
            self.label_8.setText("<html><head/><body><p>Schema-freie, dokumentenorientierte NoSQL-<br>Datenbank, die in der Programmiersprache <br>C++ geschrieben ist.</p></body></html>")
        if i == 1:
            self.label_8.setText("<html><head/><body><p>MySQL</p></body></html>")
        if i == 2:
            self.label_8.setText("<html><head/><body><p>NoSQL</p></body></html>")


    def checkRadioButton(self):
        if self.radioButton.isEnabled():
            self.comboBox.setEnabled(True)
            self.label_2.setEnabled(True)
            self.label_4.setEnabled(True)
            self.label_8.setEnabled(True)
    def checkRadioButton2(self):
        if self.radioButton_2.isEnabled():
            self.comboBox.setDisabled(True)
            self.label_2.setDisabled(True)
            self.label_4.setDisabled(True)
            self.label_8.setDisabled(True)
            
    
    
    def addInputTextToListbox(self):
        txt = self.myTextInput.text()
        self.listWidget.addItem(txt)
        
    def onClickStart(self):
        print('Test')

    # run Broker (Mosquitto) on Windows
    def runBrokerMosquittoTest(self):
        import time
        import subprocess
        import paho.mqtt.client as mqtt

        subprocess.Popen([r"..\Mosquitto\mos\mosquitto.exe"])
        client = mqtt.Client()

        client.connect("localhost", 1883, 60)
    
        client.loop_start()

        while True:
            time.sleep(2)
            client.publish("test/temperature", "test")

""" 
if __name__ == '__main__':
	app = QtWidgets.QApplication(sys.argv)
	#dialog = QtWidgets.QDialog()
    dialog = QtWidgets.QMainWindow()
 
	prog = MyFirstGuiProgram(dialog)
 
	dialog.show()
	sys.exit(app.exec_())
"""

if __name__ == "__main__":
    app = QApplication(sys.argv)
    #window = QtWidgets.QWidget()
    #ui = Ui_MainWindow()
    ui = MyFirstGuiProgram()
    #ui.setupUi(window)
    #MainWindow.show()
    ui.show()
    sys.exit(app.exec_())
    