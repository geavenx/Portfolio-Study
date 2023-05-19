def updateTimes(signalOne, signalTwo):
    maxEqualSignal = 0
    maxEqualSignalUpdates = 0
    
    counter = 0
    x = len(signalOne)
    y = len(signalTwo)
    
    if x > y:    
        for i in signalTwo:
            if i == signalOne[counter]:
                if i > maxEqualSignal:
                    maxEqualSignalUpdates += 1
                    maxEqualSignal = i
            counter += 1
    elif y >= x:
        for i in signalOne:
            if i == signalTwo[counter]:
                if i > maxEqualSignal:
                    maxEqualSignalUpdates += 1
                    maxEqualSignal = i
            counter += 1
    
    
    return maxEqualSignalUpdates

