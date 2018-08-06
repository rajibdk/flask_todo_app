from flask import Flask
from blueprintdemo import tree_mold

app = Flask(__name__)

app.register_blueprint(tree_mold, url_prifix="/oak")
app.register_blueprint(tree_mold, url_prifix="/fir")

if __name__ == "__main__":
    app.run(debug=True)