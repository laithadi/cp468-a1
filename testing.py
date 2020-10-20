import puzzle as pz

t = [[6,13,7,10],[8,9,11,0],[15,2,12,5],[14,3,1,4]]
f =  [[3,9,1,15],[14,11,4,6],[13,0,10,12],[2,7,8,5]]
t1 = [[1,8,2],[0,4,3],[7,6,5]]

# print(pz.actions(t1))

# print(pz.is_puzzle_solvable(t))

# temp = []
# for i in range(0, 20):
#     temp1 = pz.initialState(8)
#     if temp1 not in temp:
#         print(i)
#         print(temp1)
#         temp.append(temp1)

g_s = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 0]
        ]

# print(pz.h1(t1, g_s))
# print(pz.h2(t1, g_s))
# print(pz.h3(t1, g_s))

print(pz.aStar(t1, g_s, 'h3'))

# dic = {}

# dic[9999] = 'hi'

# print(dic)
# print(len(dic))

# del dic[9999]

# print(dic)

# # print(len(dic))

# diction = {9:[9,3], 3:[2,3], 4:[9,2,1]}

# temp = sorted(diction.keys())

# curr_state = diction[temp[0]]

# print(temp)
# print(curr_state)