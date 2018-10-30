from flask import Flask, render_template
app = Flask(__name__)
@app.route("/index")
def index() :
user = {"username": " Daneil"}
posts=[
{  
     "author" : {"username": "Daneil"},
     "body" : "Beautiful day in Srilanka!"

},
{  
"author" : {"username": "Amar"},
"body" : "Tiger Zinda hey movie was so cool!"

}
}
return render_template("index.html", user=user,post=posts)
if __name__ == "__main__" :
app.run()