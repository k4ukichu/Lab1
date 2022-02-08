from functools import wraps
from pickle import TRUE
from flask import session


def login_required(f):
    @wraps(f)
    def wrap(*args,**kwargs):
        if 'logged_in'in session:
            return f(*args, **kwargs)
             else:
                flash('Please sign up or sing in to access the books')
                return redirect(url_for('login'))
        return wrap 

        @app.route('/')
        @login_required
        def home():
            error=None 
            if request.method =='POST':
             if request.form['search'] !='test':
                error ='search Invalid'
            else:
                    return redirect(url_for('Books'))
                    return render_template('.html, error=error')
                    @app.route('/Welcome')
                    def Welcome():
                     return render_template('homepage.html')
                     @app.route('/Login, methods=['GET, 'POST]')
                     def login():
                         error=None
                         if request.method=='POST':
                            if request.form['username']!='test' or request.form['password']!='test':
                                error = 'Credentials not found'
                            else:
                                session['Logged in']=TRUE
                                flash("Sign In Successfull")
                                return redirect(url_for('home'))
                                return render_template('Signin.html',error=error)

@app.route('signout')
def signout():
    session.pop('Signed in',None)
    flash("Successfully Signed out from World of Books")
    return redirect(url_for('homepage'))


@app.route("/search", methods=["GET","POST"])
@login_required
def search():
    if request.method=="POST":
        return render_template("search.html")
        if request.method=="GET":
            return render_template("search.html")

@app.route("/booksearch", methods=["GET","POST"])
@login_required
def booksearch():
    searchtype=request.args.get("searchtype")
    searchtext=request.args.get("searchtext")

    if searchtext=='year':
        command = 