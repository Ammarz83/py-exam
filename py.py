# f = []
# f.extend(76,102,124)
# for i in range(len(f)):
#     temp = (i - 32) * 5/9
    
#     print([temp])

 
# def most_frequent(List):
#     counter = 0
#     num = List[0]
     
#     for i in List:
#         curr_frequency = List.count(i)
#         if(curr_frequency > counter):
#             counter = curr_frequency
#             num = i
 
#     return num
 
# List = [3,-1,-1,-1,2,3,-1,3,-1,2,4,9,3]
# print(List.count(-1))

def func1(num):
    return num + 0

num = [4,0,-5,6,-3]
res = [x for x in num if x >= 0]
res2 = [x for x in num if x< 0]
print(res)
print(res2)

