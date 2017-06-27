from django.db import models

# Create your models here.
class Lesson(models.Model):
    lesson = models.CharField(verbose_name='课程名称', max_length=150)
    def __str__(self):
        return self.lesson


class Homework(models.Model):
    name = models.ForeignKey(Lesson)
    startdate = models.DateField(verbose_name='开始日期')
    submit = models.BooleanField(verbose_name='需要交')
    deadline = models.DateField(verbose_name='截止日期', blank=True, null=True)
    valid = models.BooleanField(verbose_name='作业有效', default=True)
    content = models.TextField(verbose_name='作业内容')
    def __str__(self):
        if len(self.content)<=32:
            content_ = self.content
        else:
            content_ = self.content[:32] + ' ...'
        return '{0} >> {1}'.format(self.name, content_)
