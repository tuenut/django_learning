from django.db import models

# Create your models here.


class Poll(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(max_length=2048)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    __repr__ = __str__


class Respondent(models.Model):
    MALE = 0
    FEMALE = 1
    SEX_CHOICES = [(MALE, 'Мальчик'), (FEMALE, 'Девочка')]

    TEEN = 0
    YOUNG_ADULT = 1
    ADULT = 2
    AGE_CHOICES = [(TEEN, '12-18'), (YOUNG_ADULT, '18-21'), (ADULT, '21+')]

    sex = models.IntegerField(null=False, default=MALE, choices=SEX_CHOICES)
    age = models.IntegerField(null=False, default=TEEN, choices=AGE_CHOICES)
    polls = models.ManyToManyField(Poll)
    registration_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Пол: %s; Возраст: %s' % (dict(self.SEX_CHOICES)[int(self.sex)], dict(self.AGE_CHOICES)[int(self.age)])

    __repr__ = __str__


class Question(models.Model):
    text = models.CharField(max_length=200)
    poll = models.ManyToManyField(Poll)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text

    __repr__ = __str__


class Answer(models.Model):
    text = models.CharField(max_length=200)
    question = models.ManyToManyField(Question)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text

    __repr__ = __str__


class Votes(models.Model):
    votes_count = models.IntegerField(default=0)
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('poll', 'question', 'answer')

