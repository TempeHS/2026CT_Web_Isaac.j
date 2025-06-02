from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/index.html')
@app.route('/')
def index():
    card_data = (
        ("title",  "description", "bottom text", "image_url", "link"),
        ("title2", "description2", "bottom text2", "image_url2", "link2"),
        ("title3", "description3", "bottom text3", "image_url3", "link3"),
        ("title4", "description4", "bottom text4", "image_url4", "link4"),
        ("title5", "description5", "bottom text5", "image_url5", "link5"),
    )
    return render_template("index.html", cards=card_data), 200

@app.route('/contact.html')
def contact():
    return render_template("contact.html"), 200

@app.route('/poi.html')
def poi():
    return render_template("poi.html"), 200
                        
@app.route('/acc.html')
def acc():
    return render_template("acc.html"), 200

@app.route('/act.html')
def act():
    return render_template("act.html"), 200

@app.route('/gar.html')
def gar():
    return render_template("gar.html"), 200

@app.route('/food.html')
def food():
    return render_template("food.html"), 200

@app.route('/cltr.html')
def cltr():
    return render_template("cltr.html"), 200

@app.route('/tar.html')
def tar():
    return render_template("tar.html"), 200

if __name__ == '__main__':
    app.run(debug=True)
