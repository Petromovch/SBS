g,s,b,t=map(int,input().split())
if t<g:
    print("gold")
if s>t>g:
    print("silver")
if b>t>s:
    print("bronze")
if t>b:
    print("none")

