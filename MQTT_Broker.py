
import paho.mqtt.client as mqtt
import csv
import paho.mqtt.publish as publish
class BrokerServer:

    __client = 1

    #constructor
    def __init__(self):
        type(self).__client = mqtt.Client()

    #The callback for when the client receives a CONNACK response from the server.
    def on_connect(client, userdata, flags, rc):
        print("Connected with result code "+str(rc))

    #connect to Broker as "publisher"
    def connectToBroker(self):

        self.__client.on_connect = BrokerServer.on_connect

        self.__client.connect("localhost", 1883, 60)

    #starting the publishing service
    def startPublishing(self):
        self.__client.loop_start()
        print("Broker publishing initialized")

    #load Test Data into a list or Array to send it step by step
    def loadTestdataPackage(self):
        testdata = []
        reader = csv.reader(open("../Testdaten/Soundsensor.csv"))
        for row in reader:
            testdata.append(row)

        return testdata
        #for element in testdata:
        #    print(element)


    #send Test Data to broker and let him publish it
    def publishToBroker(self,testData):
        for row in testData:
            while(len(row) != 0):
                self.publishDataToSubscriber(row.pop())


    #publishes Test Data to all subscriber/fans
    def publishDataToSubscriber(self,testDataFile):
        releaseData = self.__client.publish("test/file", testDataFile)

    #closes the connection between publisher and broker
    def closeConnection(self):
        self.__client.loop_stop()



#Main Testing for functions

testServer = BrokerServer()
testServer.startPublishing()
tempList = []
tempList = testServer.loadTestdataPackage()
testServer.publishToBroker(tempList)
testServer.closeConnection()
