def hell(a,*args,**kwargs):
    print (a)
    if(len(args)):
        for item in args:
            print ('args',item)
    if(len(kwargs)):
        print(kwargs)
        for k,v in kwargs.items():
            print(k,v)
#
# l2=['a','d','e','r']
hell(1,2,3,{'e': 'f'},l1=[1,2,3,4],l2=['a','d','e','r'],c={'a':1,'b':2})

