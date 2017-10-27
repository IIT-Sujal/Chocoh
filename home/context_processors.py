def is_user_authenticate(request):
	if request.session.has_key('user_id'):
		return { 'user':False }
	else:
		return {'user':True }