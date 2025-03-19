# ECOR 1042 Lab 6 - Individual submission for text_UI

# Update "" to list all students contributing to the team work
__author__ = "Marco Flores, Kazahchyang Ibrahim, Yasaal Rafi, Amira Khalid"
#Written by Kazahchyang Ibrahim

# Update "" with your team (e.g. T102)
__team__ = "T046"

#==========================================#
# Place your script for your text_UI after this line
# Import necessary modules
import load_data
from typing import List, Dict
data_loader = load_data.load_data
m_avg = load_data.add_average_main_memory


# Import the sort function from the sort file
from sort import sort

# Import the histogram function from the histogram file
import histogram

# Import the curve_fit function from the curve_fit file
import curve_fit

def get_command() -> List[Dict]:
    """
    Loading data from a CSV file by entering 'L'.
    Sorting the loaded data by entering 'S'.
    Obtaining a polynomial equation from the loaded data by entering 'C'.
    Displaying a histogram using the loaded data by entering 'H'.
    Exiting the program by entering 'E'.
    """
    # Set up
    exit_command = False
    data_loaded = False
    loaded_type = ""

    # Iterate until the user prompts to exit the program
    while not exit_command:

        # Inform the user of available commands
        print("The available commands are:")
        print("   L)oad Data")
        print("   S)ort Data")
        print("   C)urve Fit")
        print("   H)istogram")
        print("   E)xit", end="\n\n")

        # Get user command
        command = input("Please type your command: ").lower()

        # Load data
        if command == "l":
            data_loaded, loaded_type = load_data_command()

        # Sort data
        elif command == "s" and data_loaded:
            data_loaded = sort_data_command(data_loaded, loaded_type)

        # Curve fit data
        elif command == "c" and data_loaded:
            curve_fit_data_command(data_loaded, loaded_type)

        # Make a histogram with data
        elif command == "h" and data_loaded:
            histogram_of_data_command(data_loaded, loaded_type)

        # Exit the program
        elif command == "e":
            exit_command = True

        # Try to manipulate data without loading any
        elif not data_loaded and (command == "l" or command == "s" or command == "c" or command == "h"):
            print("File not loaded. Please, load a file first.")

        # Invalid command before data loaded
        elif not data_loaded:
            print("No such command")

        # Invalid command
        else:
            print("Invalid command")

    return data_loaded


            
def load_data_command() -> (list[dict], str):
    """Return a tuple comprising two components: the first component is the list 
    loaded by the load_data function, and the second component is the attribute
    employed to load the data.

    The user is required to provide input for the arguments to be conveyed to the load_data function.
    These arguments include:

    The attribute serving as a filter during the data loading process.
    The value of the filter utilized to load the data.
    """
    # Prompt user to get the name of the file to load
    filename = input("Please enter the name of the file: ")

    # Get filter
    valid_filter = False
    while not valid_filter:
        # Prompt user for a filter
        attribute_filter = input("Please enter the attribute to use as a filter: ").upper()

        # Check if the filter is valid and leave the loop if it is
        if attribute_filter in {"CACH", "MODEL", "PRP", "VENDOR", "ALL"}:
            valid_filter = True
        else:
            print("Invalid filter key.")

    # Get attribute value
    if attribute_filter in {"MODEL", "VENDOR"}:
        # Prompt user for the attribute value
        attribute_value = input("Please enter the value of the attribute: ")
    elif attribute_filter != "ALL":
        # Prompt user for the attribute value
        attribute_value = int(input("Please enter the value of the attribute: "))
    else:
        # Give the attribute value a placeholder value
        attribute_value = "If you see this, you are super cool :D"

    # Inform the user that the data was loaded and return the loaded data
    print("Data loaded")
    return (m_avg(data_loader(filename, (attribute_filter, attribute_value))), attribute_filter)

    
