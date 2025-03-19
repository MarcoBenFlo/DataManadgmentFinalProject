# ECOR 1042 Lab 6 - Individual submission for batch_UI

# Update "" to list all students contributing to the team work
__author__ = "Marco Flores, Kazahchyang Ibrahim, Yasaal Rafi, Amira Khalid"
#Written by Marco Flores

# Update "" with your team (e.g. T102)
__team__ = "T046"

#==========================================#
"""
Implements the batch UI from an inputted text file, designed to use the functions previously designed to scan through a file to print updates on the data and the list if asked for within the file

Parameters:
-valid text file must be entered
-all values in the file must be seperated by ";"
-the first value must be L
-each value in the first row must be either L, S, C, H, or E
-each other value must be in accordance to the first value in each row

Examples:
=L;machine.csv;PRP;2000
=S;CACH;D;N
=H;PRP
Please enter the name of the file where your commands are stored: ****
Data loaded
Data sorted. <<<You selected not to display>>>
<<<Histograms with Study time will be shown>>>

=L;machine.csv;Vendor;amdahl
=S;MYCT;A;N
=E
Please enter the name of the file where your commands are stored: ****
Data loaded
Data sorted. <<<You selected not to display>>>

=L;machine.csv;all;1200
=S;CACH;A;Y
=C;CACH;2
=E
Please enter the name of the file where your commands are stored: ****
Data loaded
Data sorted.
[{'Vendor': 'apollo', 'Model': 'dn320', 'MYCT': 400, 'MMIN': 1000, 'MMAX': 3000, 'CACH': 0, 'PRP': 38, 'ERP': 23}, {'Vendor': 'bti', 'Model': '5000', 'MYCT': 350, 'MMIN': 64, 'MMAX': 64, 'CACH': 0, 'PRP': 10, 'ERP': 15}, {'Vendor': 'bti', 'Model': '8000', 'MYCT': 200, 'MMIN': 512, 'MMAX': 16000, 'CACH': 0, 'PRP': 35, 'ERP': 64}...
bat
"""
#Imported functions
import load_data, sort, curve_fit, histogram

#Prompting user to enter a file name
mfile = input("Please enter the name of the file where your commands are stored: ")
file = open(mfile, "rt")

#For each line in the file, the if statement will be repeated
for line in file:
    command = line.strip().split(";")
    function = command[0].upper()

#When L is in the first column, load_data is called and the values in the row are used for load_data
    if function == 'L':
        machines = load_data.load_data(command[1], (command[2], command[3]))   
        machines = load_data.add_average_main_memory(machines)
        print("Data loaded")                    
    
#When S is in the first column, sort is called and the values in the row are used for sort
    elif function == 'S':
        #If N is present, the values are not shown, but if Y (or any other value) is present, it prints the values from machines
        if command[3] == 'N':
            print("Data sorted. <<<You selected not to display>>>")
        else:
            print("Data sorted.")
            print(sort.sort(machines, command[2], command[1]))
    
#When C is in the first column, curve_fit is called and the values in the row are used for curve_fit   
    elif function == 'C':
        print(curve_fit.curve_fit(machines, command[1], command[2]))
    
#When H is in the first column, histogram is called and the values in the row are used for histogram  
    elif function == 'H':
        print("<<<Histograms with Study time will be shown>>>")
        print(histogram.histogram(machines, command[1]))

#Ends the program when E is found in the first column
    elif function == 'E':
        break