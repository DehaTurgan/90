from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

class User(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)
    date_of_birth = models.DateField(null=True, blank=True)
    favorite_team = models.CharField(max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email

class QuizQuestion(models.Model):
    question = models.TextField()
    option_a = models.CharField(max_length=255)
    option_b = models.CharField(max_length=255)

    question_tr = models.TextField()
    option_a_tr = models.CharField(max_length=255)
    option_b_tr = models.CharField(max_length=255)

    correct_answer = models.CharField(max_length=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_question(self, lang='en'):
        return self.question_tr if lang == 'tr' else self.question

    def get_option_a(self, lang='en'):
        return self.option_a_tr if lang == 'tr' else self.option_a

    def get_option_b(self, lang='en'):
        return self.option_b_tr if lang == 'tr' else self.option_b

    def __str__(self):
        return self.question[:50] 
