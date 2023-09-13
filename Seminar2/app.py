from flask import Flask, render_template, request, make_response, redirect

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to My Online Store"

@app.route('/enter', methods=['GET', 'POST'])
def enter():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        
        # Создаем cookie
        response = make_response(redirect('/welcome'))
        response.set_cookie('user_data', f'{name}|{email}')
        
        return response
    
    return render_template('enter.html')

@app.route('/welcome')
def welcome():
    user_data = request.cookies.get('user_data')
    if user_data:
        name, _ = user_data.split('|')
        return render_template('welcome.html', name=name)
    else:
        return redirect('/enter')

@app.route('/logout')
def logout():
    response = make_response(redirect('/enter'))
    response.delete_cookie('user_data')
    return response

if __name__ == '__main__':
    app.run(debug=True)
