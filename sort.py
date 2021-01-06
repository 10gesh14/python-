list = []
num = int(input())

for k in range(num):
	list.append(int(input()))

for i in range (len(list)-1,0,-1):
    for j in range (i):
        if list[j]>list[j+1]:
            list[j],list[j+1] = list[j+1],list[j]
            print(list)

        else:
        	print(list)
        
print( list)
            