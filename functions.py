#Real estate analyzer functions
def getFloatInput(sPrompt, fMinNumberAllowed):

    #Default fValue to -1 to enter loop:
    fValue = -1

    while fValue < fMinNumberAllowed:
        try:
            fValue = float(input(sPrompt))
            if fValue <  fMinNumberAllowed:
                print ("Input a number that is greater than 0.")
             
        except ValueError:
                print ("Input a number that is greater than 0.")
                continue
               
    return fValue

#Write validation for prompt if user wants another number
def getAnotherInput(sAnswer):
    
    sAnswer = input("Enter another number Y or N: ").upper()
    if sAnswer != 'Y' and sAnswer != 'N':
        nErrValue = 1
        while nErrValue > 0:
            sAnswer = input("Enter another number Y or N: ").upper()
            if sAnswer == 'Y' or sAnswer == 'N':
                break
            else:
                continue
    return sAnswer     

def getMedian(lstName):
    
    #Write a conditional statement that determines if the list has an odd or even number of elements
    if len(lstName)%2 != 0:
        lstMed = lstName[len(lstName) // 2]
    else:
        iFirstElement = lstName[(len(lstName) // 2) - 1]
        iSecondElement = lstName[(len(lstName) // 2)]
        lstMed = (iFirstElement + iSecondElement) // 2
        
    return lstMed