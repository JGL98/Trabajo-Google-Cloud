# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 11:21:37 2022

@author: chewa
"""

import random 
import string

VUESTRA_SIGLA = "JGL"

random.seed(2022+hash(VUESTRA_SIGLA))

topics = ["search","book","buy"]

f = open("events.csv","w")

for event in range(100):
	time = random.randint(5,30)
	message = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
	topic = random.choices(topics,weights=[0.8,0.15,0.05],k=1)
	print("Time: %i, Topic: %s, Message: %s"%(time,topic[0],message))
	f.write("%i,%s,%s\n"%(time,topic[0],message))

f.flush()
f.close()
print("Done")
