from typing import List, Tuple, Union
from PIL import Image, ImageQt
from PyQt5 import QtCore, QtGui, QtWidgets

class QDisplayFrame(QtWidgets.QFrame):
    
    ### Constatnts
    spacing = 6
    font = 16
    textHeight = int(font * 1.4) # aproximate font to pixle conversion
    pageLimit = 3
    outlineWidth = 5
    sliderTimerDelay = 20
    sliderHoverAreaSize = 50
    sliderMoveSpeed = 20
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        #Button graphics
        self.deleteButton = Button(ImageQt.toqpixmap(Image.open("DeleteButton.png")))
        self.rightButton = Button(ImageQt.toqpixmap(Image.open("RightButton.png")))
        self.leftButton = Button(ImageQt.toqpixmap(Image.open("LeftButton.png")))

        ### Containers
        self.pages = []

        ### Variables
        self.sliderPosition = 0
        self.sliderDelta = 0
        self.selectedIndex = -1

        # Set up
        self.setMouseTracking(True)

        
#######################################################################################
### Controller


    def mouseMoveEvent(self, event):
        self.sliderCheck(event.pos())
        self.hoverCheck(event.pos())
        

    #checks if the cursor is hovering over the "move left" or "move right" areas at the edges of the frame
    def sliderCheck(self, pos):
        if pos.x() < self.sliderHoverAreaSize and self.sliderPosition > 0:
            if self.sliderDelta == 0:
                self.sliderDelta = - self.sliderMoveSpeed
                self.sliderTimerID = self.startTimer( self.sliderTimerDelay, QtCore.Qt.CoarseTimer )
        elif pos.x() > self.width() - self.sliderHoverAreaSize:
            if self.sliderDelta == 0:
                self.sliderDelta = self.sliderMoveSpeed
                self.sliderTimerID = self.startTimer( self.sliderTimerDelay, QtCore.Qt.CoarseTimer )
        else:
            if self.sliderDelta != 0:
                self.sliderDelta = 0
                self.killTimer(self.sliderTimerID)#stop counting
            

    #layz substitute for a mouse clicked event
    def mouseReleaseEvent(self, event):
        # something is selected
        if self.selectedIndex >= 0:
            if self.deleteButton.boundaries.contains(event.pos()):
                self.deletePage()
            elif self.leftButton.boundaries.contains(event.pos()):
                self.swapPages(self.selectedIndex, self.selectedIndex - 1)
            elif self.rightButton.boundaries.contains(event.pos()):
                self.swapPages(self.selectedIndex, self.selectedIndex + 1)
        self.repaint()


    #Checks to see if the cursor is hovering over a page
    def hoverCheck(self, pos):
        #no hover checks while slider is in motion
        if self.sliderDelta != 0:
            return

        #default case 
        self.selectedIndex = -1

        #check for hovering
        for index, page in enumerate(self.pages):
            if page.boundaries.contains(pos):
                self.selectedIndex = index
                self.positionButtons(page.boundaries, index)

        self.repaint()


    #positions the applicable buttons onto the page 
    def positionButtons(self, pageBoundaries, index):
        #delete
        delX = pageBoundaries.x() + ((pageBoundaries.width() - self.deleteButton.boundaries.width() + 1) / 2) 
        delY = pageBoundaries.height() - self.deleteButton.boundaries.height() - 10
        self.deleteButton.setPosition(delX, delY)

        #left and right
        leftX = pageBoundaries.x()
        rightX = pageBoundaries.x() + pageBoundaries.width() - self.deleteButton.boundaries.width()
        lrY = pageBoundaries.y() + ((pageBoundaries.height() - self.deleteButton.boundaries.height() + 1) / 2) 
        self.leftButton.setPosition(leftX, lrY)
        self.rightButton.setPosition(rightX, lrY)

        #disable the left and right buttons if this is the last page in that direction
        self.leftButton.enabled = (index != 0)
        self.rightButton.enabled = (index != (len(self.pages) - 1))


    #don't retain selection when leaving the frame
    def leaveEvent(self, event):
        self.selectedIndex = -1

        #remove any slide timers
        if self.sliderDelta != 0:
                self.sliderDelta = 0
                self.killTimer(self.sliderTimerID)

        self.repaint()


    #Scale pages to match resize
    def resizeEvent(self, event):
        self.calculatePageBoundries()
        self.checkBoundaries()
        self.calculateSliderPositions()


    #timer used for "hover and hold" scrolling left and right
    def timerEvent(self, event):
        if len(self.pages) > self.pageLimit:
            #add initial movement
            self.sliderPosition += self.sliderDelta
            
            #disallow selecting while moving
            if self.selectedIndex >= 0:
                self.selectedIndex = -1

            self.checkBoundaries()
            self.calculateSliderPositions()
            self.repaint()
    

    #corrects the scroll position if it has gone too far in one direction
    def checkBoundaries(self, forceRightmost = False):
        #no pages, return to default
        if len(self.pages) == 0:
            self.sliderPosition = 0
            return 

        #check right boundary
        lastPageBoundaries = self.pages[len(self.pages) - 1].boundaries
        rightBoundry = lastPageBoundaries.x() + lastPageBoundaries.width()
        if self.width() > rightBoundry or forceRightmost:
            self.sliderPosition = (self.sliderPosition + rightBoundry) - self.width()

        #check left boundary 
        if self.sliderPosition < 0:
            self.sliderPosition = 0


