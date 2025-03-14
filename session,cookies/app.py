from flask import Flask,request,render_template,session,make_response,Request,flash
app = Flask(__name__,static_url_path='/')
app.secret_key = 'SOME KEY'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/set_data')
def set_data():
    session['name'] = 'Tanish'
    session['other'] = 'Some other data'
    
    return render_template('index.html',message='Session data set')


@app.route('/get_data')
def get_data():
    name = session.get('name')
    other = session.get('other')
    
    return render_template('index.html',message=f'Name: {name}, Other: {other}')

@app.route('/clear_session')
def clear_session():
    session.clear()
    return render_template('index.html',message='Session cleared')


@app.route('/set_cookie')
def set_cookie():
    response = make_response(render_template('index.html',message='Cookie set'))
    response.set_cookie('cookie_name','cookie_value')
    return response

@app.route('/get_cookie')
def get_cookie():
    cookie_value = request.cookies['cookie_name']
    return render_template('index.html',message=f"cookie value: {cookie_value}")
    
@app.route('/remove_cookie')
def remove_cookie():
    response = make_response(render_template('index.html',message='Cookie removed'))
    response.set_cookie('cookie_name',expires=0)
    return response

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        
        username = request.form.get('username')
        password = request.form.get('password')
        if username=='Tanish' and password=='12345':
            flash('Login successful')
            return render_template('index.html', message='')
        else:
            flash('login failed')
            return render_template('index.html', message='')
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5555,debug=True)