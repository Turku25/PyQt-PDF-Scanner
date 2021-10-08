from PIL import Image
from PyQt5 import QtCore, QtWidgets
from OsAbstractions import Linux
import MainUI

class UiController:
    def UiControllerSetup(self, rootWidget):
        self.rootWidget = rootWidget
        rootWidget.setWindowTitle("PyQt PDF Scanner")
        self.os = Linux()

        self.ui.SearchButton.clicked.connect(self.searchForDevices)
        self.ui.ScanButton.clicked.connect(self.scanPressed)
        self.ui.DeviceComboBox.currentIndexChanged.connect(self.updateDevice)
        self.ui.ScanSizeCombo.currentIndexChanged.connect(self.updateScanSize)
        self.ui.CustomUnitComboBox.currentIndexChanged.connect(self.updateCustomSize)
        self.ui.CustomWidthSpinBox.valueChanged.connect(self.updateCustomSize)
        self.ui.CustomHeightSpinBox.valueChanged.connect(self.updateCustomSize)
        self.ui.PortraitRadio.clicked.connect(self.updateCustomSize)
        self.ui.LandscapeRadio.clicked.connect(self.updateCustomSize)
        self.ui.QualityComboBox.currentIndexChanged.connect(self.updateScanQuality)
        self.ui.ColorRadio.clicked.connect(self.updateColor)
        self.ui.GrayRadio.clicked.connect(self.updateColor)
        self.ui.SaveButton.clicked.connect(self.savePressed)

        #Load default values
        self.updateScanSize()
        self.updateScanQuality()
        self.updateColor()
        self.createLockList()
        self.currentDevice = None

        #start an initial device scan
        controller.searchForDevices()


#######################################################################################
### UI Handlers 


    # Finds Scanners on the network and updates the selection UI
    def searchForDevices(self):
        self.lockUI()
        try:
            self.startWaitForWorker(self.searchForDevicesWorker, self.searchForDevicesFinished, "Searching for scanner devices...")
        except Exception as e:
            print("Device search failed: " + str(e))

    # Uses the current GUI data to request a scan
    def scanPressed(self):
        if not self.os.isDeviceOpen():
            return #no valid device selected

        self.lockUI()
        scanArgs = (self.scanWidth, self.scanHeight, self.bitdepth, self.color, self.scanQuality)

        #begin scan
        try:
            self.startWaitForWorker(self.scanWorker, self.scanFinished, "Scanning...", *scanArgs)
        except Exception as e:
            print("Scan failed: " + str(e))


    #save a PDF of the current pages
    def savePressed(self):
        #no pages to save
        if(len(self.ui.DisplayFrame.getPages()) == 0):
            return
        name = QtWidgets.QFileDialog.getSaveFileName(self.rootWidget, 'Save File', "Scanned_Pages.pdf")[0]
        #save was canceled / no destination was specified
        if name == '':
            return
        pages = self.ui.DisplayFrame.getPages()

        self.os.saveToPDF(name, pages)


    #called when the user changes the device selection
    #also called automatically after a device search with current index 0
    def updateDevice(self):
        index = self.ui.DeviceComboBox.currentIndex()
        if index == -1:
            return 

        try:
            self.startWaitForWorker(self.openDeviceWorker, self.unlockUI, "Connecting to Device...", index)
        except Exception as e:
            print("Device could not be loaded: " + str(e))


    #called when the user makes a change to the scan size combobox
    def updateScanSize(self):
        index = self.ui.ScanSizeCombo.currentIndex()
        if 0 <= index < 6:
            self.enableCustomSize(False)
            self.scanWidth, self.scanHeight = self.indexToSizeInMM(index)
        elif index == 6: #custom size
            self.enableCustomSize(True)
            

    #Sets the enabled state of custom size controls for when they are available or not
    def enableCustomSize(self, boolean):
        self.ui.CustomUnitLabel.setEnabled(boolean)
        self.ui.CustomWidthLabel.setEnabled(boolean)
        self.ui.CustomHeightLabel.setEnabled(boolean)
        self.ui.CustomUnitComboBox.setEnabled(boolean)
        self.ui.CustomWidthSpinBox.setEnabled(boolean)
        self.ui.CustomHeightSpinBox.setEnabled(boolean)


    #called any time an input variable to custom size is changed by the user
    #not all changes will result in a new size
    def updateCustomSize(self):
        #Custom size is not active
        if self.ui.ScanSizeCombo.currentIndex() != 6:
            return

        #Inches
        if self.ui.CustomUnitComboBox.currentIndex() == 0:
            self.scanWidth = self.inchesToMM(self.ui.CustomWidthSpinBox.value())
            self.scanHeight = self.inchesToMM(self.ui.CustomHeightSpinBox.value())
        #Millimeters
        elif self.ui.CustomUnitComboBox.currentIndex() == 1:
            self.scanWidth = self.ui.CustomWidthSpinBox.value()
            self.scanHeight = self.ui.CustomHeightSpinBox.value()
        
        if self.ui.LandscapeRadio.isChecked():
            temp = self.scanWidth
            self.scanWidth = self.scanHeight
            self.scanHeight = temp


    #called when user changes the scan quality
    def updateScanQuality(self):
        index = self.ui.QualityComboBox.currentIndex()
        if 0 <= index < 6:
            self.scanQuality = self.indexToQuality(index)


    #called when user changes the color selection
    def updateColor(self):
        if self.ui.ColorRadio.isChecked():
            self.color = 'color'
            self.bitdepth = 8
        elif self.ui.GrayRadio.isChecked():
            self.color = 'grayscale'
            self.bitdepth = 16


