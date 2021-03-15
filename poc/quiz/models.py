from django.db import models
from django.core.validators import URLValidator

# Create your models here.
class Program(models.Model):
    program_name = models.CharField(max_length=200)
    key = models.CharField(max_length=10)
    description = models.TextField()
    site = models.CharField(max_length=200)

    class Meta():
        ordering = ['key',]

    def __str__(self):
        return self.program_name

class Result(models.Model):
    time = models.DateTimeField()
    one = models.ForeignKey(Program, on_delete=models.CASCADE, related_name='one')
    two = models.ForeignKey(Program, on_delete=models.CASCADE, related_name='two')
    three = models.ForeignKey(Program, on_delete=models.CASCADE, related_name='three')
    four = models.ForeignKey(Program, on_delete=models.CASCADE, related_name='four')
    five = models.ForeignKey(Program, on_delete=models.CASCADE, related_name='five')
    six = models.ForeignKey(Program, on_delete=models.CASCADE, related_name='six')
    seven = models.ForeignKey(Program, on_delete=models.CASCADE, related_name='seven')
    eight = models.ForeignKey(Program, on_delete=models.CASCADE, related_name='eight')
    nine = models.ForeignKey(Program, on_delete=models.CASCADE, related_name='nine')
    ten = models.ForeignKey(Program, on_delete=models.CASCADE, related_name='ten')
    eleven = models.ForeignKey(Program, on_delete=models.CASCADE, related_name='eleven')
    twelve = models.ForeignKey(Program, on_delete=models.CASCADE, related_name='twelve')
    thirteen = models.ForeignKey(Program, on_delete=models.CASCADE, related_name='thirteen')
    fourteen = models.ForeignKey(Program, on_delete=models.CASCADE, related_name='fourteen')
    fifteen = models.ForeignKey(Program, on_delete=models.CASCADE, related_name='fifteen')

    def __str__(self):
        return (
            '1) ' + self.one.program_name +
            ' 2) ' + self.two.program_name +
            ' 3) ' + self.three.program_name +
            ' 4) ' + self.four.program_name +
            ' 5) ' + self.five.program_name +
            ' 6) ' + self.six.program_name +
            ' 7) ' + self.seven.program_name +
            ' 8) ' + self.eight.program_name +
            ' 9) ' + self.nine.program_name +
            ' 10) ' + self.ten.program_name +
            ' 11) ' + self.eleven.program_name +
            ' 12) ' + self.twelve.program_name +
            ' 13) ' + self.thirteen.program_name +
            ' 14) ' + self.fourteen.program_name +
            ' 15) ' + self.fifteen.program_name 
        )

class Course(models.Model):
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    course_type = models.CharField(max_length=5)
    course = models.TextField()
    def __str__(self):
        return self.course

class Career(models.Model):
    career_type = models.CharField(max_length=200)
    career = models.TextField()
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    def __str__(self):
        return self.career

class Comparison(models.Model):
    id = models.AutoField(primary_key=True)
    program_1 = models.ForeignKey(Program, on_delete=models.CASCADE,related_name='program')
    program_2 = models.ForeignKey(Program, on_delete=models.CASCADE,related_name='compare_to')
    comparison = models.TextField()
    def __str__(self):
        return str(self.program_1.program_name)+" vs. "+str(self.program_2.program_name)+" : "+str(self.comparison)

class Chart(models.Model):
    url = models.models.TextField(validators=[URLValidator()])
    width = models.IntegerField(default=400)
    height = models.IntegerField(default=400)
    chart_type = models.CharField(max_length=10)
    title = models.CharField(max_length=200)
    order = models.IntegerField(default=999)

    class Meta():
        ordering = ['order',]

    def __str__(self):
        return self.title
