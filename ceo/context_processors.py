def is_ceo_authenticate(request):
	if request.session.has_key('ceo_id'):
		return { 'ceo':False }
	else:
		return {'ceo':True }