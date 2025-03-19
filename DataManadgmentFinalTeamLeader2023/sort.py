# ECOR 1042 Lab 5 - Team submission
# Remember to include docstring and type annotations for your functions

# Update "" to list all students contributing to the team work
__author__ = "Marco Flores, Kazahchyang Ibrahim, Yasaal Rafi, Amira Khalid"

# Update "" with your team (e.g. T102)
__team__ = "T-046"

#==========================================#
# Place your sort_cache_bubble function after this line

def sort_cache_bubble(arr: list, order: [str]) -> list:
   """ Return a sorted list of machine's dictionaries in descending order
   if input order is "D" and ascending order if input order is "A" using the 
   "CACH" attribute. if "CACH" is not a key in the dictionary, print a message 
   stating the key is not in the dictionary and return original list.
  Preconditions: order == "A" or order == "D"
   
>>> sort_cache_bubble([{"CACH":10,"Model":"GP"},{"CACH":19,"Model":"MS"}], "D")
[{'CACH': 19, 'Model': 'MS'}, {'CACH': 10, 'Model': 'GP'}]

>>> sort_cache_bubble([{"Model":"GP"}, {"Model":"MS"}], "D")
'CACH' key is not present
[{'Model': 'GP'}, {'Model': 'MS'}]

>>> sort_cache_bubble([{"CACH": 50, "Model": "GP"}, {"CACH": 19, "Model": "MS"}, {"CACH": 30, "Model": "GP"}], "A")
[{'CACH': 19, 'Model': 'MS'}, {'CACH': 30, 'Model': 'GP'}, {'CACH': 50, 'Model': 'GP'}]

"""
   swap = True
   while swap:
      swap = False
      if "CACH" in arr or order == "A":
         for i in range(len(arr) - 1):
            if "CACH" in arr[i] and "CACH" in arr[i + 1]:
               if arr[i]["CACH"] > arr[i + 1]["CACH"]:
                  aux = arr[i]
                  arr[i] = arr[i + 1]
                  arr[i + 1] = aux
                  swap = True
            else:
               print('"CACH" is not a present key')
               
      elif "CACH" in arr or order == "D":
         for i in range(len(arr) - 1):
            if "CACH" in arr[i] and "CACH" in arr[i + 1]:
               if arr[i]["CACH"] < arr[i + 1]["CACH"]:
                  aux = arr[i]
                  arr[i] = arr[i + 1]
                  arr[i + 1] = aux
                  swap = True
            else:
               print('"CACH" is not a present key')

      else:
         print('"CACH" is not a present key')
      
   return arr   


#==========================================#
# Place your sort_prp_selection function after this line

def sort_prp_selection (list1: list, order: str) -> list:
   """Return the list in the order of ascending or descending based on the PRP value as requested by user.
    Precondtion: order needs to be 'A' or 'D'
    Examples
    >>>sort_prp_selection([{"PRP":10,"Model":"GP"}, {"PRP":19,"Model":"MS"}], "A")
    [{'PRP': 10, 'Model': 'GP'}, {'PRP': 19, 'Model': 'MS'}]
    
    >>>sort_prp_selection([{"PRP":10,"Model":"GP"}, {"PRP":19,"Model":"MS"}, {"PRP":12,"Model":"FRE"}], "D")
    [{'PRP': 19, 'Model': 'MS'}, {'PRP': 12, 'Model': 'FRE'}, {'PRP': 10, 'Model': 'GP'}]
    
    >>>sort_prp_selection([{"CACH":10,"Model":"GP"}, {"CACH":19,"Model":"MS"}], "D")
    "PRP" key is not present
    [{'CACH': 10, 'Model': 'GP'}, {'CACH': 19, 'Model': 'MS'}]
    """
    
   swap = True
   while swap:
      swap = False
      if "PRP" in list1 or order == "A":
         for i in range(len(list1) - 1):
               if "PRP" in list1[i] and "PRP" in list1[i + 1]:
                  if list1[i]["PRP"] > list1[i + 1]["PRP"]:
                        aux = list1[i]
                        list1[i] = list1[i + 1]
                        list1[i + 1] = aux
                        swap = True
               else:
                  print('"PRP" key is not present')
      elif "PRP" in list1 or order == "D":
         for i in range(len(list1) - 1):
               if "PRP" in list1[i] and "PRP" in list1[i + 1]:
                  if list1[i]["PRP"] < list1[i + 1]["PRP"]:
                        aux = list1[i]
                        list1[i] = list1[i + 1]
                        list1[i + 1] = aux
                        swap = True
               else:
                  print('"PRP" key is not present')
      else:
         print('"PRP" key is not present')

       
   return list1


#==========================================#
# Place your sort_m_avg_insertion function after this line

