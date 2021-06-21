from flask import Flask,flash,abort,redirect, render_template,request
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename

app = Flask(__name__,'/template/')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'

db=SQLAlchemy(app)
#working= 'C:\\users\user\\AIAMOONSHOT\\templates'
app.config['UPLOAD_FOLDER']='/template/data'
app.config['SECRET_KEY']="randomstring"
class user(db.Model):
    id = db.Column(db.String(10),primary_key=True)
    password = db.Column(db.String(80), unique=True)
    #desc = db.Column(db.String(100))
    def __repr__(self):
        return f"{self.id} - {self.password}"

@app.route('/')
def index():

    return render_template("login.html")

@app.route('/profile')
def profile():
    colours = ['CCBS', 'Welcome call', 'Mystery shopping']
    return render_template("profile.html",colours=colours)


@app.route('/upload', methods = ['POST', 'GET'])
def upload():
        
    #if (colours == "CCBS" and ext=="wav"):
        
        if request.method == 'POST':
            f = request.files['file']   
            ext = f.filename[f.filename.find(".")+1:]
            print(ext)
            if ext == 'jpg':
                flash('No file part')
                return redirect('/profile')
            
            f.save(secure_filename(f.filename))
            return "File saved successfully"

#@app.route('/', methods=['GET'])
#def dropdown():
    
#    return render_template('test.html', colours=colours)            

if __name__ == '__main__':
    app.run(debug=True)