from flask import Flask, render_template, request, send_from_directory
from flask_bootstrap import Bootstrap
from logic.Person import Person
from logic.Document import Document
from logic.ado import ADO


app = Flask(__name__)
bootstrap = Bootstrap(app)
list_packages = list()
aut_code = 0


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html', title="Home")


@app.route('/person', methods=['GET'])
def person():
    return render_template('person.html')


@app.route('/person_detail', methods=['POST'])
def person_detail():
    ado = ADO()
    op = request.form['op']
    id_person = request.form['id_person']
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    nationality = request.form['nationality']
    if op == 'I':
        sql = "INSERT INTO person (idperson, name, last_name, nationality) VALUES (%s, %s, %s, %s)"
        values = (int(id_person), first_name, last_name, nationality)
        data = ado.dml(sql=sql, val=values, op='I')
    elif op == 'U':
        sql = 'UPDATE person SET name={0}{2}{0}, last_name={0}{3}{0}, ' \
              'nationality={0}{4}{0}  WHERE idperson={1}'.format('"', int(id_person), first_name, last_name,
                                                                 nationality)
        data = ado.dml(sql=sql, op='U')
    return render_template('person_detail.html', value=data)


@app.route('/people')
def people():
    ado = ADO()
    data = ado.query("SELECT idperson, name, last_name, nationality FROM gestion_spe.person")
    return render_template('people.html', value=data)


@app.route('/address')
def document():
    ado = ADO()
    data = ado.query("SELECT id, title, pages, category, author FROM gestion_spe.document")
    return render_template('document.html', value=data)


@app.route('/Document_add', methods=['GET'])
def document_add():
    return render_template('Document_add.html')


@app.route('/document_update/<id_person>', methods=['GET'])
def document_update(id_person):
    return render_template('document_update.html', id_person=id)


@app.route('/person_delete/<id_person>', methods=['GET'])
def document_delete(id_person):
    ado = ADO()
    sql = 'DELETE FROM document WHERE id={0}'.format(int(id_person))
    data = ado.dml(sql=sql, op='D')
    return render_template('Document_detail.html', value=data)


@app.route('/Document_detail', methods=['GET'])
def document_detail():
    ado = ADO()
    id = request.form['id']
    title = request.form['title']
    pages = request.form['pages']
    category = request.form['category']
    author = request.form['author']
    sql = "INSERT INTO address (id, title, pages, category, author) " \
          "VALUES (%s, %s, %s, %s, %s)"
    values = (int(id), str(title, pages, category, author))
    data = ado.dml(sql=sql, val=values, op='I')
    return render_template('Document_detail.html', data=data)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


if __name__ == '__main__':
    app.run(debug=False)