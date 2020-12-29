from django.db import models

# Create your models here
class task(models.Model):
    task_id = models.AutoField
    user_id = models.IntegerField(default=0)
    task_complete = models.IntegerField(default=0)
    task_title = models.CharField(max_length=50)
    task_desc = models.TextField()
    pub_date = models.DateField(auto_now=True)
    
    # add objects = models.Manager() to ignore error
    objects = models.Manager()


    def __str__(self):
        return self.task_title