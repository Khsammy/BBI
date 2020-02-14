#All categories 
# Heat Map of Numbers in each category

def mkII():


    cols = ['H','MeH','MeL','L']
    H = '5,12,30,35,36,41,44,45,46,48,50,55,59,63,68,74,76,82,83,84,89'.split(',')
    MeH = '2,10,13,17,25,26,27,31,32,34,37,39,43,47,49,52,58,65,71,78,79,86,90'.split(',')
    MeL = '1,7,15,19,20,21,22,23,24,28,29,33,38,53,54,56,61,62,64,67,70,85'.split(',')           
    L = '3,4,6,8,9,11,14,16,18,40,42,51,57,66,69,72,73,75,77,80,81,87,88'.split(',')             

    mList = [cols] + [H] + [MeH] + [MeL] + [L]

    return mList



def fairchance():

    cols = ['H','MeH','MeL','L']
    H = '10,19,30,34,39,42,48,54,55,59,63,64,66,68,72,74,80,81,87,88,89,90'.split(',')
    MeH = '7,15,17,22,24,32,35,36,38,44,50,56,57,61,62,65,67,71,73,75,78,83,84'.split(',')
    MeL = '4,6,8,11,14,23,25,26,27,28,29,33,37,41,43,49,51,52,58,76,79,82'.split(',')
    L = '1,2,3,5,9,12,13,16,18,20,21,31,40,45,46,47,53,60,69,70,77,85,86'.split(',')

    fcList = [cols] + [H] + [MeH] + [MeL] + [L]

    return fcList


def zero6():

    cols = ['H','MeH','MeL','L']
    H = '1,4,12,13,18,25,30,36,42,43,44,45,51,52,53,56,63,77,78,79,81,84'.split(',')
    MeH = '9,10,11,16,17,20,21,22,27,28,40,46,49,55,57,60,64,68,75,83,85'.split(',')
    MeL = '3,5,8,32,34,37,38,48,50,54,58,61,62,65,69,70,71,72,73,86,87,90'.split(',')
    L = '2,6,7,14,15,19,23,24,26,29,31,33,35,39,41,47,59,66,67,74,76,80,82'.split(',')

    z6List = [cols] + [H] + [MeH] + [MeL] + [L]

    return z6List


def national():

    cols = ['H','MeH','MeL','L']
    H = '5,8,,18,19,24,25,27,29,33,34,46,49,50,58,61,67,73,81,84,87,90'.split(',')
    MeH = '1,4,14,28,35,41,43,45,52,53,62,63,66,69,75,76,77,78,79,82,83,86,89'.split(',')
    MeL = '2,6,7,9,10,12,15,20,22,23,30,38,40,42,44,48,51,55,57,60,80,88'.split(',')
    L = '3,11,13,16,17,21,26,31,32,36,37,39,47,54,56,59,64,65,68,70,71,72,74'.split(',')

    nList = [cols] + [H] + [MeH] + [MeL] + [L]

    return nList



def clubMaster():

    cols = ['H','MeH','MeL','L']
    H = '5,10,11,19,27,28,30,37,39,43,46,47,51,53,55,57,59,62,63,65,79,82'.split(',')
    MeH = '12,18,20,21,22,25,26,31,32,33,36,38,40,41,44,50,58,61,68,80,84,88,90'.split(',')
    MeL = '1,3,9,13,16,23,29,34,42,49,54,60,64,66,70,72,73,75,77,78,83,86'.split(',')
    L = '2,4,6,7,8,14,15,17,24,35,45,48,52,56,67,69,71,74,76,81,85,87,89'.split(',')

    cmList = [cols] + [H] + [MeH] + [MeL] + [L]

    return cmList


def supper():

    cols = ['H','MeH','MeL','L']
    H = '8,11,23,25,41,42,43,45,46,49,50,58,59,65,66,71,73,76,78,82,85,87'.split(',')
    MeH = '3,4,7,10,16,28,35,37,39,47,48,52,53,54,56,60,62,74,75,81,84,89,90'.split(',')
    MeL = '6,12,14,18,21,29,30,31,32,33,38,40,44,51,61,63,64,67,68,80,86,88'.split(',')
    L = '1,2,5,8,13,15,17,19,20,22,24,26,27,34,36,55,57,69,70,72,77,79,83'.split(',')
    
    sList = [cols] + [H] + [MeH] + [MeL] + [L]

    return sList


