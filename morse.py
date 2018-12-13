# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 03:32:28 2018

@author: PC1
"""

import winsound
import pandas as pd
import time

df = pd.read_csv('code.txt')  
letters = df.letter
codes = df.code
global Hz,dur
Hz = 550
dur = 200
def dot():
    winsound.Beep(Hz,dur)    
    
def dash():
    winsound.Beep(Hz,3*dur)
    
def letter_gap():
    time.sleep(dur/1000)

def word_gap():
    time.sleep(7*dur/1000)


def translate(letter):
        number = 0 
        for let in letters:
            
            if letter.upper() == let:
                return codes[number]
            elif letter.upper() == ' ':
                return '/'
            number = number + 1
            
            
text = input('prowide the letter\n')

output = ''
iteration = 0
for char in text:
    print (len(text),iteration)
    if iteration < len(text):
        output = output + translate(char) + ' ' 
    else:
        output = output + translate(char) 

for char in output:
    if char =='.':
        dot()
    elif char =='-':
        dash()
    elif char == ' ':
        letter_gap()
    elif char =='/':
        word_gap()
print(output)
