import paho.mqtt.client as mqtt
import paramiko


class Broker:
    __client = 1
    __message = ""

    #constructor
    def __init__(self):
        self.__client = mqtt.Client()

    #opens the connection to BrokerServer
    def connectToBroker(self):
        #self.__client.connect("192.168.2.1", 1883, 60)  #real Szenario
        self.__client.connect("localhost", 1883, 60)    #testing

    #starts listening to the Broker
    def startListening(self):
        # Blocking call that processes network traffic, dispatches callbacks and
        # handles reconnecting.
        # Other loop*() functions are available that give a threaded interface and a
        # manual interface.
        self.__client.loop_start()

    #shuts down the broker service
    def shutdownBroker(self):
        stdin, stdout, stderr = Broker.exec_command("\x03")
        self.__client.close()


    #help method for connection state
    def on_connect(client, userdata, flags, rc):
        print("Connected with result code " + str(rc))
        client.subscribe("test/file")

    #on recieve action method
    def on_message(client, userdata, msg):
        __message = msg.topic + " " + str(msg.payload)
        print(__message)


class SSHClient:
    __ssh = 1

    #test

    #constructor
    def __init__(self):
        __ssh = paramiko.SSHClient()

    # run Broker via Terminal execute
    def startBroker(self):
        self.__client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        if not self.__ssh.connect('192.168.1.2', username='pi', password='raspberry'):
            print("SSH session failed on login.")
            print(str(self.__ssh))
        else:
            print("SSH session login successful")
            stdin, stdout, stderr = SSHClient.exec_command("mosquitto")
            for line in stdout.read().splitlines():
                print(line)

import subprocess
from pymongo import MongoClient
class MongoDatabase:

    __dataBaseClient = 1

    def __init__(self):
        subprocess.call("mongod")
        __dataBaseCLient = MongoClient()

    def insertData(self, _id, Value_name, Values, Datetime):
        db = self.__dataBaseClient.BrokerBenchmarkDB
        testCollection = db.testCollection

        post = {"_id" : _id,
                "Value_name" : Value_name,
                "Values" : Values,
                "Datetime" : Datetime}

        post_id = testCollection.insert_one(post).inserted_id
        


#maintesting for classes and functions

testBroker = Broker()
testBroker.on_connect = Broker.on_connect
testBroker.on_message = Broker.on_message
testBroker.connectToBroker()
testBroker.startListening()