def sort_m_avg_insertion(data: list[dict[str, float]], order: str) -> list[dict[str, float]]:

   """

   Sort a list of dictionaries based on the 'M_AVG' attribute using the insertion sort algorithm.



   Parameters:

   - data (list[dict[str, float]]): A list of dictionaries containing the 'M_AVG' attribute.

   - order (str): Sorting order, either "A" for ascending or "D" for descending.



   Returns:

   - list[dict[str, float]]: The sorted list of dictionaries based on the 'M_AVG' attribute.



   If 'M_AVG' is not present in any dictionary, a message is printed, and the original list is returned.





   Examples:

   >>>sort_m_avg_insertion( [{"M_AVG":7.2,"Model":"GP"}, {"M_AVG":9.1,"Model":"MS"}], "D")

[{"M_AVG": 9.1, "Model":"MS"}, {"M_AVG":7.2, "Model":"GP"}]



   >>> sort_m_avg_insertion([{"Model":"GP"},{"Model":"MS"}], "D") "M_AVG" key is not present

[{"Model":"GP"}, {"Model":"MS"}]

   """

   if not data or not isinstance(order, str):

      return data



   if order not in ["A", "D"]:

      print("Invalid order. Use 'A' for ascending or 'D' for descending.")

      return data



   for i in range(1, len(data)):

      key_to_insert = data[i]

      j = i - 1



      while j >= 0 and key_to_insert.get("M_AVG", None) is not None:

         if (order == "A" and data[j].get("M_AVG", 0.0) > key_to_insert["M_AVG"]) or (

            order == "D" and data[j].get("M_AVG", 0.0) < key_to_insert["M_AVG"]

         ):

               data[j + 1] = data[j]

               j -= 1

         else:

               break



      data[j + 1] = key_to_insert



   return data

#==========================================#
def sort_myct_bubble(data: list, order: [str]) -> list:

   """
Return the list ordered in ascending or descending based on the MYCT value as requested by user.
Preconditions: order needs to be 'A' or 'D'
Examples:
>>>>sort_myct_bubble([{"MYCT":10,"Model":"GP"},{"MYCT":19,"Model":"MS"}], "D")
[{'MYCT': 10, 'Model': 'GP'}, {'MYCT': 19, 'Model': 'MS'}]
>>>sort_myct_bubble([{"MYCT":200,"Model":"GP"},{"MYCT":190,"Model":"MS"}], "D")
[{'MYCT': 200, 'Model': 'GP'}, {'MYCT': 190, 'Model': 'MS'}]
>>>sort_myct_bubble([{"MYCT":10,"Model":"GP"}, {"MYT":19,"Model":"MS"}], "D")
"MYCT" is not a present key
[{'MYCT': 10, 'Model': 'GP'}, {'MYT': 19, 'Model': 'MS'}]
   """


   swap = True
   while swap:
      swap = False
      if "MYCT" in data or order == "A":
         for i in range(len(data) - 1):
            if "MYCT" in data[i] and "MYCT" in data[i + 1]:
               if data[i]["MYCT"] > data[i + 1]["MYCT"]:
                  aux = data[i]
                  data[i] = data[i + 1]
                  data[i + 1] = aux
                  swap = True
            else:
               print('"MYCT" is not a present key')         
      elif "MYCT" in data or order == "D":
         for i in range(len(data) - 1):
            if "MYCT" in data[i] and "MYCT" in data[i + 1]:
               if data[i]["MYCT"] < data[i + 1]["MYCT"]:
                  aux = data[i]
                  data[i] = data[i + 1]
                  data[i + 1] = aux
                  swap = True
            else:
               print('"MYCT" is not a present key')
      else:
         print('"MYCT" is not a present key')


   return data      
    


#==========================================#
# Place your sort function after this line

def sort(arr: list, order: str, item: str) -> list:
   """ Return the list ordered in the user's request with the given item attribute.
   Precondition: order has to be "A" or "D"
   Example
   >>> sort([{"CACH": 50, "Model": "GP"}, {"CACH": 19, "Model": "MS"}, {"CACH": 30, "Model": "GP"}], "D", "Model")
   Cannot be sorted by "Model"
   
   >>> sort([{"PRP":10,"Model":"GP"}, {"PRP":19,"Model":"MS"}, {"PRP":12,"Model":"FRE"}], "A", "PRP")
   [{'PRP': 10, 'Model': 'GP'}, {'PRP': 12, 'Model': 'FRE'}, {'PRP': 19, 'Model': 'MS'}]
   
   >>> sort([{"CACH": 50, "Model": "GP"}, {"CACH": 19, "Model": "MS"}, {"CACH": 30, "Model": "GP"}], "D", "CACH")
   [{'CACH': 50, 'Model': 'GP'}, {'CACH': 30, 'Model': 'GP'}, {'CACH': 19, 'Model': 'MS'}]
   
   """
   
   list1 = ["CACH", "PRP", "M_AVG", "MYCT"] 
   
   if order == "A": 
      if item == "CACH": 
         return sort_cache_bubble(arr, "A")
      if item == "PRP":
         return sort_prp_selection(arr, "A") 
      if item == "M_AVG":
         return sort_m_avg_insertion(arr, "A") 
      if item == "MYCT":
         return sort_myct_bubble(arr, "A")
      
   if order == "D":   
      if item == "CACH": 
         return sort_cache_bubble(arr, "D")
      if item == "PRP":
         return sort_prp_selection(arr, "D") 
      if item == "M_AVG":
         return sort_m_avg_insertion(arr, "D") 
      if item == "MYCT":
         return sort_myct_bubble(arr, "D")
              
   if item != list1:
      print (f"{'Cannot be sorted by'}", '"' + item +'"')
      return arr

