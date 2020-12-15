from appone.models import Company, Department, Employee

# department creation
dev = Department(name='Development')
dev.save()
design = Department(name='Design')
design.save()
marketing = Department(name='Marketing')
marketing.save()

# Django company creation
django = Company(name='Django')
django.save()

Employee(company=django, department=design, name='John', age=25, salary=3250.20).save()
Employee(company=django, department=dev, name='Alice', age=33, salary=4400.00).save()

# Pear company creation
pear = Company(name='Pear')
pear.save()

Employee(company=pear, department=marketing, name='Jake', age=46, salary=8000.00).save()
Employee(company=pear, department=dev, name='Sarah', age=21, salary=2800.00).save()

# Requetes SQL associées

# Travail chez Django et nom commence par J
# employees_django = Employee.objects.filter(company__name= "Django", name__startswith="J")

# Ceux qui ne sont pas dans le dep Dev et qui gagnent plus de 4000e/mois
# employees_django = Employee.objects.exclude(department__name='Developpement').filter(salary__gte=4000.00)

# Compter les employés
# Employee.objects.all().count()

# Emmployés de la marque Pear par age decroissant
# Employee.objects.filter(company__name="Pear").order_by('-age')

# Calcul la moyenne des salaires des employés de Django
# from django.db.models import Avg
# Employee.objects.filter(company__name='Django').aggregate(Avg('salary'))
