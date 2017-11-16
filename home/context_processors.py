
from home.views import db_init
import hashlib

def is_user_authenticate(request):
	db,cur=db_init()
	request.session.set_expiry(7200)
	if request.session.has_key('user_id'):
		query="select * from user where user_id='%s' and password='%s'"%(request.session['user_id'],request.session['password'])
		cur.execute(query)
		l=cur.fetchall()
		if l:
			return { 'user':False }
		else :
			del request.session['user_id']
			del request.session['password']
			return { 'user':True}
	else:
		return {'ceo':True}