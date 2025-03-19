# ECOR 1042 Lab 4 - team submission

#import check module here

#import load_data module here

# Update "" with your the name of the active members of the team
__author__ = "Marco Flores, Kazahchyang Ibrahim, Yasaal Rafi, Amira Khalid"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-046"

#==========================================#

# Place test_return_list function here 
def test_return_list():
            
            
            result = load_data.machine_vendor_list('machine-test.csv', 'amdahl')
            check.equal(isinstance(result, list), True)
            
            result = load_data.machine_vendor_list('machine-test.csv', 'apollo')
            check.equal(isinstance(result, list), True)
            
            result = load_data.machine_vendor_list('machine-test.csv', 'bti')
            check.equal(isinstance(result, list), True)
            
            
            result = load_data.machine_model_list('machine-test.csv', 'amdahl')
            check.equal(isinstance(result, list), True)
            
            result = load_data.machine_model_list('machine-test.csv', 'apollo')
            check.equal(isinstance(result, list), True)
            
            result = load_data.machine_model_list('machine-test.csv', 'bti')
            check.equal(isinstance(result, list), True)

            
            result = load_data.machine_cache_list('machine-test.csv', 32)
            check.equal(isinstance(result, list), True)
            
            result = load_data.machine_cache_list('machine-test.csv', 0)
            check.equal(isinstance(result, list), True)
            
            result = load_data.machine_cache_list('machine-test.csv', 0)
            check.equal(isinstance(result, list), True)
            
            
            result = load_data.machine_prp_list('machine-test.csv', 269)
            check.equal(isinstance(result, list), True)
            
            result = load_data.machine_prp_list('machine-test.csv', 38)
            check.equal(isinstance(result, list), True)
            
            result = load_data.machine_prp_list('machine-test.csv', 10)
            check.equal(isinstance(result, list), True)  
            
            
            result = load_data.add_average_main_memory([{'Vendor': 'amdahl', 'Model': '470v/7', 'MYCT': 29, 'MMIN': 8000, 'MMAX': 32000, 'CACH': 32, 'ERP': 253}])
            check.equal(isinstance(result, list), True)
            result = load_data.add_average_main_memory([{'Vendor': 'amdahl', 'Model': '470v/7', 'MYCT': 29, 'MMIN': 8000, 'MMAX': 32000, 'CACH': 32, 'ERP': 253}])
            check.equal(isinstance(result, list), True)
            
            result = load_data.add_average_main_memory([{'Vendor': 'bti', 'Model': '5000', 'MYCT': 350, 'MMIN': 64, 'MMAX': 64, 'CACH': 0, 'ERP': 15}])
            check.equal(isinstance(result, list), True)     
            

            result = load_data.load_data('machine-test.csv', ('PRP',269))
            check.equal(isinstance(result, list), True)
            
            result = load_data.load_data('machine-test.csv', ('CACH', 128))
            check.equal(isinstance(result, list), True)
            
            result = load_data.load_data('machine-test.csv', ('PRP', 76))
            check.equal(isinstance(result, list), True)
            
            result = load_data.load_data('machine-test.csv', ('PRP', 150))
            check.equal(isinstance(result, list), True)
            
            result = load_data.load_data('machine-test.csv', ('CACH', 0))
            check.equal(isinstance(result, list), True)
            
            result = load_data.load_data('machine-test.csv', ('PRP', 10))
            check.equal(isinstance(result, list), True)        

            check.summary()



# Place test_return_list_correct_lenght function here

