# ECOR 1042 Lab 3 - Template


# Update "" to list all students contributing to the team work
__author__ = "Marco Flores, Kazahchyang Ibrahim, Yasaal Rafi, Amira Khalid"

# Update "" with your team (e.g. T102)
__team__ = "T046"

#==========================================#
# Place your machine_vendor_list function after this line
import string

def machine_vendor_list(file_path: str, vendor: str) -> list:
    """Return the set of the machines of the requested vendor.
    Examples
    >>> machine_vendor_list('machine.csv', 'adviser')
    [{'Model': '32/60', 'MYCT': 125, 'MMIN': 256, 'MMAX': 6000, 'CACH': 256, 'PRP': 198, 'ERP': 199}]
    
    >>> machine_vendor_list('machine.csv','apollo')
    [{'Model': 'dn320', 'MYCT': 400, 'MMIN': 1000, 'MMAX': 3000, 'CACH': 0, 'PRP': 38, 'ERP': 23}, {'Model': 'dn420', 'MYCT': 400, 'MMIN': 512, 'MMAX': 3500, 'CACH': 4, 'PRP': 40, 'ERP': 24}]
    
    >>> machine_vendor_list('machine.csv','wang')
    [{'Model': 'vs-100', 'MYCT': 480, 'MMIN': 512, 'MMAX': 8000, 'CACH': 32, 'PRP': 67, 'ERP': 47}, {'Model': 'vs-90', 'MYCT': 480, 'MMIN': 1000, 'MMAX': 4000, 'CACH': 0, 'PRP': 45, 'ERP': 25}]  
    
    """
    machines = []

    try:
        with open(file_path, 'r', newline='') as file:
            lines = file.readlines()

            if not lines:
                return []
            
            header = lines[0].strip().split(',')
            vendor_index = None
            for i in range(len(header)):
                if header[i].lower() == 'vendor':
                    vendor_index = i
                    break

            if vendor_index is None:
                return []

            for line in lines[1:]:
                values = line.strip().split(',')
                if values[vendor_index].lower() == vendor.lower():
                    machine = {header[i]: int(values[i]) if values[i].isdigit() else values[i] for i in range(len(header)) if i != vendor_index}
                    machines.append(machine)

    except FileNotFoundError:
        return []

    return machines

#==========================================#
# Place your machine_model_list function after this line

def machine_model_list(file_name: str, model: str) -> list[dict]:
    """Extracts a list of machines from a CSV-like file based on the provided machine model.

    Parameters:
        filename (str): The name of the file where the data is stored.
        model (str): The machine model to filter the list.

    Returns:
        list: A list of dictionaries representing machines. Each dictionary contains
        attributes of a machine, with keys as attribute labels (except 'Model').
        Returns an empty list if no machines satisfy the provided model.

    Examples:
        >>> machine_model_list('machine.csv', '32/60')
        [{'Vendor': 'adviser', 'MYCT': 125, 'MMIN': 256, 'MMAX': 6000, 'CACH': 256,
          'PRP': 198, 'ERP':199},
         {another element},
         ...
        ]
    """
    #create list
    machine_list = []
    
    #open file
    with open(file_name, "r") as file:
        
        #get the header
        headers = file.readline().split(",")

        #remove white space from header and check for model
        for i in range(len(headers)):
            headers[i] = headers[i].strip()

        #read the first line
        line = file.readline()
        
        #loop for each line of the file.
        while line != '':
        
            #make sure line is not empty
            if line != '\n':
                
                #split line
                line = line.split(",")

                #create temperary dictionary
                temp_dict = {}

                #check if the model are the same as the specified model
                if model == line[1]:

                    #loop for each header
                    for i in range(len(headers)):

                        #remove white space
                        line[i] = line[i].strip()
                        
                        #make sure
                        if i != 1:

                            try:#try to int casting the line
                                temp_dict[headers[i]] = int(line[i])
                            except:#if not store value as str
                                temp_dict[headers[i]] = line[i]

                    #add new dictionary to list
                    machine_list += [temp_dict]

            #read next line
            line = file.readline()
            
    return machine_list
#==========================================#
# Place your machine_cache_list function after this line

def machine_cache_list(filename: str, cach: int) -> list:
    """
    Filters file based on minimum cache memory

    Parameters:
    - filename must be a string and a valid file name located in the same location as the python code is stored
    - cach must be an integer that relates to one of the CACHE values in the file

    Examples:
    >>>machine_cache_list('machine.csv', 200)
    [{'Vendor': 'adviser', 'Model': '32/60', 'MYCT': 125, 'MMIN': 256, 'MMAX': 6000, 'PRP': 198, 'ERP': 199}, ......]
    >>>machine_cache_list('machine.csv', 800)
    []
    """
    try:
        machines = []
        with open(filename, "r") as mfile:
            lines = mfile.readlines()
            headers = lines[0].strip().split(',')
            column = 0
            for i in range(len(headers)):
                if headers[i] == "CACH":
                    column = i
            for line in lines[1:]:
                values = line.strip().split(',')
                cache_value = int(values[column].replace(',', '')) 
                machine_data = {}
                if cache_value >= cach:
                    for i in range(len(headers)):
                        if i != column:
                            if headers[i] in ['MYCT', 'MMIN', 'MMAX', 'PRP', 'ERP']:
                                machine_data[headers[i]] = int(values[i])
                            else:
                                machine_data[headers[i]] = values[i]
                    machines.append(machine_data)
        return machines
    except FileNotFoundError:
        print(f"'{filename}' does not exist.")


#==========================================#
# Place your machine_prp_list function after this line