def premierKing():

    cols = ['H','MeH','MeL','L']
    H = '1,4,5,7,9,11,18,45,49,62,67,68,70,73,76,78,82,83,86,87,89,90'.split(',')
    MeH = '2,3,12,15,17,21,32,33,37,44,46,53,60,65,66,72,74,75,77,79,80,81,85'.split(',')
    MeL = '10,13,14,22,24,25,26,30,35,39,40,42,43,48,50,51,56,58,59,61,63,69'.split(',')
    L = '6,8,16,19,20,23,27,28,29,31,34,36,38,41,47,52,54,55,57,64,71,84,88'.split(',')
    
    pkList = [cols] + [H] + [MeH] + [MeL] + [L]

    return pkList


def vag():
    
    cols = ['H','MeH','MeL','L']
    H  = '6,13,20,29,33,35,37,46,54,55,56,57,70,72,73,74,76,77,80,81,86,89'.split(',')
    MeH  = '3,5,8,17,21,23,25,30,36,38,39,40,41,44,45,48,52,61,62,64,66,67,78'.split(',')
    MeL  = '4,7,9,10,11,12,15,16,22,27,28,32,34,42,43,50,63,69,71,83,87,88'.split(',')
    L  = '1,2,14,18,19,24,26,31,47,49,51,53,58,59,60,65,68,75,79,82,84,85,90'.split(',')

    vList = [cols] + [H] + [MeH] + [MeL] + [L]

    return vList

def bonanza():

    cols = ['H','MeH','MeL','L']
    H  = '6,9,11,24,36,40,46,49,62,64,68,69,73,76,77,79,80,81,84,87,89,90'.split(',')
    MeH  = '1,7,14,15,17,20,25,27,34,41,43,44,53,55,57,58,60,61,78,82,83,85,86'.split(',')
    MeL  = '21,22,23,26,28,29,31,32,33,39,45,47,48,50,59,65,66,67,70,71,72,74'.split(',')
    L  = '2,3,4,5,8,10,12,13,16,18,19,30,35,37,38,42,51,52,54,56,63,75,88'.split(',')

    bList = [cols] + [H] + [MeH] + [MeL] + [L]


    return bList

def jackpot():

    cols = ['H','MeH','MeL','L']
    H  = '3,11,13,26,28,44,45,46,47,54,56,58,59'.split(',')
    MeH  = ''.split(',')
    MeL  = ''.split(',')
    L  = ''.split(',')

    jpList = [cols] + [H] + [MeH] + [MeL] + [L]

    return jpList


def royal():
    
    cols = ['H','MeH','MeL','L']
    H  = ''.split(',')
    MeH  = ''.split(',')
    MeL  = ''.split(',')
    L  = ''.split(',')

    
    rList = [cols] + [H] + [MeH] + [MeL] + [L]

    return rList

def diamond():

    cols = ['H','MeH','MeL','L']
    H  = ''.split(',')
    MeH  = ''.split(',')
    MeL  = ''.split(',')
    L  = ''.split(',')
    
    dList = [cols] + [H] + [MeH] + [MeL] + [L]

    return dList


def fortune():

    cols = ['H','MeH','MeL','L']
    H  = ''.split(',')
    MeH  = ''.split(',')
    MeL  = ''.split(',')
    L  = ''.split(',')

    fList = [cols] + [H] + [MeH] + [MeL] + [L]

    return fList




def international():

    cols = ['H','MeH','MeL','L']
    H = ''.split(',')
    MeH = ''.split(',')
    MeL = ''.split(',')
    L = ''.split(',')
    
    inList = [cols] + [H] + [MeH] + [MeL] + [L]
    
    return inList


def gLuckyG():

    cols = ['H','MeH','MeL','L']
    H  = ''.split(',')
    MeH  = ''.split(',')
    MeL  = ''.split(',')
    L  = ''.split(',')

    glgList = [cols] + [H] + [MeH] + [MeL] + [L]

    return glgList

def tota():

    cols = ['H','MeH','MeL','L']
    H  = ''.split(',')
    MeH  = ''.split(',')
    MeL  = ''.split(',')
    L  = ''.split(',')

    tList = [cols] + [H] + [MeH] + [MeL] + [L]


    return tList