def test_return_list_correct_lenght():

            result = load_data.machine_vendor_list('machine-test.csv', 'amdahl')

            check.equal(len(result), 9)

           

            result = load_data.machine_vendor_list('machine-test.csv', 'burroughs')

            check.equal(len(result), 8)

           

            result = load_data.machine_vendor_list('machine-test.csv', 'basf')

            check.equal(len(result), 2)

           

           

            result = load_data.machine_model_list('machine-test.csv', '470v/7')
            check.equal(len(result), 1)

           

            result = load_data.machine_model_list('machine-test.csv', '580-5840')

            check.equal(len(result), 4)

           

            result = load_data.machine_model_list('machine-test.csv', 'Three39')

            check.equal(len(result), 0)



           

            result = load_data.machine_cache_list('machine-test.csv', 32)

            check.equal(len(result), 12)

           

            result = load_data.machine_cache_list('machine-test.csv', 65)

            check.equal(len(result), 4)

           

            result = load_data.machine_cache_list('machine-test.csv', 64)

            check.equal(len(result), 8)

           

           

            result = load_data.machine_prp_list('machine-test.csv', 150)

            check.equal(len(result), 8)

           

            result = load_data.machine_prp_list('machine-test.csv', 200)

            check.equal(len(result), 7)

           

            result = load_data.machine_prp_list('machine-test.csv', 100)

            check.equal(len(result), 11)  

           

           

            result = load_data.add_average_main_memory([{'Vendor': 'amdahl', 'Model': '470v/b', 'MYCT': 26, 'MMIN': 8000, 'MMAX': 32000, 'CACH': 64, 'ERP': 290}])

            check.equal(len(result), 1)

           

            result = load_data.add_average_main_memory([])

            check.equal(len(result), 0)

           

            result = load_data.add_average_main_memory([{'Vendor': 'burroughs', 'Model': 'b6925', 'MYCT': 110, 'MMIN': 3100, 'MMAX': 6200, 'CACH': 0, 'ERP': 45}])

            check.equal(len(result), 1)     

           



            result = load_data.load_data('machine-test.csv', ('MYCT',20))

            check.equal(len(result), 0)

           

            result = load_data.load_data('machine-test.csv', ('CACH',32))

            check.equal(len(result), 12)

           

            result = load_data.load_data('machine-test.csv', ('PRP', 300))

            check.equal(len(result), 5)

           

            result = load_data.load_data('machine-test.csv', ('MYCT', 23))

            check.equal(len(result), 0)

           

            result = load_data.load_data('machine-test.csv', ('CACH', 0))

            check.equal(len(result), 22)
   
           

            result = load_data.load_data('machine-test.csv', ('MYCT', 143))

            check.equal(len(result), 0)            

           

           

           
            check.summary()
   

#Place test_return_correct_dict_inside_list function here

