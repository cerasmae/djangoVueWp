# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.contrib.staticfiles.templatetags.staticfiles import static

def cover_upload_path(instance, filename):
	return './covers/cover_{}'.format(instance.pk, filename)

# Create your models here.
class Question(models.Model):
	COLOR_CHOICES = (
		('Red', '#F44336'),
		('Orange', '#FF9800'),
		('Yellow', '#FFEB3B'),
		('Green', '#4CAF50'),
		('Blue', '#2196F3'),
		('Indigo', '#3F51B5'),
		('Violet', '#9C27B0'),
		('Pink', '#E91E63'),
		('Brown', '#795548'),
		('Grey', '#9E9E9E'),
		('Black', '#000000'),
		('White', '#FFFFFF'),
	)
	question = models.CharField(max_length=255, blank=False)
	description = models.TextField(blank=True)
	cover = models.FileField(upload_to=cover_upload_path, blank=True)
	color = models.CharField(choices=COLOR_CHOICES, default='White', max_length=10)

	# @property
	# def cover_url(self):
	# 	if self.cover:
	# 		return self.cover.url
	# 	return static('img/default_cover.png')

	def __str__(self):
		return self.question
	