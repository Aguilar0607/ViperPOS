from config.wsgi import *
from core.erp.models import Type, Employee
# Create your tests here.

#  Listar

#  select * from tabla

# query = Type.objects.all()
# print(query)

# # insert
# t = Type(name='Chanchito').save()
# t.name = 'Emmanuel'
# t.save()

# edit
# try:
#     t = Type.objects.get(id=1)
#     t.name = 'AccionistaEmmanuel'
#     t.save()
# except Exception as e:
#     print(e)


# Delete
# t = Type.objects.get(pk=4)
# t.delete()

# obj = Type.objects.filter(name__icontains='pre')
# obj = Type.objects.filter(name__icontains='terry').query

# e = Employee.objects.filter(name__endswith='l')
# print(e)

# for i in Type.objects.filter(name__endswith='l'):
#     print(i.name)