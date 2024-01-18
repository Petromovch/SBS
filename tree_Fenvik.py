def p(k):
 return k&(-k)
def pref_sum(mas):
    pref=[0]
    k=0
    for i in range(len(mas)):
        k+=mas[i]
        pref.append(k)
    return pref
def build_tree(pref):
 tree=[0 for i in range(len(mas))]
 for i in range(len(mas)):
  tree[i]=pref[i+1]-pref[i+1-p(i+1)]
 return tree
def Sum_02b(tree,b):
    s=0
    while b>-1:
        s+=tree[b]
        b=b-p(b+1)
    return s
def S(a,b):
    return Sum_02b(tree,b)-Sum_02b(tree,a-1)
def Increase(tree,b,x):
    while b<len(tree):
        tree[b]+=x
        b=b+p(b+1)
    return tree
n=int(input())
mas=list(map(int,input().split()))
tree=build_tree(pref_sum(mas))
print(tree)
q=int(input())
for i in range(q):
    l=int(input())
    for j in range(l):
        a1,b1=(map(int,input().split()))
        Increase(tree,a1-1,b1)
    c1,d1=(map(int,input().split()))
    print(S(c1-1,d1-1))
        

    
