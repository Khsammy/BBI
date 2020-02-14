#!/usr/bin/python3

import random
from itertools import combinations_with_replacement as cwr
from itertools import combinations as comb
from heat_map import get_heat_map as ghm


#banner
def banner():
    conBanner = """
                ________&______&_____&____&_____
                |                               |
                |                               |
                |   _____       _____           |
                |   |   |         |             π
                |   |___|         |             |
                |   |   |         |             π
                |   |___|       __|__           |
                |                               |
                |______?___?___?__?__?__?__?__?_π
                version 0.1
                \n\n
                """ 

    return conBanner

#Frequency based on HML Pattern
#Numeric
def genHMLNum(fn):
    #Alphabetic
    def genHMLAlpha():
        alphaRep = ['H', 'MeH', 'MeL', 'L']
        alphaRes = list(cwr(alphaRep,5))
        return random.sample(alphaRes, 1)
    
    fDataSet = ghm(fn)
    cols = fDataSet.pop(0)
    H = fDataSet[0]
    MeH = fDataSet[1]
    MeL = fDataSet[2]
    L = fDataSet[3]
    
    PattAlphaComb = genHMLAlpha()
    print(PattAlphaComb[0])
    PattNumComb = []


    # guess numbers according to hml pattern generated
    count = len(PattAlphaComb)
    while(count != 0):
        for alpha in PattAlphaComb[0]:
            if str(alpha).lower() == 'h':
                PattNumComb.append(random.sample(H, 1))
            elif str(alpha).lower() == 'meh':
                PattNumComb.append(random.sample(MeH, 1))
            elif str(alpha).lower() == 'mel':
                PattNumComb.append(random.sample(MeL, 1))
            elif str(alpha).lower() == 'l':
                PattNumComb.append(random.sample(L, 1))
            else:
                PattNumComb.append("invalid.")

        count -= 1

    return PattNumComb

#EO Pattern
def genEONum():

    #generate matrix
    def genMat(unOdd,unEven):

        #print(unOdd)
        #print(unEven)
        cOdd = random.sample(
                unOdd[
                    random.sample(
                        range(len(unOdd)),1)[0]
                    ],10)

        cEven = random.sample(
                unEven[
                    random.sample(
                        range(len(unEven)),1)[0]
                    ],10)

        mResult = []
        for i in range(len(cOdd)):
            mResult.append(int(cOdd[i]) + int(cEven[i]))

        print(f'A => {cOdd}\nB => {cEven}\nA + B => {mResult}')

        VResult = [(mResult[2]),(mResult[5]),(mResult[7]),(mResult[8]),(mResult[9])]

        return VResult


    #mains
    cSet = [(num) for num in range(1,47)]
    even = []
    odd = []

    for num in cSet:
        if int(num) % 2 == 0:
            even.append(int(num))
        else:
            odd.append(int(num))

    oV = list(comb(odd,10))
    eV = list(comb(even,10))


    uniqOdd = []
    for row in oV:
        if sum(row) == 240:
            uniqOdd.append(row)
        else:
            continue

    #print(uniqOdd)

    uniqEven = []
    for row in eV:
        if sum(row) > 259 and sum(row) < 289:
            uniqEven.append(row)
        else:
            continue

    #print(uniqEven)

    finalSet = genMat(uniqOdd,uniqEven)

    return finalSet


#Based on the Tens Pattern 
# Numeric
#breaks the main set down into sub-sets of ten numbers
def genTensNum():
    finalSet = []
    tempSet = []
    for num in range(1,91):
        if '0' in str(num):
            if str(num) == '90':
                finalSet.append(tempSet)
                tempSet = []                            
                tempSet.append(num)                                      
                finalSet.append(tempSet)
            else:
                finalSet.append(tempSet)                                   
                tempSet = []
                tempSet.append(num)

        else:
            tempSet.append(num)      

    choiceSet = random.sample(finalSet[random.sample(range(0,9),1)[0]],5)

    return choiceSet


