from flask import *
import requests
from github import Github
from pprint import pprint
app = Flask(__name__)

@app.errorhandler(401)
def not_found_error(error):
    return 'bad request!', 401


@app.route('/')
def login():
    return render_template ('login.html')



# @app.route('/login')

# def lo():
# 	msg="msg"
# 	try: 
# 		nm=request.args.get("username")
# 		password=request.args.get("pass")
# 		g = Github(nm, password)

		
# 	except:
# 		msg = "wrong password"  
# 	finally:
		# user = g.get_user()
		# a=user.login
		# base_url='https://api.github.com/users/'
		# end_url='/repos'
		# complete_url=base_url+a+end_url
		# response=requests.get(complete_url)
		# x=response.json()
		# pprint(x)
		# z=[]
		# 3for i in x:
		# 	z.append(i["name"])
		# return render_template('success.html',name_html=nm,pass_html=password)
@app.route('/login')

def lo():
	msg="msg"
	try: 
		nm=request.args.get("username")
		password=request.args.get("pass")
		g = Github(nm, password)
	

		
	except:
		flash("Authorization failed.")
		msg = "wrong password"  
	finally:
		user = g.get_user()
		a=user.login
		base_url='https://api.github.com/users/'
		end_url='/repos'
		complete_url=base_url+a+end_url
		response=requests.get(complete_url)
		x=response.json()
		# Avatar url
		v=x[0]['owner']["avatar_url"]
		# Repo namelist
		a=[]
		for i in x:
			a.append(i["name"])
		#repo url
		b=[]
		for i in x:
			b.append("https://github.com/"+i["full_name"])
		#Stars count of repo
		e=[]
		for i in x:
			e.append(i["stargazers_count"])
		#watchers count of repo
		f=[]
		for i in x:
			f.append(i["watchers_count"])
		#forks count of repo
		g=[]
		for i in x:
			g.append(i["forks"])
		c=a+b+e+f+g

		# return render_template('success.html',len=len(a),a=a,len_b=len(b),b=b,name_html=nm,pass_html=password,a_html=a,avatar_html=v)
		return render_template('success.html',len=len(c),c=c,name_html=nm,pass_html=password,a_html=a,avatar_html=v)


if __name__ == '__main__':
	# app.run()
	# app.debug = True
	app.run(debug = True)
