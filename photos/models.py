from django.db import models

class Category(models.Model):
    id=models.AutoField(primary_key=True)
    name = models.CharField(max_length=25, blank=False)

    def __str__(self):
        return self.name
    
class Session(models.Model):
    id=models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return self.name

def path_file_name(instance, filename):
        if(instance.session):
            return '/'.join(['media', 'Photos', instance.session.name, filename])
        return '/'.join(['media', 'Photos', filename])

class Photo(models.Model):
    id=models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, blank=False)
    session = models.ForeignKey(Session, on_delete=models.PROTECT, blank=True, null=True)
    image = models.ImageField(upload_to=path_file_name)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    date_created = models.DateField()

    def __str__(self):
        return self.name