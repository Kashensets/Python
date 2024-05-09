h = int(input ("Ievadi eglītes augstumu!"))
if h > 0:
    for i in range (1, h + 1):
        print(" " * (h -i) + "*" * (2*i -1))
else:
    print("Augstumam jābūt pozitīvam skaitlim")
    
 #             for in range (1, h+1):
#    if i < h:
#        print(" "*10+"*"*6)






#height = int(input ("Ievadiet eglītes augstumu: "))
#if height > 0:
#    for i in range(1, height + 1):
#        print(" " * (height - i) + "*" * (2*i - 1))
#else:
#    print("Augstumam jābūt pozitīvam skaitlim.")
