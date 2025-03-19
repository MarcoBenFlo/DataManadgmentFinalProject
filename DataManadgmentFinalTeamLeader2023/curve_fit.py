# ECOR 1042 Lab 6 - Individual submission for curve_fit function

# Remember to include docstring and type annotations for your functions

# Update "" to list all students contributing to the team work
__author__ = "Marco Flores, Kazahchyang Ibrahim, Yasaal Rafi, Amira Khalid"
#Written by Amira Khalid

# Update "" with your team (e.g. T102)
__team__ = "T046"

#==========================================#
# Place your curve_fit function after this line

import matplotlib.pyplot as plt
import numpy as np

def curve_fit(data: list, attr: str, num: int) -> list:
    """
    Return a string representation of the equation of the
    best fit for the average of M_AVG
    
    >>>curve_fit([{'CACH': 5, 'M_AVG': 2}, {'CACH': 4, 'M_AVG': 5}], 'CACH', 2)
'-3.0x+17.0'
    >>>curve_fit([{'CACH': 32, 'M_AVG': 2000}, {'CACH': 64 , 'M_AVG': 400}], 'CACH', 3)
'-50.0x+3600.0'
    >>>curve_fit([{'CACH': 32, 'M_AVG': 400}, {'CACH': 64 , 'M_AVG': 50}], 'CACH', 1)
'-10.94x+750.0'

    """

    avg_main_memory = {}
    
    for i in data: 
        if i[attr] in avg_main_memory.keys():
            avg_main_memory[i[attr]].append(i["M_AVG"])
        else:
            avg_main_memory[i[attr]] = [i["M_AVG"]]

    for key in avg_main_memory.keys():
        total = 0
        for value in avg_main_memory[key]:
            total += value
        avg = round(total / len(avg_main_memory[key]), 2)
        avg_main_memory[key] = avg


    x = list(avg_main_memory.keys())
    y = list(avg_main_memory.values())
    
    length = len(x)
    
    if length > num + 1:
        degree = num
    else:
        degree = length - 1

        
    z = np.polyfit(x, y, degree)
    string = ""
    order = len(z) - 1

    for item in z:
        if order > 1:
            string += str(round(item, 2)) + "x^" + str(order)

        elif order == 1:
            string += str(round(item, 2)) + "x"
            
        elif order < 1:
            string += str(round(item, 2))
            
        order = order - 1
        if order >= 0:
            string += "+"
            
    string = string.replace('+-', '-')
    return string