#######################################################################################
### Model


    #adds a new page on the rightmost position
    def addPage( self, image, width, height):

        self.pages.append( Page(ImageQt.toqpixmap(image), width, height))

        self.calculatePageBoundries()
        #True option makes sure the new scan is in view
        self.checkBoundaries(True)
        self.calculateSliderPositions()
        self.repaint()


    #deletes the page at selectedIndex and repositions remaining pages
    def deletePage(self):
        del self.pages[self.selectedIndex]
        self.selectedIndex = -1
        # first call to move pages right of the deleted
        self.calculatePageBoundries()
        self.checkBoundaries()
        self.calculateSliderPositions()


    #swaps the position of 2 pages given their indexes. used for reordering pages
    def swapPages(self, index1, index2):
        pageCount = len(self.pages)
        # dont allow swaps with self or invalid indecies
        if (index1 >= 0        and index2 >= 0 and
            index1 < pageCount and index2 < pageCount and
            index1 != index2):

            tempPage = self.pages[index1]
            self.pages[index1] = self.pages[index2]
            self.pages[index2] = tempPage

            self.selectedIndex = -1
            self.calculatePageBoundries()
            self.repaint()


    #calculates where and how large pages should be given the current frame size
    def calculatePageBoundries(self):
        #return if there is nothing to calculate
        if len(self.pages) == 0:
            return

        maxWidth, maxHeight = self.getMeasurements()

        for count, page in enumerate(self.pages):
            page.scaledPixMap = page.originalPixMap.scaled(maxWidth, maxHeight, QtCore.Qt.KeepAspectRatio)
        
        self.calculateSliderPositions()

    def calculateSliderPositions(self):
        runningWidth = 0
        for count, page in enumerate(self.pages):            
            xPosition = runningWidth - self.sliderPosition
            page.boundaries = QtCore.QRect(xPosition, 0, page.scaledPixMap.width(), page.scaledPixMap.height())
            runningWidth +=  page.scaledPixMap.width() + self.spacing
                

    #calculates the largest area a single page is allowed to inhabit
    def getMeasurements(self)-> Union[int, int]:
        totalWidth = self.width()
        totalheight = self.height()
        totalPages = len(self.pages)
        
        if totalPages > self.pageLimit:
            totalPages = self.pageLimit

        maxWidth = ((totalWidth - ((totalPages - 1) * self.spacing) ) / totalPages) 
        maxHeight = totalheight - self.textHeight

        return maxWidth, maxHeight


    #returns a list of the scanned pages
    def getPages(self)-> List[Tuple[ImageQt.QPixmap, int, int]]:
        scannedPages = []
        for p in self.pages:
            scannedPages.append((p.originalPixMap, p.width, p.height))
        return scannedPages



#######################################################################################
### View


    #paints all elements to the screen
    def paintEvent(self, event):
        painter = QtGui.QPainter(self)

        self.clearScreen(painter)
        
        #return if there is nothing to draw
        if len(self.pages) == 0:
            return

        for index, page in enumerate(self.pages):
            #this page is off the screen on the left and doesnt need to be drawn
            if page.boundaries.x() + page.boundaries.width() < 0:
                continue
            #this page is off the screen on the right. no more pages need to be drawn.
            if page.boundaries.x() > self.width():
                break

            # Draw scanned image
            painter.drawPixmap(QtCore.QPoint(page.boundaries.x(), page.boundaries.y()), page.scaledPixMap)

            if index == self.selectedIndex:
                #draw outline
                pen = QtGui.QPen(QtCore.Qt.green)
                pen.setWidth(self.outlineWidth)
                painter.drawRect(page.boundaries)

                #draw buttons
                painter.drawPixmap(QtCore.QPoint(self.deleteButton.boundaries.x(), self.deleteButton.boundaries.y()), self.deleteButton.pixMap)
                if self.leftButton.enabled == True:
                    painter.drawPixmap(QtCore.QPoint(self.leftButton.boundaries.x(), self.leftButton.boundaries.y()), self.leftButton.pixMap)
                if self.rightButton.enabled == True:
                    painter.drawPixmap(QtCore.QPoint(self.rightButton.boundaries.x(), self.rightButton.boundaries.y()), self.rightButton.pixMap)
                
            # Draw page number
            painter.setFont(QtGui.QFont("Arial", self.font))
            painter.drawText(QtCore.QRect(page.boundaries.x(), 
                                          page.boundaries.height(), 
                                          page.boundaries.width(), 
                                          self.textHeight), 
                                          QtCore.Qt.AlignCenter, 
                                          str(index + 1))
        painter.end()


    #draws background color over entire screen
    def clearScreen(self, painter):
        painter.drawRect(QtCore.QRect(-1,-1,
                                      self.width() + 1, 
                                      self.height() + 1))


#######################################################################################
### Helper Classes


class Page():
    def __init__(self, pixMap, width, height):
        self.originalPixMap = pixMap
        self.scaledPixMap = pixMap
        self.width = width 
        self.height = height
        self.boundaries = QtCore.QRect()

class Button():
    def __init__(self, pixMap):
        self.pixMap = pixMap
        self.boundaries = QtCore.QRect(0, 0, pixMap.width(), pixMap.height())
        self.enabled = True
    
    def setPosition(self, x, y):
        self.boundaries = QtCore.QRect(x, y, self.pixMap.width(), self.pixMap.height())
        