def sort_data_command(data: list[dict], loaded_type: str) -> list[dict]:
    """Provides a sorted duplicate of the given list.

    The user is prompted to furnish the arguments for the sort function, encompassing:

    The attribute by which the list will be sorted.
    The order in which the list will be arranged, whether in ascending or descending order.
    """
    # Get attribute to sort by
    valid_attribute = False
    while not valid_attribute:

        # Prompt user for an attribute
        sorting_attribute = input("Please enter the attribute you want to use for sorting:\n'CACH', 'PRP', 'M_AVG', 'MYCT':\n").upper()

        # Check if input is a valid attribute and present
        if sorting_attribute != loaded_type and (sorting_attribute == "CACH" or sorting_attribute == "PRP" or sorting_attribute == "M_AVG" or sorting_attribute == "MYCT"):
            valid_attribute = True
        
        # Attribute is not present
        elif sorting_attribute == loaded_type:
            print("Attribute {} is not present in the loaded data.".format(loaded_type))

        # Inform user of an invalid attribute
        else:
            print("Invalid attribute.")
        
    # Get the order to sort
    valid_order = False
    while not valid_order:

        # Prompt user for sorting order
        sorting_order = input("Ascending (A) or Descending (D) order: ").upper()

        # Check if input is a valid order
        if sorting_order == "A" or sorting_order == "D":
            valid_order = True
        
        # Inform user of an invalid order
        else:
            print("Invalid order.")
        
    # Sort the loaded data
    sorted_data = sort(data, sorting_order, sorting_attribute)

    # Prompt user on if they want to have sorted data displayed
    display_data = input("Data Sorted. Do you want to display the data?: ").lower()

    # Display data
    if display_data == "y":
        print(sorted_data)
    
    # Return sorted data
    return sorted_data

def curve_fit_data_command(data: list[dict], loaded_type: str) -> None:
    """Presents the optimal polynomial equation that fits M_AVG in comparison to another attribute.

    The user is prompted to provide the necessary arguments for the curve_fit function, including:

    The attribute for M_AVG comparison.
    The order of the fitted polynomial, with a maximum degree of 5.
    """
    # Get attribute to comapare M_AVG to
    valid_attribute = False
    while not valid_attribute:
        
        # Prompt user for an attribute
        fit_attribute = input("Please enter the attribute you want to use to find the best fit for M_AVG: ").upper()

        # Check if input is a valid attribute
        if fit_attribute != loaded_type and (fit_attribute == "MYCT" or fit_attribute == "MMIN" or fit_attribute == "MMAX" or fit_attribute == "CACH" or fit_attribute == "PRP" or fit_attribute == "ERP"):
            valid_attribute = True

        # Inform user of an invalid attribute
        else:
            print("Invalid attribute.")

    # Get the degree to fit the curve to
    valid_degree = False
    while not valid_degree:

        # Prompt user for the degree
        fit_degree = input("Please enter the order of the polynomial to be fitted: ")

        # Check if user input can be converted to an integer
        try:
            fit_degree = int(fit_degree)

            # Insure that the degree is a valid order for the data loaded
            if fit_degree < len(data) and fit_degree <= 5 and fit_degree > 0:
                valid_degree = True

            # Inform user of an invalid degree
            else:
                print("Invalid degree.")

        # Inform user of an invalid degree
        except:
            print("Invalid degree.")

    # Get and print the polynomial equation
    fitted_curve = curve_fit(data, fit_attribute, fit_degree)
    print(fitted_curve)
        
    
    

def histogram_of_data_command(data: list[dict], loaded_type: str) -> None:
    """Presents a histogram illustrating the values of an attribute.

    The user is prompted to input the necessary arguments for the 
    histogram function, which include:

    The attribute to be utilized for the histogram's values.
    """
    # Get attribute for the histogram
    valid_attribute = False
    while not valid_attribute:

        # Prompt user for an attribute
        histogram_attribute = input("Please enter the attribute you want to use for plotting: ").upper()

        # Check if input is a valid attribute
        if loaded_type != histogram_attribute and (histogram_attribute == "MODEL" or histogram_attribute == "VENDOR" or histogram_attribute == "MYCT" or histogram_attribute == "MMIN" or histogram_attribute == "MMAX" or histogram_attribute == "CACH" or histogram_attribute == "PRP" or histogram_attribute == "ERP" or histogram_attribute == "M_AVG"):
            valid_attribute = True

            # Vendor is fixed to be what the function expects
            if histogram_attribute == "VENDOR":
                histogram_attribute = "Vendor"
        
            # Model is fixed to be what the function expects
            elif histogram_attribute == "MODEL":
                histogram_attribute = "Model"

        # Inform user of an invalid attribute
        else:
            print("Invalid attribute.")
            
    # Get and display the histogram
    histogram(data, histogram_attribute)
    
get_command()