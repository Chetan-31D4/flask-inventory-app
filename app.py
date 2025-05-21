from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)
DATABASE = 'inventory.db'

# DB helper
def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def dashboard():
    conn = get_db()
    products = conn.execute('SELECT * FROM products').fetchall()
    conn.close()
    return render_template('dashboard.html', products=products)

@app.route('/add', methods=['POST'])
def add_product():
    name = request.form['name']
    quantity = request.form['quantity']
    conn = get_db()
    conn.execute('INSERT INTO products (name, quantity) VALUES (?, ?)', (name, quantity))
    conn.commit()
    conn.close()
    return redirect(url_for('dashboard'))

@app.route('/delete/<int:id>', methods=['POST'])
def delete_product(id):
    conn = get_db()
    conn.execute('DELETE FROM products WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('dashboard'))

@app.route('/edit/<int:id>', methods=['POST'])
def edit_product(id):
    name = request.form['name']
    quantity = request.form['quantity']
    conn = get_db()
    conn.execute('UPDATE products SET name = ?, quantity = ? WHERE id = ?', (name, quantity, id))
    conn.commit()
    conn.close()
    return redirect(url_for(    'dashboard'))


if __name__ == '__main__':
    app.run(debug=True)