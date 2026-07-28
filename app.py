from flask import Flask, render_template, request
from yourappdb import query_db, get_db
from flask import g

app = Flask(__name__)
def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()
init_db()

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route("/")
def hello_world():
    user = query_db('select * from contacts')
    the_username = "anonyme"
    one_user = query_db('select * from contacts where first_name = ?',
                [the_username], one=True)
    return render_template("hey.html", users=user, one_user=one_user, the_title="my title")
@app.route("/add_one_job", methods=["GET","POST"])
def add_one_job():

    if request.method == 'POST':

        the_username = "anonyme"
        one_user = query_db("insert into job (name) values (:name)",request.form)
        user = query_db('select * from job')
        return render_template("jobform.html", jobs=user, one_user=one_user, the_title="add new job")
    user = query_db('select * from job')
    one_user = query_db("select * from job limit 1", one=True)
    return render_template("jobform.html", jobs=user, one_user=one_user, the_title="add new job")

@app.route("/add_one_phonecontact", methods=["GET","POST"])
def add_one_phonecontact():

    if request.method == 'POST':

        the_username = "anonyme"
        one_user = query_db("insert into phonecontact (name,phone,email) values (:name,:phone,:email)",request.form)
        user = query_db('select * from phonecontact')
        return render_template("phonecontactform.html", phonecontacts=user, one_user=one_user, the_title="add new phonecontact")
    user = query_db('select * from phonecontact')
    one_user = query_db("select * from phonecontact limit 1", one=True)
    return render_template("phonecontactform.html", phonecontacts=user, one_user=one_user, the_title="add new phonecontact")

@app.route("/add_one_fake_sms", methods=["GET","POST"])
def add_one_fake_sms():

    if request.method == 'POST':

        the_username = "anonyme"
        one_user = query_db("insert into fake_sms (contact1_id,contact2_id,text) values (:contact1_id,:contact2_id,:text)",request.form)
        user = query_db('select * from fake_sms')
        return render_template("fake_smsform.html", fake_smss=user, one_user=one_user, the_title="add new fake_sms")
    user = query_db('select * from fake_sms')
    one_user = query_db("select * from fake_sms limit 1", one=True)
    return render_template("fake_smsform.html", fake_smss=user, one_user=one_user, the_title="add new fake_sms")

@app.route("/add_one_fake_email", methods=["GET","POST"])
def add_one_fake_email():

    if request.method == 'POST':

        the_username = "anonyme"
        one_user = query_db("insert into fake_email (contact1_id,contact2_id,object,text) values (:contact1_id,:contact2_id,:object,:text)",request.form)
        user = query_db('select * from fake_email')
        return render_template("fake_emailform.html", fake_emails=user, one_user=one_user, the_title="add new fake_email")
    user = query_db('select * from fake_email')
    one_user = query_db("select * from fake_email limit 1", one=True)
    return render_template("fake_emailform.html", fake_emails=user, one_user=one_user, the_title="add new fake_email")

@app.route("/add_one_product", methods=["GET","POST"])
def add_one_product():

    if request.method == 'POST':

        the_username = "anonyme"
        one_user = query_db("insert into product (title,description,price,stock) values (:title,:description,:price,:stock)",request.form)
        user = query_db('select * from product')
        return render_template("productform.html", products=user, one_user=one_user, the_title="add new product")
    user = query_db('select * from product')
    one_user = query_db("select * from product limit 1", one=True)
    return render_template("productform.html", products=user, one_user=one_user, the_title="add new product")

@app.route("/add_one_photo", methods=["GET","POST"])
def add_one_photo():

    if request.method == 'POST':

        the_username = "anonyme"
        one_user = query_db("insert into photo (pic,description,location,lat,lon,phonecontact_id) values (:pic,:description,:location,:lat,:lon,:phonecontact_id)",request.form)
        user = query_db('select * from photo')
        return render_template("photoform.html", photos=user, one_user=one_user, the_title="add new photo")
    user = query_db('select * from photo')
    one_user = query_db("select * from photo limit 1", one=True)
    return render_template("photoform.html", photos=user, one_user=one_user, the_title="add new photo")

