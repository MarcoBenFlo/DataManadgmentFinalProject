# ECOR 1042 Lab 6 - Individual submission for histogram

# Remember to include docstring and type annotations for your functions

# Update "" to list all students contributing to the team work
__author__ = "Marco Flores, Kazahchyang Ibrahim, Yasaal Rafi, Amira Khalid"
#Written by Yasaal Rafi

# Update "" with your team (e.g. T102)
__team__ = "T046"

#==========================================#
import matplotlib.pyplot as plt
import numpy as np


def histogram(machine_list: list, attribute: str):
    """Return a histogram. If numerical, return the max value. If categorial, return -1.
    
    Examples
    >>> histogram([{"Vendor": "amdahl", "PRP": 21}, {"Vendor": "apollo", "PRP": 10}, {"Vendor": "bit", "PRP": 50}], "Vendor")
    -1
    
    >>> histogram([{"Vendor": "amdahl", "PRP": 21}, {"Vendor": "apollo", "PRP": 10}, {"Vendor": "bit", "PRP": 50}], "PRP")
    50
    
    >>> histogram([{"Vendor": "amdahl", "CACH": 201}, {"Vendor": "apollo", "CACH": 100}, {"Vendor": "bit", "CACH": 650}], "CACH")
    650
    """
    values = [machine[attribute] for machine in machine_list]

    if isinstance(values[0], str):

        unique_values = list(set(values))
        counts = [values.count(value) for value in unique_values]
        plt.figure()
        plt.bar(unique_values, counts)
        plt.xlabel(attribute)
        plt.ylabel('Count')
        plt.title('Histogram of ' + attribute)
        plt.show()
        return -1
    else:

        num_bins = 20
        max_value = max(values)
        bins = [i * max_value / num_bins for i in range(num_bins + 1)]	
        plt.figure()
        plt.hist(values, bins=bins)
        plt.xlabel(attribute)
        plt.ylabel('Count')
        plt.title('Histogram of ' + attribute)
        plt.show()
        return max_value
