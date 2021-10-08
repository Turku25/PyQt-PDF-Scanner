#Linux imports
import os
import sane
from fpdf import FPDF
from PyQt5 import QtGui

class Linux():
    
    def __init__(self):
        self.devices = []
        self.currentDevice = None


    #searches network for scanner devices
    def getScannerDevices(self):
        ver = sane.init()
        self.devices =  sane.get_devices()


    #returns number of devices found
    def deviceCount(self):
        return len(self.devices)


    #returns a list of device names
    def getDeviceNames(self):
        names = []
        for d in self.devices:
            names.append(d[2])
        return names
    

    #Connects to the device at a given index
    def openDevice(self, index):
        if index == None:
            self.currentDevice = None
            return
        
        if index >= 0 and index < self.deviceCount():
            self.currentDevice = sane.open(self.devices[index][0])
            return
        
        self.currentDevice = None


    # boolean of if a device is open
    def isDeviceOpen(self):
        return self.currentDevice != None
    

    #Performs a scan with the given parameters on the current device
    def scan(self, scanWidth, scanHeight, bitdepth, color, scanQuality):
        self.scannedImage = None
        try:
            self.currentDevice.br_x = scanWidth
            self.currentDevice.br_y = scanHeight
            self.currentDevice.depth = bitdepth
            self.currentDevice.mode = color
            self.currentDevice.resolution = scanQuality
        except: 
            print("Failed to set print settings")

        self.currentDevice.start()
        self.scannedImage = self.currentDevice.snap()


    #gets the most recently scanned image
    def getImage(self):
        return self.scannedImage


    #Creates a PDF out of the given pages and saves them to a given file
    def saveToPDF(self, fileName, pages):
        pdf = FPDF('P', 'mm', 'Letter')

        #write pages to temp JPG files
        # FPDF doesn't have a way to take images straight from memory
        filePaths = []
        for count, page in enumerate(pages):
            tempFileName = "tmp_{0}.jpg".format(count)
            filePaths.append(tempFileName)
            QtGui.QPixmap(page[0]).save(tempFileName, "JPG")

        #add each page to the PDF
        for count, filePath in enumerate(filePaths):
            width = pages[count][1]
            height = pages[count][2]
            pdf.add_page(format = (width, height))
            pdf.image(filePath, 0, 0, width, height, "JPG")

        #write the PDF file
        pdf.output(fileName, "F")

        #remove temp files
        for filePath in filePaths:
            os.remove(filePath)