import sys, os
sys.path.append(os.path.abspath("../Lib/site-packages"))
sys.path.append(os.path.abspath("./Lib/site-packages"))

from flask import Flask
from controller.accountctl import account

app = Flask(__name__)
app.register_blueprint(account, url_prefix='/account')

if __name__ == "__main__":
    app.run()