def peoples():

    cols = ['H','MeH','MeL','L']
    H  = ''.split(',')
    MeH  = ''.split(',')
    MeL  = ''.split(',')
    L  = ''.split(',')

    pList = [cols] + [H] + [MeH] + [MeL] + [L]

    return pList


def lucky():

    cols = ['H','MeH','MeL','L']
    H  = ''.split(',')
    MeH  = ''.split(',')
    MeL  = ''.split(',')
    L  = ''.split(',')
    
    lList = [cols] + [H] + [MeH] + [MeL] + [L]


    return lList


def enugu():

    cols = ['H','MeH','MeL','L']
    H  = ''.split(',')
    MeH  = ''.split(',')
    MeL  = ''.split(',')
    L  = ''.split(',')

    eList = [cols] + [H] + [MeH] + [MeL] + [L]


    return eList


def gold():

    cols = ['H','MeH','MeL','L']
    H  = ''.split(',')
    MeH  = ''.split(',')
    MeL  = ''.split(',')
    L  = ''.split(',')
                
    gList = [cols] + [H] + [MeH] + [MeL] + [L]

    return gList


def metro():

    cols = ['H','MeH','MeL','L']
    H  = ''.split(',')
    MeH  = ''.split(',')
    MeL  = ''.split(',')
    L  = ''.split(',')
    
    mList = [cols] + [H] + [MeH] + [MeL] + [L]

    return mList


def bingo():

    cols = ['H','MeH','MeL','L']
    H  = ''.split(',')
    MeH  = ''.split(',')
    MeL  = ''.split(',')
    L  = ''.split(',')

    bList = [cols] + [H] + [MeH] + [MeL] + [L]


    return bList





def midWeek():

    cols = ['H','MeH','MeL','L']
    H  = ''.split(',')
    MeH  = ''.split(',')
    MeL  = ''.split(',')
    L  = ''.split(',')
                                                              
    mwList = [cols] + [H] + [MeH] + [MeL] + [L]

    return mwList



def msp():

    cols = ['H','MeH','MeL','L']
    H  = ''.split(',')
    MeH  = ''.split(',')
    MeL  = ''.split(',')
    L  = ''.split(',')
                                                              
    mList = [cols] + [H] + [MeH] + [MeL] + [L]

    return mList




def intrenational():

    cols = ['H','MeH','MeL','L']
    H  = ''.split(',')
    MeH  = ''.split(',')
    MeL  = ''.split(',')
    L  = ''.split(',')
                                            
    inList = [cols] + [H] + [MeH] + [MeL] + [L]

    return inList


# get function with name
def get_heat_map(func):
    
    check_func = str(func).lower()
    if check_func == 'mkII':
        return mkII()
    
    elif check_func == 'fairchance':
        return fairchance()
    
    elif check_func == '06':
        return zero6()

    elif check_func == 'national':
        return national()
    
    elif check_func == 'clubmaster':
        return clubMaster()

    elif check_func == 'super':
        return supper()
    
    elif check_func == 'premierking':
        return premierKing()
    
    elif check_func == 'vag':
        return vag()
    
    elif check_func == 'bonanza':
        return bonanza()
    
    elif check_func == 'jackpot':
        return jackpot()
    
    elif check_func == 'gold':
        return gold()

    elif check_func == 'metro':
        return metro()
    
    elif check_func == 'royal':
        return royal()
    
    elif check_func == 'bingo':
        return bingo()

    elif check_func == 'fortune':
        return fortune()
    
    elif check_func == 'international':
        return international()
        
    elif check_func == 'diamond':
        return diamond()

    elif check_func == 'peoples':
        return peoples()
    
    elif check_func == 'lucky':
        return lucky()
    
    elif check_func == 'enugu':
        return enugu()
    
    elif check_func == 'midweek':
        return midWeek()

    elif check_func == 'tota':
        return tota()
    
    elif check_func == 'luckyg' or check_func == 'gluckyg':
        return gLuckyG()

    elif check_func == 'intrenational':
        return intrenational()
    
    elif check_func == 'msp':
        return msp()
    
    else:
        return 'Wrong Category Name..!!'


#print(get_heat_map('national'))
print('Heat Map loaded...')
