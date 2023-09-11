from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('base.html')

@app.route('/category/clothing')
def clothing():
    return render_template('categories/clothing.html')

@app.route('/category/shoes')
def shoes():
    return render_template('categories/shoes.html')

@app.route('/product/jacket')
def jacket():
    return render_template('products/jacket.html')

if __name__ == '__main__':
    app.run()
