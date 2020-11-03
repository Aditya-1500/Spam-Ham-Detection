# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 12:59:12 2020

@author: Aditya
"""

#Quotient Filter with 8(2^3) buckets and 32 bit unsigned murmurhash3 function

import mmh3
import copy

#Initialize the quotient filter
qf = []
for i in range(8):
    #Three bits for each bucket
    #is_occupied, is_continuation, is_shifted
    qf.append([[0,0,0],-1])

#q = 3		#number of buckets = 2^q
#r = 29		


def lookup(q,r,key="abc"):
    """
    	A function that checks whether a key is probably present in the filter or not.
    	Uses 32-bit unsigned MurMurHash3 function to generate fingerprint.
    	remainder is generated using least significant 'r' bits of the fingerprint (fp % 2**r)
    	quotient is generated using most significant 'p-r' bits of the fingerprint (fp // 2**r)
    	Args: 
    		- key: Key to be searched 
    	Output:
    		returns
    		- String "Key is definitely not present" if the key is not found
    		- String "Key is probably present" if a remainder matches
    """
    quotient = q
    remainder = r
    	
    #Calculate the quotient and remainder
    #    fingerprint = mmh3.lhash(key,signed=False)
    #    quotient = fingerprint // (2**r)
    #    remainder = fingerprint % (2**r)
    
    #If quotient is not present
    if qf[quotient][0][0] == 0:
        return "Key is 'definitely not present'"
    
    #Else find the starting of cluster
    idx = quotient
    countOccupied = 0
    while qf[idx][0] != [1,0,0]:
        if qf[idx][0][0] == 1:
            countOccupied += 1
        idx -= 1
    	
    	#Find the start of run for quotient
    while countOccupied > 0 and idx < 8:
        idx += 1
        idx = idx%8
        if qf[idx][0][1] == 0:
            countOccupied -= 1
    	
    	#Find remainder in the run
    if qf[idx][1] == remainder:
        return "Key is 'probably present'"
    else:
        idx += 1
        while qf[idx][0][1] == 1:
            if remainder == qf[idx][1]:
                return "Key is 'probably present'"
            if remainder > qf[idx-1][1] and remainder < qf[idx][1]:
                return "Key is 'definitely not present'"
            idx += 1
    return "Key is 'definitely not present'"


def addKey(q,r,key='abc'):
    """
    Function to insert a key in the quotient filter.
    The function uses unsigned 32-bit MurMurHash3 to generate fingerprint.
    remainder is generated using least significant 'r' bits of the fingerprint (fp % 2**r)
    quotient is generated using most significant 'p-r' bits of the fingerprint (fp // 2**r)
    Args: 
    	- key: Key to be added
    Returns: None
    """
    #    fingerprint = mmh3.hash(key,signed=False)
    #    quotient = fingerprint // (2**r)
    #    remainder = fingerprint % (2**r)
    #If the quotient is not present and we are at start of cluster i.e. no collision, directly insert the key.
    quotient = q
    remainder = r
    
    if qf[quotient][0] == [0,0,0]:
        qf[quotient][0] = [1,0,0]
        qf[quotient][1] = remainder
        return 
    #If the position is occupied and to insert the key (hard collision), we have to shift.
    if qf[quotient][0][0] == 0:
        qf[quotient][0][0] = 1
        idx = quotient
        while qf[idx][0] != [0,0,0]:
            idx += 1
        qf[idx][0] = [0,0,1]
        qf[idx][1] = remainder
    else:
    		#Quotient is present but there are already fingerprints with same quotient (soft collision)
        idx = quotient
        countOccupied = 0
    		#Find the start of cluster and then start of run for quotient
        while qf[idx][0] != [1,0,0]:
            if qf[idx][0][0] == 1:
                countOccupied += 1
            idx -= 1
        while countOccupied > 0 and idx < 8:
            idx += 1
            if qf[idx][0][1] == 0:
                countOccupied -= 1
        if qf[idx][0] == [0,0,0]:
            qf[idx][0] = [0,0,1]
            qf[idx][1] = remainder
        else:
            if remainder > qf[idx][1]:
                #Move right
                while qf[idx][1] < remainder and qf[idx][0] != [0,0,0]:
                    idx += 1
                    idx = idx % 8
                if qf[idx][0] == [0,0,0]:
                    qf[idx][0][1:] = [1,1]
                    qf[idx][1] = remainder
                elif qf[idx][1] > remainder:
                    #Shift remaining remainders right
                    temp = qf[idx]
                    qf[idx][0][1:] = [1,0]
                    qf[idx][1] = remainder
                    idx += 1
                    idx = idx % 8
                    while qf[idx][0] != [0,0,0]:
                        temp1 = qf[idx]
                        qf[idx][0][1] = temp[0][1]
                        qf[idx][0][2] = 1
                        qf[idx][1] = temp[1]
                        temp = temp1
                        idx += 1
                        idx = idx % 8
                    qf[idx][0][1] = temp[0][1]
                    qf[idx][0][2] = 1
                    qf[idx][1] = temp[1]
            elif remainder < qf[idx][1]:
                #Shift all right
                temp = copy.deepcopy(qf[idx])
                temp[0][1] = 1
                qf[idx][0][1:] = [0,0]
                qf[idx][1] = remainder
                idx += 1
                idx = idx % 8
                while qf[idx][0] != [0,0,0]:
                    temp1 = copy.deepcopy(qf[idx])
                    qf[idx][0][1] = temp[0][1]
                    qf[idx][0][2] = 1
                    qf[idx][1] = temp[1]
                    temp = copy.deepcopy(temp1)
                    idx += 1
                    idx = idx % 8
                qf[idx][0][1] = temp[0][1]
                qf[idx][0][2] = 1
                qf[idx][1] = temp[1]

addKey(1,7)
addKey(4,12)
addKey(7,16)
addKey(1,9)
addKey(2,11)
addKey(1,5)

print(lookup(1,6))
print(lookup(1,7))
print(lookup(1,8))
print(lookup(1,9))
print(lookup(1,10))

print(lookup(2,11))
print(lookup(2,12))

print(lookup(4,12))
print(lookup(4,15))

print(lookup(7,16))

