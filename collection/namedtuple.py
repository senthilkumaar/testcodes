from collections import namedtuple
employee = namedtuple('employee' , ['name','age','designation', 'salary'])
raj = employee(name='raj',age='27',designation= 'SSE', salary=12000)
# megha = employee(name='Megha', age='26', designation= 'Analyst',salary= 16000)
# for p in [raj, megha]:
#     print('{} is name. {}is age. {} is designation. {} is salary '.format(*p))


books = namedtuple('books', 'name subject price')
physics = books(name='theory of relativity' ,subject='physics' ,price='350')
physics= books(name='law of gravity', subject='physics',price='330')
for p in [physics]:
    print('{} {} {}'.format(*p))
    print('*******************************')

print(physics._fields)
physics._replace(price='450')

print(physics._replace(price='450'))

for p in [physics]:
    print('{} {} {}'.format(*p))




karen= {'name':'Karen', 'age': '27', 'designation' : 'TA', 'salary': '14000' }
print(employee(**karen))

print(raj)
print(raj._asdict())
Jack=['jack', '27', 'TL','19000']
print(employee._make(Jack))