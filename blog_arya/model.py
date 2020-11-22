
# from blog_arya import db
# from datetime import datetime
# from blog_arya import login_manager
# from flask_login import UserMixin
#
# @login_manager.user_loader
# def load_user(id):
#     return Fieldofficer.query.get(id)
#
#
# class Fieldofficer(db.Model,UserMixin):
#     id=db.Column(db.Integer,primary_key=True)
#     name=db.Column(db.String(50),nullable=False,unique=True)
#     email = db.Column(db.String(120), nullable=False, unique=True)
#     subject = db.Column(db.String(100), nullable=False, unique=True)
#     message = db.Column(db.String(200), nullable=False, unique=True)
#
#
#     def __repr__(self):
#         return f"Fieldofficer('{self.email}','{self.hr_no}','{self.name}'"