def machine_prp_list(file_name, min_prp: int) -> list:
    """Returns list of computers that exceed the minimum published performance
    parameter set.
    
    >>>machine_prp_list('machine.csv', 150)
    {'Vendor': 'adviser', 'Model': '32/60', 'MYCT': 125, 'MMIN': 256,
    'MMAX': 6000, 'CACH': 256, 'ERP':199},
    {another element},
    
    >>>machine_list_prp('machine.csv', 933)
    [{'Vendor': 'amdahl', 'Model': '580-5880', 'MYCT': 23, 'MMIN': 32000, 
    'MMAX': 64000, 'CACH': 128, 'ERP': 1238}, 
    {another element}
    
    >>>machine_list_prp('machine.csv', 483)
    [{'Vendor': 'amdahl', 'Model': '580-5850', 'MYCT': 23, 'MMIN': 16000, 
    'MMAX': 32000, 'CACH': 64, 'ERP': 381},
    {another element}
    
    ...
    """
    machine_list = []

    with open(file_name, 'r') as file:
        header = file.readline().strip().split(',')
        
        for line in file:
            values = line.strip().split(',')
            machine_info = {}

            for i in range(len(header)):
                machine_info[header[i]] = values[i]

            for key in machine_info:
                upper_key = key.upper()
                if upper_key not in ('PRP', 'VENDOR', 'MODEL'):

                    try:
                        machine_info[key] = int(machine_info[key]) if \
                            machine_info[key].isdigit() else machine_info[key]
                        
                    except ValueError:
                        continue
                    
            if 'PRP' in machine_info and int(machine_info['PRP']) >= min_prp:
                del machine_info['PRP']
                machine_list.append(machine_info)
                
    return machine_list


#==========================================#
# Place your load_data function after this line

def load_data(filename: str, pair_of_values: tuple) -> list:
    
    """
    Allows the user to choose the data filtered in a file

    Parameters:
    - filename must be a string and a valid file name located in the same location as the python code is stored
    - pair_of_values must be a tuple with only two values. The first must be a string and either "'Vendor', 'Model', 'CACH', 'PRP', or 'ALL'" in lowercase or uppercase, and the second value must be a filter value represented as an integer

    Examples:
    >>>load_data('machine.csv', ('PRP', 200))
    [{'Vendor': 'amdahl', 'Model': '470v/7', 'MYCT': '29', 'MMIN': '8000', 'MMAX': '32000', 'CACH': '32', 'ERP': '253'}...
    >>>load_data('machine.csv', ('all', 150))
    [{'Vendor': 'adviser', 'Model': '32/60', 'MYCT': 125, 'MMIN': 256, 'MMAX': 6000, 'CACH': 256, 'PRP': 198, 'ERP': '199'}...
    >>>load_data('machine.csv', ('Marco', 1000))
    []
    """
    
      
    if pair_of_values[0].upper() == 'VENDOR':
        return (machine_vendor_list(filename, pair_of_values[1]))
    elif pair_of_values[0].upper() == 'MODEL':
        return (machine_model_list(filename, pair_of_values[1]))
    elif pair_of_values[0].upper() == 'CACH':
        return (machine_cache_list(filename, pair_of_values[1]))
    elif pair_of_values[0].upper() == 'PRP':
        return (machine_prp_list(filename, pair_of_values[1]))
    elif pair_of_values[0].upper() == 'ALL':
        mfile = open(filename, "r")
        lines = mfile.readlines()
        headers = lines[0].strip().split(',')
        machines = []
        for line in lines[1:]:
            values = line.strip().split(',')
            machines.append({headers[i]: values[i] if i < 2 else int(values[i]) for i in range(len(headers))})



        mfile.close()
        return machines    
   
    else:
        print("Not a proper value")
        return[]


#==========================================#
# Place your add_average_main_memory function after this line

def add_average_main_memory(file_path: list) -> list:
    """Return the average of MMIN and MMAX from the selected row.
        Examples
        >>> add_average_main_memory([{'Vendor': 'adviser', 'Model': '32/60', 'MYCT': 125, 'MMIN': 256, 'MMAX': 6000, 'CACH': 256, 'ERP': 199}])
        [{'Vendor': 'adviser', 'Model': '32/60', 'MYCT': 125, 'MMIN': 256, 'MMAX': 6000, 'CACH': 256, 'ERP': 199, 'M_AVG': 3128.0}]
        
        >>> add_average_main_memory([{'Vendor': 'amdahl', 'Model': '580-5880', 'MYCT': 23, 'MMIN': 32000, 'MMAX': 64000, 'CACH': 128, 'ERP': 1238}])
        [{'Vendor': 'amdahl', 'Model': '580-5880', 'MYCT': 23, 'MMIN': 32000, 'MMAX': 64000, 'CACH': 128, 'ERP': 1238, 'M_AVG': 48000.0}]
        
        >>> add_average_main_memory([{'Vendor': 'amdahl', 'Model': '580-5880', 'MYCT': 23, 'MMIN': 32000, 'MMAX': 64000, 'CACH': 128, 'ERP': 1238}])
        [{'Vendor': 'amdahl', 'Model': '580-5880', 'MYCT': 23, 'MMIN': 32000, 'MMAX': 64000, 'CACH': 128, 'ERP': 1238, 'M_AVG': 48000.0}]
        """
    machine_list = []
    for e_dict in file_path:
                
        new_dict = e_dict
        average = 0
                        
        for item1 in e_dict:
            if item1 == 'MMAX' or item1 == 'MMIN':
                average += e_dict[item1]
                                        
        new_dict['M_AVG'] = round(average / 2, 2)
        machine_list.append(new_dict)
                        
    return machine_list
        


# Do NOT include a main script in your submission