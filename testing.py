import puzzle as pz

temp = [] 
for i in range(0,20):
    temp1 = pz.initialState(8)
    if temp1 not in temp:
        temp.append(temp1)
        print(temp1)