#Magic generator
def magicGen():
    alphaSet = ['N','T']
    oddSet = '21,27,31,33,17,11,13,7,39,41'.split(',')
    evenSet = '22,26,34,24,28,36,40,14,18,46'.split(',')
    mSet = '43,53,65,57,45,47,35,21,75,87'.split(',')

    nSet = oddSet + evenSet + mSet

    alphaChoice = str(random.sample(alphaSet,1)[0]).lower()

    if alphaChoice == 'n':
        print(alphaChoice.upper() + ":")
        nComb = list(comb(nSet,5))
        return random.sample(nComb,2)

    elif alphaChoice == 't':
        print(alphaChoice.upper() + ":")
        tSet = []
        for digit in nSet:
            rev = int((int(digit) % 10 * 10) + int(int(digit)/10))
            tSet.append(rev)

        tComb = list(comb(tSet,5))
        return random.sample(tComb,2)

    else:
        raise ValueError



#generates just 2 numbers
def magicGen2():
    alphaSet = ['N','T']
    oddSet = '21,27,31,33,17,11,13,7,39,41'.split(',')
    evenSet = '22,26,34,24,28,36,40,14,18,46'.split(',')       
    mSet = '43,53,65,57,45,47,35,21,75,87'.split(',')

    nSet = oddSet + evenSet + mSet

    alphaChoice = str(random.sample(alphaSet,1)[0]).lower()

    if alphaChoice == 'n':                                         
        print(alphaChoice.upper() + ":")                           
        nComb = list(comb(nSet,2))
        return random.sample(nComb,2)

    elif alphaChoice == 't':
        print(alphaChoice.upper() + ":")
        tSet = []
        for digit in nSet:
            rev = int((int(digit) % 10 * 10) + int(int(digit)/10))
            tSet.append(rev)

        tComb = list(comb(tSet,2))
        return random.sample(tComb,2)

    else:
        raise ValueError


#add all differences
#generates N numbers 
def generateNumbers(func,lastPlayed,pattern_choice):

    if str(pattern_choice).lower() == 'hml':
        hml = genHMLNum(func)
        if sorted(lastPlayed) != sorted(hml):
            return hml
        else:
            return -1
    elif str(pattern_choice).lower() == 'tens':
        tens = genTensNum()
        if tens != []:
            return tens
        else:
            return -1

    elif str(pattern_choice).lower() == 'eo':
        eo = genEONum()
        if eo != []:
            return eo
        else:
            return -1

    elif str(pattern_choice).lower() == 'mag':
        mn = magicGen()
        if mn != []:
            return mn
        else:
            return -1

    elif str(pattern_choice).lower() == 'mag2':
        mn = magicGen2()
        if mn != []:
            return mn
        else:
            return -1

    else:
        raise ValueError

#mains
def main():
    print(banner())
    print("#?> Maybe 80%-90% Chance")

    print("Pattern Choice e.g(eo,hml,tens,mag)")
    pattern_choice = input("Choose a Pattern : ")

    if pattern_choice == 'hml':
        print("\nCategory (e.g vag,super)\n")
        category = input("Category :> ")

        #get last numbers played from the user
        print("\nEnter the Total  Number of last drawn Numbers that you know e.g 1:\n\n")
        numOfLastPlayed_o = int(input("N Total =>> "))

        lastPlayed = []

        for num in range(1,(5*numOfLastPlayed_o)+1):
            dNum = input("Number " + str(num) + ": ")

            if dNum.isdigit() != True:
                print("Please only Numeric-based values are allowed!")
                break

            elif int(dNum) > 90 or int(dNum) < 1:
                print("Number entered not in range(1-90)")
                break
            else:
                lastPlayed.append(int(dNum))

        print("\nNumbers Entered are => " + str(lastPlayed))

        print("Generated Number Set is " +str(generateNumbers(category,lastPlayed,pattern_choice)))


    else:
        print("Generated Number Set is " + str(generateNumbers('','',pattern_choice)))



if __name__ == "__main__":
    main()
