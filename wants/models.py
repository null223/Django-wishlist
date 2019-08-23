from django.db import models
from django.utils import timezone

# Create your models here.
class Genre(models.Model):
	name = models.CharField('欲しいものジャンル', max_length=15)
	created_at = models.DateTimeField('日付', default=timezone.now)

	def __str__(self):
		return self.name

class Wish(models.Model):
	title = models.CharField('欲しいもの', max_length=30)
	when_buy = models.CharField('いつ買うか', max_length=10)
	hm = models.IntegerField()
	genre = models.ForeignKey(
		Genre, verbose_name='欲しいものジャンル', on_delete=models.PROTECT,
	)
	created_at = models.DateTimeField('日付', default=timezone.now)

	def __str__(self):
		return '{0} {1} {2}'.format(self.title, self.when_buy, self.genre)