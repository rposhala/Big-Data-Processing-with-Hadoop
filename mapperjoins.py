import sys
#c =0
for line in sys.stdin:
    #c+=1
    #print(c)
    ## defining variables which guides us to columns of final table 
    employee_id = '_'
    name = '_'
    salary = '_'
    country = '_'
    passcode = '_'
    # splitting the data and storing it in a list
    data = line.strip().split("\t")
    #print(data)
    if len(data) == 2 and '-' in  data[0]:
        employee_id = data[0]
        name = data[1]
    elif len(data) >= 4 and '-' in data[0] :
        employee_id = data[0]
        salary = data[1][1:]+','+data[2][:-1]
        if data[3] == data[-2]:
            country = data[3]
        else :
            country = data[3][1:]+','+data[-2][:-1]
        passcode = data[-1]
    print('%s\t%s\t%s\t%s\t%s'%(employee_id,name,salary,country,passcode))
    
