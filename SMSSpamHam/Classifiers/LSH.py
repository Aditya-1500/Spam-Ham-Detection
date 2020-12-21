# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 15:33:57 2020

@author: Aditya
"""

import pandas as pd
from datasketch import MinHash

class LSH:
    def __init__(self):
        self.hamHash = MinHash(num_perm=512)
        self.spamHash = MinHash(num_perm=512)  
        self.hamCl = []
        self.spamCl = []
        
    def update(self,hCl,sCl):
        self.hamCl = hCl
        self.spamCl = sCl
        for ham in self.hamCl:
            for h in ham.split(" "):
                self.hamHash.update(h.encode('utf-8'))
        for spam in self.spamCl:
            for s in spam.split(" "):
                self.spamHash.update(s.encode('utf-8'))
    
    def query(self,message):
        q = MinHash(num_perm=512)
        for m in message.split(" "):
            q.update(m.encode('utf-8'))
        jh = q.jaccard(self.hamHash)
        js = q.jaccard(self.spamHash)
        if jh > js:
            return "Ham"
        else:
            return "Spam"
            
"""
messages = pd.read_csv('Ham_Spam_Clusters.csv')
hamCl = list(messages['Ham'])
spamCl = list(messages['Spam'])
                
l = LSH()
l.update(hamCl,spamCl)
print(l.query(spamCl[0]))
"""