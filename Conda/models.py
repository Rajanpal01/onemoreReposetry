from django.db import models

# Create your models here.
class Project_details(models.Model):
    project_name = models.CharField(max_length= 100)
    project_price = models.CharField(max_length=30)
    project_images = models.ImageField(upload_to='images/file')
    project_Files = models.FileField(upload_to='important', null= True)
    server_site = models.CharField(max_length=100)
    Client_Side = models.CharField(max_length=100)
    DataBase = models.CharField(max_length=100)
    project_desc = models.CharField(max_length=150)

    def __str__(self):
        return self.project_name
    
class Projects_ideas(models.Model):
    new_name = models.CharField(max_length=150)

    def __str__(self):
        return self.new_name


class Form_data(models.Model):
    name = models.CharField(max_length=50)
    Mobile = models.CharField(max_length=20)
    Email = models.EmailField()
    password = models.CharField(max_length=30)

    def __str__(self):
        return self.name
    
    @staticmethod
    def get_form_value(Email,password):
        try:
            return Form_data.objects.get(Email = Email, password = password)
        except:
            return False

    def isExist(self):
        if (Form_data.objects.filter(Email= self.Email)):
            return True
        return False

class Documentation(models.Model):
    Docment_word = models.FileField(upload_to='Docu')
    Document_name = models.CharField(max_length=100)
    Document_desc = models.CharField(max_length=300)
    Document_price = models.CharField(max_length=50)


class PPT(models.Model):
    Ppt_word = models.FileField(upload_to='PPT')
    Ppt_name = models.CharField(max_length=100)
    Ppt_desc = models.CharField(max_length=300)
    Ppt_price = models.CharField(max_length=50)

