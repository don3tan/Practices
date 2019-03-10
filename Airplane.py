class Seat:

    def __init__(self, seatType):
        # Seat Types
        # W - Window | M - Mid | A - Aisle
        self.seatType = seatType
        self.passengerNo = None
    
    def addPassenger(self, passengerNo):
        self.passengerNo = passengerNo

class SegmentCol:

    def __init__(self, noOfSeats, segmentPos):
        self.noOfSeats = noOfSeats
        self.segmentPos = segmentPos
        self.col = []
        
    def createCol(self):
        for i in range(1,self.noOfSeats + 1):

            #Check and assign Seat Type

            seatType = "M"

            if i == 1:
                if self.segmentPos == "left":
                    seatType = "W"
                elif self.segmentPos == "right":
                    seatType = "A"
                else:
                    seatType = "A"

            elif i == self.noOfSeats:
                if self.segmentPos == "left":
                    seatType = "A"
                elif self.segmentPos == "right":
                    seatType = "W"
                else:
                    seatType = "A"

            self.col.append(Seat(seatType))
    
    def getList(self):

        # Get the list of Seat Instances

        temp = []

        for seat in self.col:
            temp.append(seat)

        return temp

    def displayListPassengerNo(self):

        # Get the list of Passenger No

        temp = []
        for i in self.col:
            temp.append(i.passengerNo)
        return temp

    # def displayListSeatType(self):

    #     # Get the list of Seat Type

    #     temp = []
    #     for i in self.col:
    #         temp.append(i.seatType)
    #     return temp

class Plane:

    def __init__(self,buildArray,noOfPassenger):
        self.buildArray = buildArray
        self.noOfSegment = len(buildArray)
        self.planeLayout = []
        self.noOfPassenger = noOfPassenger
    
    def findMaxRow(self):
        self.maxRow = self.buildArray[0][1]
        for i in range(1,len(self.buildArray)):
            if self.buildArray[i][1] > self.maxRow:
                self.maxRow = self.buildArray[i][1]

    def buildPlaneStructure(self):
        
        # Define the length of loop using max row number
        self.findMaxRow()

        for row in range(1,self.maxRow+1):

            col = []

            for i in range(1, self.noOfSegment + 1):

                # Check the required number of row for each segment
                if self.buildArray[i-1][1] >= row:

                    segmentPos = "mid"

                    if i == 1:

                        segmentPos = "left"

                    elif i == self.noOfSegment:

                        segmentPos = "right"


                    temp = SegmentCol(self.buildArray[i-1][0], segmentPos)
                    temp.createCol()
                    col.append(temp)

                # Append empty arrays if there are no more rows
                else:
                    col.append([])
                
                
            self.planeLayout.append(col)
    
    def allocatePassenger(self):
        
        # Create a list of passenger numbers
        # Assume that passenger numbers are just running numbers
        passengersList = list(range(1,self.noOfPassenger + 1))

        # Assign priority for seat allocation
        # Allocation starts from Aisle Seats
        seatPriority = ["A","W","M"]

        # Loop through the priority array
        for seatType in seatPriority:

            # Accessing Segments from plane layout
            for seg in self.planeLayout:

                # Accessing Segcol instances within Segments
                for segCol in seg:

                    # Prevent errors when segcol has no seats
                    if type(segCol) != type([]):

                        #Allocate a passenger to a seat
                        for seat in segCol.getList():
                            if len(passengersList) > 0:
                                if seat.seatType == seatType:
                                    seat.addPassenger(passengersList[0])
                                    passengersList.pop(0)
                            else:
                                break
                        if len(passengersList) == 0:
                            break
                if len(passengersList) == 0:
                    break
    
    def buildPlane(self):
        if len(self.buildArray) >= 2:
            self.buildPlaneStructure()
            self.allocatePassenger()
            return True
        else:
            return False
    
    def displayListPassengerNo(self):

        temp = []

        result = self.buildPlane()

        if not result:
            return "Please input a bigger array"

        for seg in self.planeLayout:

            # Temp2 splits the plane by row numbers by wrapping it in an array

            temp2 = []

            for segCol in seg:
                if type(segCol) != type([]):

                    temp2.append(segCol.displayListPassengerNo())

                else:

                    #Appending a empty array for empty Segcol to maintain correct positioning
                    temp2.append(segCol)

            temp.append(temp2)
        
        return temp

if __name__ == "__main__":

    print('Test Case 1')
    plane1 = Plane([[3,2],[4,3],[2,3],[3,4]],30)
    result = plane1.displayListPassengerNo()
    expected = [[[19 , 25, 1], [2, 26, 27, 3], [4, 5], [6, 28, 20]], [[21, 29, 7], [8, 30, None, 9], [10, 11], [12, None, 22]], [[], [13, None, None, 14], [15, 16], [17, None, 23]], [[], [], [], [18, None, 24]]]
    assert expected == result
    print('Expected:', expected)
    print('Actual  :', result)

    print('\n')

    print('Test Case 2')
    plane1 = Plane([[2,5],[4,7],[2,3]],20)
    result = plane1.displayListPassengerNo()
    expected = [[[None,1],[2,None,None,3],[4,None]],[[None,5],[6,None,None,7],[8,None]],[[None,9],[10,None,None,11],[12,None]],[[None,13],[14,None,None,15],[]],[[None,16],[17,None,None,18],[]],[[],[19,None,None,20],[]],[[],[None,None,None,None],[]]]
    assert expected == result
    print('Expected:', expected)
    print('Actual  :', result)

    print('\n')

    print('Test Case 3')
    plane1 = Plane([[2,2],[2,2],[2,2]],5)
    result = plane1.displayListPassengerNo()
    expected = [[[None,1],[2,3],[4,None]],[[None,5],[None,None],[None,None]]]
    assert expected == result
    print('Expected:', expected)
    print('Actual  :', result)

    print('\n')

    print('Test Case 4')
    plane1 = Plane([[2,2]],5)
    result = plane1.displayListPassengerNo()
    expected = "Please input a bigger array"
    assert expected == result
    print('Expected:', expected)
    print('Actual  :', result)

