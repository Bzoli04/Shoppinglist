from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Alap bevásárlólista
shopping_list = []

@app.route('/')
def home():
    return render_template('index.html', shopping_list=shopping_list)

@app.route('/add', methods=['POST'])
def add_item():
    item = request.form.get('item')
    if item:
        shopping_list.append(item)
    return redirect(url_for('home'))

@app.route('/delete/<item>')
def delete_item(item):
    if item in shopping_list:
        shopping_list.remove(item)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)

