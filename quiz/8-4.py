n = int(input())
temp=[0]*(n+1)
temp[1]=1
temp[2]=3
for i in range(3,n+1):
    temp[i] = temp[i-1] + 2* temp[i-2]

print(temp[n])