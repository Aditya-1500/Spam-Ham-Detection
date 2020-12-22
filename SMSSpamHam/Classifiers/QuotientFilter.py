# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 12:59:12 2020

@author: Aditya
"""

#Quotient Filter with (2^16) buckets and 32 bit unsigned murmurhash3 function

import mmh3
import copy
import pandas as pd

class QuotientFilter:

    def __init__(self):
        #Initialize the quotient filter
        self.qf = []
        self.p = 2**16       #Number of buckets
        self.q = 16          
        self.r = 16
        for i in range(self.p):
            #Three bits for each bucket
            #is_occupied, is_continuation, is_shifted
            self.qf.append([[0,0,0],-1])


    def lookup(self,key):
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
        	
        #Calculate the quotient and remainder
        fingerprint = mmh3.hash(key,signed=False)
        quotient = fingerprint // (2**self.r)
        remainder = fingerprint % (2**self.r)
        
        #If quotient is not present
        if self.qf[quotient][0][0] == 0:
            # return "Key is 'definitely not present'"
            return "Ham"
        
        #Else find the starting of cluster
        idx = quotient
        countOccupied = 0
        while self.qf[idx][0] != [1,0,0]:
            if self.qf[idx][0][0] == 1:
                countOccupied += 1
            idx -= 1
        	
        	#Find the start of run for quotient
        while countOccupied > 0 and idx < self.p:
            idx += 1
            idx = idx%self.p
            if self.qf[idx][0][1] == 0:
                countOccupied -= 1
        	
        	#Find remainder in the run
        if self.qf[idx][1] == remainder:
            # return "Key is 'probably present'"
            return "Spam"
        else:
            idx += 1
            while self.qf[idx][0][1] == 1:
                if remainder == self.qf[idx][1]:
                    # return "Key is 'probably present'"
                    return "Spam"
                if remainder > self.qf[idx-1][1] and remainder < self.qf[idx][1]:
                    # return "Key is 'definitely not present'"
                    return "Ham"
                idx += 1
        return "Ham"
        # return "Key is 'definitely not present'"
    
    
    def addKey(self,key='abc'):
        """
        Function to insert a key in the quotient filter.
        The function uses unsigned 32-bit MurMurHash3 to generate fingerprint.
        remainder is generated using least significant 'r' bits of the fingerprint (fp % 2**r)
        quotient is generated using most significant 'p-r' bits of the fingerprint (fp // 2**r)
        Args: 
        	- key: Key to be added
        Returns: None
        """
        fingerprint = mmh3.hash(key,signed=False)
        quotient = fingerprint // (2**self.r)
        remainder = fingerprint % (2**self.r)
        
        #If key is already 'probably present'
        if self.lookup(key) == 'Spam':
            return
        
        #If the quotient is not present and we are at start of cluster i.e. no collision, directly insert the key.
        if self.qf[quotient][0] == [0,0,0]:
            self.qf[quotient][0] = [1,0,0]
            self.qf[quotient][1] = remainder
            return 
        #If the position is occupied and to insert the key (hard collision), we have to shift.
        if self.qf[quotient][0][0] == 0:
            self.qf[quotient][0][0] = 1
            idx = quotient
            while self.qf[idx][0] != [0,0,0]:
                idx += 1
            self.qf[idx][0] = [0,0,1]
            self.qf[idx][1] = remainder
        else:
        	#Quotient is present but there are already fingerprints with same quotient (soft collision)
            idx = quotient
            countOccupied = 0
        		#Find the start of cluster and then start of run for quotient
            while self.qf[idx][0] != [1,0,0]:
                if self.qf[idx][0][0] == 1:
                    countOccupied += 1
                idx -= 1
            while countOccupied > 0 and idx < self.p:
                idx += 1
                if self.qf[idx][0][1] == 0:
                    countOccupied -= 1
            if self.qf[idx][0] == [0,0,0]:
                self.qf[idx][0] = [0,0,1]
                self.qf[idx][1] = remainder
            else:
                if remainder > self.qf[idx][1]:
                    #Move right
                    while self.qf[idx][1] < remainder and self.qf[idx][0] != [0,0,0]:
                        idx += 1
                        idx = idx % self.p
                    if self.qf[idx][0] == [0,0,0]:
                        self.qf[idx][0][1:] = [1,1]
                        self.qf[idx][1] = remainder
                    elif self.qf[idx][1] > remainder:
                        #Shift remaining remainders right
                        temp = self.qf[idx]
                        self.qf[idx][0][1:] = [1,0]
                        self.qf[idx][1] = remainder
                        idx += 1
                        idx = idx % self.p
                        while self.qf[idx][0] != [0,0,0]:
                            temp1 = self.qf[idx]
                            self.qf[idx][0][1] = temp[0][1]
                            self.qf[idx][0][2] = 1
                            self.qf[idx][1] = temp[1]
                            temp = temp1
                            idx += 1
                            idx = idx % self.p
                        self.qf[idx][0][1] = temp[0][1]
                        self.qf[idx][0][2] = 1
                        self.qf[idx][1] = temp[1]
                elif remainder < self.qf[idx][1]:
                    #Shift all right
                    temp = copy.deepcopy(self.qf[idx])
                    temp[0][1] = 1
                    self.qf[idx][0][1:] = [0,0]
                    self.qf[idx][1] = remainder
                    idx += 1
                    idx = idx % self.p
                    while self.qf[idx][0] != [0,0,0]:
                        temp1 = copy.deepcopy(self.qf[idx])
                        self.qf[idx][0][1] = temp[0][1]
                        self.qf[idx][0][2] = 1
                        self.qf[idx][1] = temp[1]
                        temp = copy.deepcopy(temp1)
                        idx += 1
                        idx = idx % self.p
                    self.qf[idx][0][1] = temp[0][1]
                    self.qf[idx][0][2] = 1
                    self.qf[idx][1] = temp[1]

"""
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
"""
# q = QuotientFilter()
# urls = pd.read_csv('SpamUrls.csv')
# counter = 0
# for u in urls['url']:
#     q.addKey(u)
#     counter+=1
