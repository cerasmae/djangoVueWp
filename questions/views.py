# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views import View
from django.core import serializers
from django.http import HttpResponse

from .models import Question

# Create your views here.
class QuestionView(View):

	def get(self, request):
		data = serializers.serialize("json", Question.objects.all())
		return HttpResponse(data, content_type="application/json")

