from django.db import models
from cms.models import CMSPlugin

# Create your models here.
class Poll(models.Model):
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __unicode__(self):
        return self.question

class Choice(models.Model):
    poll = models.ForeignKey(Poll)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __unicode__(self):
        return self.choice_text

class PollPluginModel(CMSPlugin):
    poll = models.ForeignKey('polls.Poll', related_name = 'plugins')

    def __unicode__(self):
        return self.poll.question
