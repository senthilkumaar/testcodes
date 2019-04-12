import sys
sys.path.append(r'C:\Users\senthilkumaar.s.HCLTECH\PycharmProjects\untitled')

from reivewques.inheritance import Notebook
#from .hi import ji


#print (ji.sum1())

print(sys.path)
#print(dir())
notes=Notebook()
notes.add('Alice', '<al@kth.se>', 'Lv 24', 'Sthlm')
notes.add('Bob', '<bb@kth.se>', 'Rtb 35', 'Sthlm')

notes.show('Alice')
notes.show('Carol')
print(notes.people)
print(notes.nice)