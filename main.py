#!/usr/bin/env python
import random
import units
import battlespace 

def introduction():
    

    

    greeting = 'Hello {}, I\'m Lieutenant {}. I will be your intelligence officer during your work here with the {} at Al-Hiyal.'.format(rank, lt_name, branch)
    return greeting
    
def help():
    help = """
    Type H: For help
    Type I: For latest intelligence report
    Type B: For Base Management
    Type S: For Security Accessment 
    Type P: 
    """
    return help

def play():
    print introduction()

if __name__ == '__main__':
    play()
