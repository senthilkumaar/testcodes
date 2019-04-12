with open (r'C:\Users\senthilkumaar.s.HCLTECH\PycharmProjects\untitled\commontest\filehandling\read.txt',"r+") as f:
    filedetail=f.readline().split(" ")
    finallist={}
    for item in set(filedetail):
        k=item
        v=int(filedetail.count(item))
        finallist.update({k:v})
    print(finallist)
    maximum=(max(finallist.values()))
    for key, value in finallist.items():
        if maximum == value:
            print (key, value)
