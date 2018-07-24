with open('/home/cf-celine/Desktop/djangoVueWp/src/data/posts.json') as f:
	ques = json.load(f)
	f.close()

Question.objects.bulk_create([Question(question=q['question'], description=q['description']) for q in ques])