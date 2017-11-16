from home.views import db_init
import hashlib
def is_ceo_authenticate(request):
	db,cur=db_init()
	request.session.set_expiry(7200)
	if request.session.has_key('ceo_id'):
		query="select * from ceo where email_id='%s' and password='%s'"%(request.session['ceo_id'],request.session['ceo_password'])
		cur.execute(query)
		l=cur.fetchall()
		if l:
			return { 'ceo':True }
		else :
			del request.session['ceo_id']
			del request.session['ceo_password']
			return { 'ceo':False}
	else:
		return {'ceo':False }