#######################################################################################
### Threading


    #boiler plate for a threaded worker that will display a wait popup while completing work
    #only one worker can be working at a time
    def startWaitForWorker(self, work, finished, message, *workArgs):
        dialog = QtWidgets.QProgressDialog(message, "cancel", 0 ,0, self.rootWidget)
        dialog.setWindowTitle("Please Wait")
        dialog.setCancelButton(None)
        dialog.show()
        self.workerThread = None
        self.workerThread = Worker(work, finished, dialog, *workArgs) 
        self.workerThread.start()


    #off main thread search for scanner devices
    def searchForDevicesWorker(self):
        self.os.getScannerDevices()


    #called when the device search worker thread is completed
    #adds the found devices to the UI and selects device at index 0, opening it
    def searchForDevicesFinished(self):
        self.ui.DeviceComboBox.clear()

        if self.os.deviceCount() == 0:
            self.ui.DeviceComboBox.addItem("No Devices Found")
        else:
            for name in self.os.getDeviceNames():
                self.ui.DeviceComboBox.addItem(name)

        self.ui.DeviceComboBox.setCurrentIndex(0)


    #off main thread call for the os abstraction to open a specific device
    def openDeviceWorker(self, *args):
        self.os.openDevice(*args)


    #performs a scan off the main thread so the UI doesn't freeze
    def scanWorker(self, *scanArgs):
        self.os.scan(*scanArgs)


    #called when a scan worker thread finishes it's work
    #adds the newly scanned page to the UI
    def scanFinished(self):
        scannedImage = self.os.getImage()
        if scannedImage == None:
            return

        if self.ui.LandscapeRadio.isChecked():
            scannedImage = scannedImage.transpose(Image.ROTATE_270)
            height = self.scanWidth
            width = self.scanHeight
        else:
            height = self.scanHeight
            width = self.scanWidth
        
        self.ui.DisplayFrame.addPage(scannedImage, width, height)
        self.unlockUI()


#######################################################################################
### Helper Functions

    #creates a list of all the UI elements that need to be locked while an operation is under way
    def createLockList(self):
        self.savedEnables = []
        self.lockList = []
        self.lockList.append(self.ui.DeviceComboBox)
        self.lockList.append(self.ui.SearchButton)
        self.lockList.append(self.ui.ScanSizeCombo)
        self.lockList.append(self.ui.CustomUnitComboBox)
        self.lockList.append(self.ui.CustomWidthSpinBox)
        self.lockList.append(self.ui.CustomHeightSpinBox)
        self.lockList.append(self.ui.QualityComboBox)
        self.lockList.append(self.ui.ColorRadio)
        self.lockList.append(self.ui.GrayRadio)
        self.lockList.append(self.ui.PortraitRadio)
        self.lockList.append(self.ui.LandscapeRadio)
        self.lockList.append(self.ui.ScanButton)
        self.lockList.append(self.ui.SaveButton)
        self.lockList.append(self.ui.DisplayFrame)


    #Save the current enabled state and disable each ui element
    #Used to prevent modifying data while an operation is happening
    def lockUI(self):
        #the UI is already locked
        if len(self.savedEnables) != 0:
            return
        for element in self.lockList:
            self.savedEnables.append(element.isEnabled())
            element.setEnabled(False)


    #Restore saved enabled states to each ui element
    def unlockUI(self):
        for index, enabled in enumerate(self.savedEnables):
            self.lockList[index].setEnabled(enabled)
        self.savedEnables.clear()


    #converts inches to millimeters
    def inchesToMM(self, inches):
        return inches * 25.4


    #mapping of size combobox index to size values
    def indexToSizeInMM(self, index):
        if index == 0:
            # 8.5 x 11 in
            return 215.9, 279.4
        elif index == 1:
            # 8.5 x 14 in
            return 215.9, 355.6
        elif index == 2:
            return 297, 420
        elif index == 3:
            return 210, 297
        elif index == 4:
            return 148, 210
        elif index == 5:
            return 105, 148
        # default
        return 0, 0


    #mapping of quality combobox index to quality value
    def indexToQuality(self, index):
        if index == 0:
            return 75
        elif index == 1:
            return 150
        elif index == 2:
            return 300
        elif index == 3:
            return 600
        elif index == 4:
            return 1200
        elif index == 5:
            return 2400


#######################################################################################
### Helper Classes


class Worker(QtCore.QThread):
    def __init__(self, work, finished, waitWindow, *workArgs):
        super().__init__()
        self.work = work
        if finished != None:
            self.finished.connect(finished)
        self.waitWindow = waitWindow
        self.workArgs = workArgs

    def run(self):
        self.work(*self.workArgs)
        self.waitWindow.deleteLater()


#######################################################################################
### Main Method


if __name__ == "__main__":
    import sys
    controller = UiController()
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    
    controller.ui = MainUI.Ui_MainWindow()
    controller.ui.setupUi(mainWindow)
    

    #center the main window on the screen
    screenGeometry = QtWidgets.QApplication.desktop().availableGeometry()
    x = (screenGeometry.width()-mainWindow.width()) / 2
    y = (screenGeometry.height()-mainWindow.height()) / 2
    mainWindow.move(int(x + 0.5), int(y + 0.5))

    controller.UiControllerSetup(mainWindow)
    mainWindow.show()

    sys.exit(app.exec_())