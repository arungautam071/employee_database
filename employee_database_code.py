#django model database code for Employee-Department-Project relationship

from django.db import models



class Department(models.Model):
    D_number = models.IntegerField(max_length=30)
    D_name = models.CharField(max_length=30)
    D_location = models.CharField()

    

class Employee(models.Model):
    e_name = models.CharField(max_length=20)
    e_gender = models.CharField(max_length=10)
    e_dob = models.DateTimeField()
    e_doj = models.DateTimeField()
    e_adder = models.CharField(max_length=100)
    e_department= models.ForeignKey(Department, on_delete=models.CASCADE)


#M2M relation between employee and project.
class Project(models.Model):
    p_number = models.IntegerField(max_length=30)
    p_name = models.CharField(max_length=30)
    p_location = models.CharField()
    p_department= models.ForeignKey(Department, on_delete=models.CASCADE)
    p_employee =models.ManyToManyField(Employee)    

   
