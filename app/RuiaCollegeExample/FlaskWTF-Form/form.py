from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import Form
from wtfforms import TextField
from tf.validators import Required
app = Flask(__name__)
app.config['SECRET_KEY']='hard to guess string'
bootstrap=Bootstrap(app)
class NameForm(Form):
    name = TexrField("What is your name ?",validators= [ Required() ])
@app.route("/",method = ["GET","POST"]
def  index():
    name=None
    form=NameForm()
    if form.validate_on_submit():
        name=formname.data
        form.name.dat
        form.name.dat=""
    return render_template("index.html",form=form,name=name)
if __name__ == "__main__":
    app.run(debug=True)