def test_return_correct_dict_inside_list():
            #3 tests for machine_vendor_list
            check.equal(load_data.machine_vendor_list('machine-test.csv', 'amdahl'), [{'Model': '470v/7', 'MYCT': 29, 'MMIN': 8000, 'MMAX': 32000, 'CACH': 32, 'PRP': 269, 'ERP': 253}, {'Model': '470v/7a', 'MYCT': 29, 'MMIN': 8000, 'MMAX': 32000, 'CACH': 32, 'PRP': 220, 'ERP': 253}, {'Model': '470v/7b', 'MYCT': 29, 'MMIN': 8000, 'MMAX': 32000, 'CACH': 32, 'PRP': 172, 'ERP': 253}, {'Model': '470v/7c', 'MYCT': 29, 'MMIN': 8000, 'MMAX': 16000, 'CACH': 32, 'PRP': 132, 'ERP': 132}, {'Model': '470v/b', 'MYCT': 26, 'MMIN': 8000, 'MMAX': 32000, 'CACH': 64, 'PRP': 318, 'ERP': 290}, {'Model': '580-5840', 'MYCT': 23, 'MMIN': 16000, 'MMAX': 32000, 'CACH': 64, 'PRP': 367, 'ERP': 381}, {'Model': '580-5840', 'MYCT': 23, 'MMIN': 16000, 'MMAX': 32000, 'CACH': 64, 'PRP': 489, 'ERP': 381}, {'Model': '580-5840', 'MYCT': 23, 'MMIN': 16000, 'MMAX': 64000, 'CACH': 64, 'PRP': 636, 'ERP': 749}, {'Model': '580-5840', 'MYCT': 23, 'MMIN': 32000, 'MMAX': 64000, 'CACH': 128, 'PRP': 1144, 'ERP': 1238}])
            check.equal(load_data.machine_vendor_list('machine-test.csv', 'apollo'), [{'Model': 'dn320', 'MYCT': 400, 'MMIN': 1000, 'MMAX': 3000, 'CACH': 0, 'PRP': 38, 'ERP': 23}])
            check.equal(load_data.machine_vendor_list('machine-test.csv', 'burroughs'), [{'Model': 'b1955', 'MYCT': 167, 'MMIN': 524, 'MMAX': 2000, 'CACH': 8, 'PRP': 19, 'ERP': 23}, {'Model': 'b2900', 'MYCT': 143, 'MMIN': 512, 'MMAX': 5000, 'CACH': 0, 'PRP': 28, 'ERP': 29}, {'Model': 'b2925', 'MYCT': 143, 'MMIN': 1000, 'MMAX': 2000, 'CACH': 0, 'PRP': 31, 'ERP': 22}, {'Model': 'b4955', 'MYCT': 110, 'MMIN': 5000, 'MMAX': 5000, 'CACH': 142, 'PRP': 120, 'ERP': 124}, {'Model': 'b5900', 'MYCT': 143, 'MMIN': 1500, 'MMAX': 6300, 'CACH': 0, 'PRP': 30, 'ERP': 35}, {'Model': 'b5920', 'MYCT': 143, 'MMIN': 3100, 'MMAX': 6200, 'CACH': 0, 'PRP': 33, 'ERP': 39}, {'Model': 'b6900', 'MYCT': 143, 'MMIN': 2300, 'MMAX': 6200, 'CACH': 0, 'PRP': 61, 'ERP': 40}, {'Model': 'b6925', 'MYCT': 110, 'MMIN': 3100, 'MMAX': 6200, 'CACH': 0, 'PRP': 76, 'ERP': 45}])
    
            #3 tests for machine_model_list
            check.equal(load_data.machine_model_list('machine-test.csv', '470v/7'), [{'Vendor': 'amdahl', 'MYCT': 29, 'MMIN': 8000, 'MMAX': 32000, 'CACH': 32, 'PRP': 269, 'ERP': 253}])
            check.equal(load_data.machine_model_list('machine-test.csv', 'dn320'), [{'Vendor': 'apollo', 'MYCT': 400, 'MMIN': 1000, 'MMAX': 3000, 'CACH': 0, 'PRP': 38, 'ERP': 23}])
            check.equal(load_data.machine_model_list('machine-test.csv', 'b6925'), [{'Vendor': 'burroughs', 'MYCT': 110, 'MMIN': 3100, 'MMAX': 6200, 'CACH': 0, 'PRP': 76, 'ERP': 45}])
    
            #3 tests for machine_cache_list
            check.equal(load_data.machine_cache_list('machine-test.csv', 32), [{'Vendor': 'amdahl', 'Model': '470v/7', 'MYCT': 29, 'MMIN': 8000, 'MMAX': 32000, 'PRP': 269, 'ERP': 253}, {'Vendor': 'amdahl', 'Model': '470v/7a', 'MYCT': 29, 'MMIN': 8000, 'MMAX': 32000, 'PRP': 220, 'ERP': 253}, {'Vendor': 'amdahl', 'Model': '470v/7b', 'MYCT': 29, 'MMIN': 8000, 'MMAX': 32000, 'PRP': 172, 'ERP': 253}, {'Vendor': 'amdahl', 'Model': '470v/7c', 'MYCT': 29, 'MMIN': 8000, 'MMAX': 16000, 'PRP': 132, 'ERP': 132}, {'Vendor': 'amdahl', 'Model': '470v/b', 'MYCT': 26, 'MMIN': 8000, 'MMAX': 32000, 'PRP': 318, 'ERP': 290}, {'Vendor': 'amdahl', 'Model': '580-5840', 'MYCT': 23, 'MMIN': 16000, 'MMAX': 32000, 'PRP': 367, 'ERP': 381}, {'Vendor': 'amdahl', 'Model': '580-5840', 'MYCT': 23, 'MMIN': 16000, 'MMAX': 32000, 'PRP': 489, 'ERP': 381}, {'Vendor': 'amdahl', 'Model': '580-5840', 'MYCT': 23, 'MMIN': 16000, 'MMAX': 64000, 'PRP': 636, 'ERP': 749}, {'Vendor': 'amdahl', 'Model': '580-5840', 'MYCT': 23, 'MMIN': 32000, 'MMAX': 64000, 'PRP': 1144, 'ERP': 1238}, {'Vendor': 'basf', 'Model': 'Jul-65', 'MYCT': 60, 'MMIN': 2000, 'MMAX': 8000, 'PRP': 92, 'ERP': 70}, {'Vendor': 'basf', 'Model': 'Jul-68', 'MYCT': 50, 'MMIN': 4000, 'MMAX': 16000, 'PRP': 138, 'ERP': 117}, {'Vendor': 'burroughs', 'Model': 'b4955', 'MYCT': 110, 'MMIN': 5000, 'MMAX': 5000, 'PRP': 120, 'ERP': 124}])
            check.equal(load_data.machine_cache_list('machine-test.csv', 128), [{'Vendor': 'amdahl', 'Model': '580-5840', 'MYCT': 23, 'MMIN': 32000, 'MMAX': 64000, 'PRP': 1144, 'ERP': 1238}, {'Vendor': 'burroughs', 'Model': 'b4955', 'MYCT': 110, 'MMIN': 5000, 'MMAX': 5000, 'PRP': 120, 'ERP': 124}])
            check.equal(load_data.machine_cache_list('machine-test.csv', 0), [{'Vendor': 'amdahl', 'Model': '470v/7', 'MYCT': 29, 'MMIN': 8000, 'MMAX': 32000, 'PRP': 269, 'ERP': 253}, {'Vendor': 'amdahl', 'Model': '470v/7a', 'MYCT': 29, 'MMIN': 8000, 'MMAX': 32000, 'PRP': 220, 'ERP': 253}, {'Vendor': 'amdahl', 'Model': '470v/7b', 'MYCT': 29, 'MMIN': 8000, 'MMAX': 32000, 'PRP': 172, 'ERP': 253}, {'Vendor': 'amdahl', 'Model': '470v/7c', 'MYCT': 29, 'MMIN': 8000, 'MMAX': 16000, 'PRP': 132, 'ERP': 132}, {'Vendor': 'amdahl', 'Model': '470v/b', 'MYCT': 26, 'MMIN': 8000, 'MMAX': 32000, 'PRP': 318, 'ERP': 290}, {'Vendor': 'amdahl', 'Model': '580-5840', 'MYCT': 23, 'MMIN': 16000, 'MMAX': 32000, 'PRP': 367, 'ERP': 381}, {'Vendor': 'amdahl', 'Model': '580-5840', 'MYCT': 23, 'MMIN': 16000, 'MMAX': 32000, 'PRP': 489, 'ERP': 381}, {'Vendor': 'amdahl', 'Model': '580-5840', 'MYCT': 23, 'MMIN': 16000, 'MMAX': 64000, 'PRP': 636, 'ERP': 749}, {'Vendor': 'amdahl', 'Model': '580-5840', 'MYCT': 23, 'MMIN': 32000, 'MMAX': 64000, 'PRP': 1144, 'ERP': 1238}, {'Vendor': 'apollo', 'Model': 'dn320', 'MYCT': 400, 'MMIN': 1000, 'MMAX': 3000, 'PRP': 38, 'ERP': 23}, {'Vendor': 'basf', 'Model': 'Jul-65', 'MYCT': 60, 'MMIN': 2000, 'MMAX': 8000, 'PRP': 92, 'ERP': 70}, {'Vendor': 'basf', 'Model': 'Jul-68', 'MYCT': 50, 'MMIN': 4000, 'MMAX': 16000, 'PRP': 138, 'ERP': 117}, {'Vendor': 'bti', 'Model': '5000', 'MYCT': 350, 'MMIN': 64, 'MMAX': 64, 'PRP': 10, 'ERP': 15}, {'Vendor': 'bti', 'Model': '8000', 'MYCT': 200, 'MMIN': 512, 'MMAX': 16000, 'PRP': 35, 'ERP': 64}, {'Vendor': 'burroughs', 'Model': 'b1955', 'MYCT': 167, 'MMIN': 524, 'MMAX': 2000, 'PRP': 19, 'ERP': 23}, {'Vendor': 'burroughs', 'Model': 'b2900', 'MYCT': 143, 'MMIN': 512, 'MMAX': 5000, 'PRP': 28, 'ERP': 29}, {'Vendor': 'burroughs', 'Model': 'b2925', 'MYCT': 143, 'MMIN': 1000, 'MMAX': 2000, 'PRP': 31, 'ERP': 22}, {'Vendor': 'burroughs', 'Model': 'b4955', 'MYCT': 110, 'MMIN': 5000, 'MMAX': 5000, 'PRP': 120, 'ERP': 124}, {'Vendor': 'burroughs', 'Model': 'b5900', 'MYCT': 143, 'MMIN': 1500, 'MMAX': 6300, 'PRP': 30, 'ERP': 35}, {'Vendor': 'burroughs', 'Model': 'b5920', 'MYCT': 143, 'MMIN': 3100, 'MMAX': 6200, 'PRP': 33, 'ERP': 39}, {'Vendor': 'burroughs', 'Model': 'b6900', 'MYCT': 143, 'MMIN': 2300, 'MMAX': 6200, 'PRP': 61, 'ERP': 40}, {'Vendor': 'burroughs', 'Model': 'b6925', 'MYCT': 110, 'MMIN': 3100, 'MMAX': 6200, 'PRP': 76, 'ERP': 45}])
    
            #3 tests for machine_prp_list
            check.equal(load_data.machine_prp_list('machine-test.csv', 269), [{'Vendor': 'amdahl', 'Model': '470v/7', 'MYCT': 29, 'MMIN': 8000, 'MMAX': 32000, 'CACH': 32, 'ERP': 253}, {'Vendor': 'amdahl', 'Model': '470v/b', 'MYCT': 26, 'MMIN': 8000, 'MMAX': 32000, 'CACH': 64, 'ERP': 290}, {'Vendor': 'amdahl', 'Model': '580-5840', 'MYCT': 23, 'MMIN': 16000, 'MMAX': 32000, 'CACH': 64, 'ERP': 381}, {'Vendor': 'amdahl', 'Model': '580-5840', 'MYCT': 23, 'MMIN': 16000, 'MMAX': 32000, 'CACH': 64, 'ERP': 381}, {'Vendor': 'amdahl', 'Model': '580-5840', 'MYCT': 23, 'MMIN': 16000, 'MMAX': 64000, 'CACH': 64, 'ERP': 749}, {'Vendor': 'amdahl', 'Model': '580-5840', 'MYCT': 23, 'MMIN': 32000, 'MMAX': 64000, 'CACH': 128, 'ERP': 1238}])
            check.equal(load_data.machine_prp_list('machine-test.csv', 10),[{'Vendor': 'amdahl', 'Model': '470v/7', 'MYCT': 29, 'MMIN': 8000, 'MMAX': 32000, 'CACH': 32, 'ERP': 253}, {'Vendor': 'amdahl', 'Model': '470v/7a', 'MYCT': 29, 'MMIN': 8000, 'MMAX': 32000, 'CACH': 32, 'ERP': 253}, {'Vendor': 'amdahl', 'Model': '470v/7b', 'MYCT': 29, 'MMIN': 8000, 'MMAX': 32000, 'CACH': 32, 'ERP': 253}, {'Vendor': 'amdahl', 'Model': '470v/7c', 'MYCT': 29, 'MMIN': 8000, 'MMAX': 16000, 'CACH': 32, 'ERP': 132}, {'Vendor': 'amdahl', 'Model': '470v/b', 'MYCT': 26, 'MMIN': 8000, 'MMAX': 32000, 'CACH': 64, 'ERP': 290}, {'Vendor': 'amdahl', 'Model': '580-5840', 'MYCT': 23, 'MMIN': 16000, 'MMAX': 32000, 'CACH': 64, 'ERP': 381}, {'Vendor': 'amdahl', 'Model': '580-5840', 'MYCT': 23, 'MMIN': 16000, 'MMAX': 32000, 'CACH': 64, 'ERP': 381}, {'Vendor': 'amdahl', 'Model': '580-5840', 'MYCT': 23, 'MMIN': 16000, 'MMAX': 64000, 'CACH': 64, 'ERP': 749}, {'Vendor': 'amdahl', 'Model': '580-5840', 'MYCT': 23, 'MMIN': 32000, 'MMAX': 64000, 'CACH': 128, 'ERP': 1238}, {'Vendor': 'apollo', 'Model': 'dn320', 'MYCT': 400, 'MMIN': 1000, 'MMAX': 3000, 'CACH': 0, 'ERP': 23}, {'Vendor': 'basf', 'Model': 'Jul-65', 'MYCT': 60, 'MMIN': 2000, 'MMAX': 8000, 'CACH': 65, 'ERP': 70}, {'Vendor': 'basf', 'Model': 'Jul-68', 'MYCT': 50, 'MMIN': 4000, 'MMAX': 16000, 'CACH': 65, 'ERP': 117}, {'Vendor': 'bti', 'Model': '5000', 'MYCT': 350, 'MMIN': 64, 'MMAX': 64, 'CACH': 0, 'ERP': 15}, {'Vendor': 'bti', 'Model': '8000', 'MYCT': 200, 'MMIN': 512, 'MMAX': 16000, 'CACH': 0, 'ERP': 64}, {'Vendor': 'burroughs', 'Model': 'b1955', 'MYCT': 167, 'MMIN': 524, 'MMAX': 2000, 'CACH': 8, 'ERP': 23}, {'Vendor': 'burroughs', 'Model': 'b2900', 'MYCT': 143, 'MMIN': 512, 'MMAX': 5000, 'CACH': 0, 'ERP': 29}, {'Vendor': 'burroughs', 'Model': 'b2925', 'MYCT': 143, 'MMIN': 1000, 'MMAX': 2000, 'CACH': 0, 'ERP': 22}, {'Vendor': 'burroughs', 'Model': 'b4955', 'MYCT': 110, 'MMIN': 5000, 'MMAX': 5000, 'CACH': 142, 'ERP': 124}, {'Vendor': 'burroughs', 'Model': 'b5900', 'MYCT': 143, 'MMIN': 1500, 'MMAX': 6300, 'CACH': 0, 'ERP': 35}, {'Vendor': 'burroughs', 'Model': 'b5920', 'MYCT': 143, 'MMIN': 3100, 'MMAX': 6200, 'CACH': 0, 'ERP': 39}, {'Vendor': 'burroughs', 'Model': 'b6900', 'MYCT': 143, 'MMIN': 2300, 'MMAX': 6200, 'CACH': 0, 'ERP': 40}, {'Vendor': 'burroughs', 'Model': 'b6925', 'MYCT': 110, 'MMIN': 3100, 'MMAX': 6200, 'CACH': 0, 'ERP': 45}])
            check.equal(load_data.machine_prp_list('machine-test.csv', 76), [{'Vendor': 'amdahl', 'Model': '470v/7', 'MYCT': 29, 'MMIN': 8000, 'MMAX': 32000, 'CACH': 32, 'ERP': 253}, {'Vendor': 'amdahl', 'Model': '470v/7a', 'MYCT': 29, 'MMIN': 8000, 'MMAX': 32000, 'CACH': 32, 'ERP': 253}, {'Vendor': 'amdahl', 'Model': '470v/7b', 'MYCT': 29, 'MMIN': 8000, 'MMAX': 32000, 'CACH': 32, 'ERP': 253}, {'Vendor': 'amdahl', 'Model': '470v/7c', 'MYCT': 29, 'MMIN': 8000, 'MMAX': 16000, 'CACH': 32, 'ERP': 132}, {'Vendor': 'amdahl', 'Model': '470v/b', 'MYCT': 26, 'MMIN': 8000, 'MMAX': 32000, 'CACH': 64, 'ERP': 290}, {'Vendor': 'amdahl', 'Model': '580-5840', 'MYCT': 23, 'MMIN': 16000, 'MMAX': 32000, 'CACH': 64, 'ERP': 381}, {'Vendor': 'amdahl', 'Model': '580-5840', 'MYCT': 23, 'MMIN': 16000, 'MMAX': 32000, 'CACH': 64, 'ERP': 381}, {'Vendor': 'amdahl', 'Model': '580-5840', 'MYCT': 23, 'MMIN': 16000, 'MMAX': 64000, 'CACH': 64, 'ERP': 749}, {'Vendor': 'amdahl', 'Model': '580-5840', 'MYCT': 23, 'MMIN': 32000, 'MMAX': 64000, 'CACH': 128, 'ERP': 1238}, {'Vendor': 'basf', 'Model': 'Jul-65', 'MYCT': 60, 'MMIN': 2000, 'MMAX': 8000, 'CACH': 65, 'ERP': 70}, {'Vendor': 'basf', 'Model': 'Jul-68', 'MYCT': 50, 'MMIN': 4000, 'MMAX': 16000, 'CACH': 65, 'ERP': 117}, {'Vendor': 'burroughs', 'Model': 'b4955', 'MYCT': 110, 'MMIN': 5000, 'MMAX': 5000, 'CACH': 142, 'ERP': 124}, {'Vendor': 'burroughs', 'Model': 'b6925', 'MYCT': 110, 'MMIN': 3100, 'MMAX': 6200, 'CACH': 0, 'ERP': 45}])

            #3 tests for add_average_main_memory
            check.equal(load_data.add_average_main_memory([{'Vendor': 'adviser', 'Model': '470v/7', 'MYCT': 29, 'MMIN': 8000, 'MMAX': 32000, 'CACH': 32, 'ERP': 253}]), [{'Vendor': 'adviser', 'Model': '470v/7', 'MYCT': 29, 'MMIN': 8000, 'MMAX': 32000, 'CACH': 32, 'ERP': 253, 'M_AVG': 20000.0}])
            check.equal(load_data.add_average_main_memory([{'Vendor': 'adviser', 'Model': '32/60', 'MYCT': 125, 'MMIN': 256, 'MMAX': 6000, 'CACH': 256, 'ERP': 199}]), [{'Vendor': 'adviser', 'Model': '32/60', 'MYCT': 125, 'MMIN': 256, 'MMAX': 6000, 'CACH': 256, 'ERP': 199, 'M_AVG': 3128.0}])
            check.equal(load_data.add_average_main_memory([{'Vendor': 'burroughs', 'Model': 'b6925', 'MYCT': 110, 'MMIN': 3100, 'MMAX': 6200, 'CACH': 0, 'ERP': 45}]), [{'Vendor': 'burroughs', 'Model': 'b6925', 'MYCT': 110, 'MMIN': 3100, 'MMAX': 6200, 'CACH': 0, 'ERP': 45, 'M_AVG': 4650.0}])

            #6 tests for load_data
            check.equal((load_data.load_data('machine-test.csv', ('PRP', 269))), [{'Vendor': 'amdahl', 'Model': '470v/7', 'MYCT': 29, 'MMIN': 8000, 'MMAX': 32000, 'CACH': 32, 'ERP': 253}, {'Vendor': 'amdahl', 'Model': '470v/b', 'MYCT': 26, 'MMIN': 8000, 'MMAX': 32000, 'CACH': 64, 'ERP': 290}, {'Vendor': 'amdahl', 'Model': '580-5840', 'MYCT': 23, 'MMIN': 16000, 'MMAX': 32000, 'CACH': 64, 'ERP': 381}, {'Vendor': 'amdahl', 'Model': '580-5840', 'MYCT': 23, 'MMIN': 16000, 'MMAX': 32000, 'CACH': 64, 'ERP': 381}, {'Vendor': 'amdahl', 'Model': '580-5840', 'MYCT': 23, 'MMIN': 16000, 'MMAX': 64000, 'CACH': 64, 'ERP': 749}, {'Vendor': 'amdahl', 'Model': '580-5840', 'MYCT': 23, 'MMIN': 32000, 'MMAX': 64000, 'CACH': 128, 'ERP': 1238}])
            check.equal((load_data.load_data('machine-test.csv', ('Vendor', 'apollo'))), [{'Model': 'dn320', 'MYCT': 400, 'MMIN': 1000, 'MMAX': 3000, 'CACH': 0, 'PRP': 38, 'ERP': 23}])
            check.equal((load_data.load_data('machine-test.csv', ('Model', '470v/b'))), [{'Vendor': 'amdahl', 'MYCT': 26, 'MMIN': 8000, 'MMAX': 32000, 'CACH': 64, 'PRP': 318, 'ERP': 290}])
            check.equal((load_data.load_data('machine-test.csv', ('cach', 8))), [{'Vendor': 'amdahl', 'Model': '470v/7', 'MYCT': 29, 'MMIN': 8000, 'MMAX': 32000, 'PRP': 269, 'ERP': 253}, {'Vendor': 'amdahl', 'Model': '470v/7a', 'MYCT': 29, 'MMIN': 8000, 'MMAX': 32000, 'PRP': 220, 'ERP': 253}, {'Vendor': 'amdahl', 'Model': '470v/7b', 'MYCT': 29, 'MMIN': 8000, 'MMAX': 32000, 'PRP': 172, 'ERP': 253}, {'Vendor': 'amdahl', 'Model': '470v/7c', 'MYCT': 29, 'MMIN': 8000, 'MMAX': 16000, 'PRP': 132, 'ERP': 132}, {'Vendor': 'amdahl', 'Model': '470v/b', 'MYCT': 26, 'MMIN': 8000, 'MMAX': 32000, 'PRP': 318, 'ERP': 290}, {'Vendor': 'amdahl', 'Model': '580-5840', 'MYCT': 23, 'MMIN': 16000, 'MMAX': 32000, 'PRP': 367, 'ERP': 381}, {'Vendor': 'amdahl', 'Model': '580-5840', 'MYCT': 23, 'MMIN': 16000, 'MMAX': 32000, 'PRP': 489, 'ERP': 381}, {'Vendor': 'amdahl', 'Model': '580-5840', 'MYCT': 23, 'MMIN': 16000, 'MMAX': 64000, 'PRP': 636, 'ERP': 749}, {'Vendor': 'amdahl', 'Model': '580-5840', 'MYCT': 23, 'MMIN': 32000, 'MMAX': 64000, 'PRP': 1144, 'ERP': 1238}, {'Vendor': 'basf', 'Model': 'Jul-65', 'MYCT': 60, 'MMIN': 2000, 'MMAX': 8000, 'PRP': 92, 'ERP': 70}, {'Vendor': 'basf', 'Model': 'Jul-68', 'MYCT': 50, 'MMIN': 4000, 'MMAX': 16000, 'PRP': 138, 'ERP': 117}, {'Vendor': 'burroughs', 'Model': 'b1955', 'MYCT': 167, 'MMIN': 524, 'MMAX': 2000, 'PRP': 19, 'ERP': 23}, {'Vendor': 'burroughs', 'Model': 'b4955', 'MYCT': 110, 'MMIN': 5000, 'MMAX': 5000, 'PRP': 120, 'ERP': 124}])
            check.equal((load_data.load_data('machine-test.csv', ('Model', '470v/b'))), [{'Vendor': 'amdahl', 'MYCT': 26, 'MMIN': 8000, 'MMAX': 32000, 'CACH': 64, 'PRP': 318, 'ERP': 290}])
            check.equal((load_data.load_data('machine-test.csv', ('all', 150))), [{'Vendor': 'amdahl', 'Model': '470v/7', 'MYCT': 29, 'MMIN': 8000, 'MMAX': 32000, 'CACH': 32, 'PRP': 269, 'ERP': 253}, {'Vendor': 'amdahl', 'Model': '470v/7a', 'MYCT': 29, 'MMIN': 8000, 'MMAX': 32000, 'CACH': 32, 'PRP': 220, 'ERP': 253}, {'Vendor': 'amdahl', 'Model': '470v/7b', 'MYCT': 29, 'MMIN': 8000, 'MMAX': 32000, 'CACH': 32, 'PRP': 172, 'ERP': 253}, {'Vendor': 'amdahl', 'Model': '470v/7c', 'MYCT': 29, 'MMIN': 8000, 'MMAX': 16000, 'CACH': 32, 'PRP': 132, 'ERP': 132}, {'Vendor': 'amdahl', 'Model': '470v/b', 'MYCT': 26, 'MMIN': 8000, 'MMAX': 32000, 'CACH': 64, 'PRP': 318, 'ERP': 290}, {'Vendor': 'amdahl', 'Model': '580-5840', 'MYCT': 23, 'MMIN': 16000, 'MMAX': 32000, 'CACH': 64, 'PRP': 367, 'ERP': 381}, {'Vendor': 'amdahl', 'Model': '580-5840', 'MYCT': 23, 'MMIN': 16000, 'MMAX': 32000, 'CACH': 64, 'PRP': 489, 'ERP': 381}, {'Vendor': 'amdahl', 'Model': '580-5840', 'MYCT': 23, 'MMIN': 16000, 'MMAX': 64000, 'CACH': 64, 'PRP': 636, 'ERP': 749}, {'Vendor': 'amdahl', 'Model': '580-5840', 'MYCT': 23, 'MMIN': 32000, 'MMAX': 64000, 'CACH': 128, 'PRP': 1144, 'ERP': 1238}, {'Vendor': 'apollo', 'Model': 'dn320', 'MYCT': 400, 'MMIN': 1000, 'MMAX': 3000, 'CACH': 0, 'PRP': 38, 'ERP': 23}, {'Vendor': 'basf', 'Model': 'Jul-65', 'MYCT': 60, 'MMIN': 2000, 'MMAX': 8000, 'CACH': 65, 'PRP': 92, 'ERP': 70}, {'Vendor': 'basf', 'Model': 'Jul-68', 'MYCT': 50, 'MMIN': 4000, 'MMAX': 16000, 'CACH': 65, 'PRP': 138, 'ERP': 117}, {'Vendor': 'bti', 'Model': '5000', 'MYCT': 350, 'MMIN': 64, 'MMAX': 64, 'CACH': 0, 'PRP': 10, 'ERP': 15}, {'Vendor': 'bti', 'Model': '8000', 'MYCT': 200, 'MMIN': 512, 'MMAX': 16000, 'CACH': 0, 'PRP': 35, 'ERP': 64}, {'Vendor': 'burroughs', 'Model': 'b1955', 'MYCT': 167, 'MMIN': 524, 'MMAX': 2000, 'CACH': 8, 'PRP': 19, 'ERP': 23}, {'Vendor': 'burroughs', 'Model': 'b2900', 'MYCT': 143, 'MMIN': 512, 'MMAX': 5000, 'CACH': 0, 'PRP': 28, 'ERP': 29}, {'Vendor': 'burroughs', 'Model': 'b2925', 'MYCT': 143, 'MMIN': 1000, 'MMAX': 2000, 'CACH': 0, 'PRP': 31, 'ERP': 22}, {'Vendor': 'burroughs', 'Model': 'b4955', 'MYCT': 110, 'MMIN': 5000, 'MMAX': 5000, 'CACH': 142, 'PRP': 120, 'ERP': 124}, {'Vendor': 'burroughs', 'Model': 'b5900', 'MYCT': 143, 'MMIN': 1500, 'MMAX': 6300, 'CACH': 0, 'PRP': 30, 'ERP': 35}, {'Vendor': 'burroughs', 'Model': 'b5920', 'MYCT': 143, 'MMIN': 3100, 'MMAX': 6200, 'CACH': 0, 'PRP': 33, 'ERP': 39}, {'Vendor': 'burroughs', 'Model': 'b6900', 'MYCT': 143, 'MMIN': 2300, 'MMAX': 6200, 'CACH': 0, 'PRP': 61, 'ERP': 40}, {'Vendor': 'burroughs', 'Model': 'b6925', 'MYCT': 110, 'MMIN': 3100, 'MMAX': 6200, 'CACH': 0, 'PRP': 76, 'ERP': 45}])
            
            #Recieve summary
            check.summary()



