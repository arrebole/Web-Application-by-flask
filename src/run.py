import sys
sys.path.append("../Lib/site-packages")
sys.path.append("./Lib/site-packages")

from flask import Flask, redirect, render_template
from controller import account, archive, search

app = Flask(
    __name__, 
    static_folder="../theme", 
    static_url_path="/",
    template_folder="../theme"
)

# register router
app.register_blueprint(account, url_prefix='/api/account')
app.register_blueprint(archive, url_prefix='/api/archive')
app.register_blueprint(search, url_prefix='/api/search')

# home page
@app.route("/")
def home():
    return render_template('index.html')

# error redirect to home
@app.errorhandler(404)
def notFind(error):
    return redirect("/")


if __name__ == "__main__":
    app.run(debug = True)