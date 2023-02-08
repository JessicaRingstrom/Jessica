n1 = int(input("write 'a number:"))
n2 = int(input("write another one:"))
n3 = int(input("another one:"))
n4 = int(input("last number:"))
if n1>=n2 and n1>=n3 and n1<=n4:
    print("näst störst tal är" + str(n1))
elif n1>=n2 and n1<=n3 and n1>=n4:
    print("näst störst tal är" + str(n1))
elif n1<=n2 and n1>=n3 and n1>=n4:
    print("näst störst tal är" + str(n1))
elif n2>=n1 and n2>=n3 and n2<=n4:
    print("näst störst tal är" + str(n2))
elif n2>=n1 and n2<=n3 and n2>=n4:
    print("näst störst tal är" + str(n2))
elif n2<=n1 and n2>=n3 and n2>=n4:
    print("näst störst tal är" + str(n2))
elif n3>=n1 and n3>=n2 and n3<=n4:
    print("näst störst tal är" + str(n3))
elif n3>=n1 and n3<=n2 and n3>=n4:
    print("näst störst tal är" + str(n3))
elif n3>=n1 and n3<=n2 and n3>=n4:
    print("näst störst tal är" + str(n3))
elif n4>=n1 and n4>=n2 and n4<=n3:
    print("näst störst tal är" + str(n4))
elif n4>=n1 and n4<=n2 and n4>=n3:
    print("näst störst tal är" + str(n4))
elif n4<=n1 and n4>=n2 and n4>=n3:
    print("näst störst tal är" + str(n4))
