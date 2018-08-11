from flask import Flask

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://krgqluvk:WeWUqNxgoXxFJ0rGLuuaot4Hc1avUp6g@pellefant-02.db.elephantsql.com:5432/krgqluvk'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False