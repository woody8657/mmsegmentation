import os



if __name__ == '__main__':
    for i in range(26):
        if i+1 < 10:
            os.makedirs(f"./S5_solution/0{i+1}/", exist_ok = True) 
        else:
            os.makedirs(f"./S5_solution/{i+1}/", exist_ok = True) 
    
   