alp='abcdefghijklmnopqrstuvwxyz'
key=4
newma=''
massa=input("enter a message:")

for chat in massa:
    posit=alp.find(chat)
    newpos=(posit-key)%26# - use drepted values find
    newch=alp[newpos]
    print("encrpted char",newch)
    newma+=newch

print("the encrpted",newma)    
