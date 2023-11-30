n=int(input())
mas=list(map(int,input().split()))
q=int(input())
pref=[0]
for i in range(len(mas)):
    pref.append(pref[-1]+mas[i])
for i in range(q):
    l,r=map(int,input().split())
    pref_temp=pref[l-1:r+1]
    dictionary={}
    for i in pref_temp:
        if i in dictionary.keys():
            dictionary[i]+=1
        else:
            dictionary[i]=1
    values=list(dictionary.values())
    res=0
    for i in values:
        res+=i*(i-1)//2
    print(res)
        
