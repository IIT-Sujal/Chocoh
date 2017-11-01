def is_ceo_authenticate(request):
	request.session.set_expiry(7200)
	if request.session.has_key('ceo_id'):
		return { 'ceo':True }
	else:
		return {'ceo':False }