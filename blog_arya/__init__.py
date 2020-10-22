from  flask import Flask,render_template,redirect,url_for
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
db=SQLAlchemy(app)
app.config['SECRET_KEY']='12345'
app.config['SQLALCHEMY_DATABASE_URI']="postgresql://postgres:1234@localhost:5432/Fieldofficer"

# app.config['MAIL_SERVER']="smtp.googlemail.com"
# app.config['MAIL_PORT']=587
# app.config['MAIL_USE_TLS']='True'
# app.config['MAIL_USERNAME']='siddharth24092001@gmail.com'
# app.config['MAIL_PASSWORD']='siddharth@1234'
# mail=Mail(app)
# mail.init_app(app)
#
# login_manager=LoginManager(app)
# login_manager.login_view="Login"
# login_manager.login_message_category="info"

from blog_arya import routes