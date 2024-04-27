#Импорт
from flask import Flask, render_template,request, redirect
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
#sqlite and sqlalchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///diary.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class feedbacktable(db.Model):
    #userid
    id = db.Column(db.Integer, primary_key=True)
    #user topic
    email = db.Column(db.String(50), nullable=False)
    #user feedback
    text = db.Column(db.Text, nullable=False)
    def __repr__(self):
            return f'<feedback {self.id}>'


#Запуск страницы с контентом
@app.route('/')
def index():
    return render_template('index.html')


#Динамичные скиллы
@app.route('/', methods=['POST'])
def process_form_python():
    button_python = request.form.get('button_python')
    button_discord = request.form.get('button_discord')
    button_db = request.form.get('button_db')
    button_html = request.form.get('button_html')
    return render_template('index.html', 
                           button_python=button_python,
                           button_discord=button_discord,
                           button_db=button_db,
                           button_html=button_html)

@app.route('/sent', methods=['GET','POST'])
def reg():
    if request.method == 'POST':
        email= request.form['email']
        text = request.form['text']
        
        #Задание №3. Реализовать запись пользователей
        feedback = feedbacktable(email=email, text=text)

        db.session.add(feedback)
        db.session.commit()        
        return redirect('/')
    
    else:    
        return render_template('index.html')