#Place test_add_average function here

def test_add_average():
    
            machine = load_data.load_data("machine-test.csv", ('Vendor', 'amdahl'))
            len_machine = len(machine[0])
            average = load_data.add_average_main_memory(machine)
            check.equal(len(machine), len(average))
            check.equal(len_machine + 1, len(average[0]))
            check.equal(average[0]['M_AVG'], 20000.0)
    
            machine = load_data.load_data("machine-test.csv", ('Model', '470v/7'))
            len_machine = len(machine[0])
            average = load_data.add_average_main_memory(machine)
            check.equal(len(machine), len(average))
            check.equal(len_machine + 1, len(average[0]))
            check.equal(average[0]['M_AVG'], 20000.0)
    
            machine = load_data.load_data("machine-test.csv", ('PRP', 269))
            len_machine = len(machine[0])
            average = load_data.add_average_main_memory(machine)
            check.equal(len(machine), len(average))
            check.equal(len_machine + 1, len(average[0]))
            check.equal(average[0]['M_AVG'], 20000.0)
    
            machine = load_data.load_data("machine-test.csv", ('CACH', 32))
            len_machine = len(machine[0])
            average = load_data.add_average_main_memory(machine)
            check.equal(len(machine), len(average))
            check.equal(len_machine + 1, len(average[0]))
            check.equal(average[0]['M_AVG'], 20000.0)
    
            machine = load_data.load_data("machine-test.csv", ('ALL', 32))
            len_machine = len(machine[0])
            average = load_data.add_average_main_memory(machine)
            check.equal(len(machine), len(average))
            check.equal(len_machine + 1, len(average[0]))
            check.equal(average[0]['M_AVG'], 20000.0)


# Do NOT include a main script in your submission
