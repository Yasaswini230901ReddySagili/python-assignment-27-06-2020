file1 = open('myfile.txt', 'w') 
file1.writelines(L) 
file1.close()  
file1 = open('myfile.txt', 'r') 
count = 0 
for line in file1: 
    count += 1
    print("Line{}: {}".format(count, line.strip())) 
file1.close() 