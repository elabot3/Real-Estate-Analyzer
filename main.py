# Lists and Real Estate Analyzer
# May 10, 2022
# Author: L
# Purpose: Design a sales analyzer program for real estate properties.

from functions import *

def main():
    #Initialize variable to enter the loop
    fPropValue = .01
    
    #Create a list to store the input float values
    lstSalesProp = []
    
    #Ask user for property value
    while fPropValue == .01:
        fSalesPrice = getFloatInput("Enter property sales value: ", .01)
    
        #Convert property value to float and add to lstSalesProp 
        fProp = lstSalesProp.append(float(fSalesPrice))
    
        #Ask if the user would like to enter another number 
        sAnum = getAnotherInput("Enter another number Y or N: ")

        if sAnum == 'N':
            break
        
    #Sort the list 
    lstSalesProp.sort()
    
    #Write a for loop to output each property value 
    nProp = 1
    for fPropPrice in lstSalesProp:
        print(f'Property {nProp} $ {fPropPrice:>10,.2f}')
        nProp+=1
    
    #Determine the minimum, maximum, total, average, median, commission
    lstMin = min(lstSalesProp)
    lstMax = max(lstSalesProp)
    lstTotal = sum(lstSalesProp)
    lstAverage = lstTotal / len(lstSalesProp)
    lstMedian = getMedian(lstSalesProp)
    lstCommission = lstTotal * .03
    
    #Output values
    fPrintValues = f"""
Minimum:     $ {lstMin:>15,.2f}
Maximum:     $ {lstMax:>15,.2f}
Total:       $ {lstTotal:>15,.2f}
Average:     $ {lstAverage:>15,.2f}
Median:      $ {lstMedian:>15,.2f}
Commission:  $ {lstCommission:>15,.2f}
"""
    print(fPrintValues)
      
main()