# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 13:52:25 2021

@author: Ayman Abdeen
"""

import pyautogui
import time
import random

for z in range(1,10000):
	x = random.randint(0, 500)
	y = random.randint(0, 500)
	s = random.randint(0, 5)
	pyautogui.moveTo(x, y)

	localtime = time.localtime()
	result = time.strftime("%I:%M:%S %p", localtime)

	print('Moved at ' + str(result) + ' (' + str(x) + ', ' + str(y) + ')  --> '+ str(s) + 's  --> '+ str(z))

	time.sleep(s)
    
