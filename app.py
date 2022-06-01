import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

def get_defect(defect_id):
    conn = get_db_connection()
    defect = conn.execute('SELECT * FROM defects WHERE id = ?',
                        (defect_id,)).fetchone()
    conn.close()
    if defect is None:
        abort(404)
    return defect

app = Flask(__name__)
app.config['SECRET_KEY'] = 'vegatpafirst'

@app.route('/')
def index():
    conn = get_db_connection()
    defects = conn.execute('SELECT * FROM defects').fetchall()
    conn.close()
    return render_template('index.html', defects=defects)

@app.route('/<int:defect_id>')
def defect(defect_id):
    defect = get_defect(defect_id)
    return render_template('defect.html', defect=defect)

@app.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        equipment = request.form['equipment']
        number = request.form['number']
        description = request.form['description']
        time_start = request.form['time_start']
        user_start = request.form['user_start']

        if not equipment:
            flash('Ввод типа оборудования обязателен')
        elif not number:
            flash('Ввод номера оборудования обязателен')
        elif not description:
            flash('Ввод описания неисправности обязателен')
        elif not time_start:
            flash('Ввод времени начала неисправности обязателен')
        elif not user_start:
            flash('Ввод ФИО регистрирующего неисправность обязателен')
        else:
            conn = get_db_connection()
            conn.execute("INSERT INTO defects (number, equipment, description, user_start) VALUES (?, ?, ?, ?)",
                        (number, equipment, description, user_start)
                        )
            conn.commit()
            conn.close()
            return redirect(url_for('index'))
    return render_template('create.html')

@app.route('/<int:id>/edit', methods=('GET', 'POST'))
def edit(id):
    defect = get_defect(id)

    if request.method == 'POST':
        time_finish = request.form['time_finish']
        fix_descr = request.form['fix_descr']
        repairman = request.form['repairman']

        if not fix_descr:
            flash('Ввод описания устранения неисправности обязателен')
        elif not time_finish:
            flash('Ввод времени устранения неисправности обязателен')
        elif not repairman:
            flash('Ввод ФИО устранившего неисправность обязателен')
        else:
            conn = get_db_connection()
            conn.execute('UPDATE defects SET fix_descr = ?, time_finish = ?, repairman = ?'
                         ' WHERE id = ?',
                         (fix_descr, time_finish, repairman, id))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))

    return render_template('edit.html', defect=defect)
