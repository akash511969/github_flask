from flask import *
from github import Github
app = Flask(__name__)

@app.route('/')
def login():
    return render_template ('login.html')



@app.route('/login')

def lo():
	msg="msg"
	try: 
		nm=request.args.get("username")
		password=request.args.get("pass")
		g = Github(nm, password)

		
	except:
		msg = "wrong password"  
	finally:
		user = g.get_user()
		a=user.login
		
		return render_template('success.html',name_html=nm,pass_html=password,a_html=a)

if __name__ == '__main__':
	# app.run()
	# app.debug = True
	app.run(debug = True)
