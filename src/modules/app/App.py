import time
import sys

from modules import file
from modules import image

from flask import Flask
from flask import request, redirect, url_for, session
from flask import render_template
from flask_session import Session

UPLOAD_PATH = f"{{os.getcwd()}}\\uploads\\"
EXTENSIONS = {".jpg", ".png", ".jpeg"}

app = Flask(__name__, template_folder="views", static_url_path="/storage")
app.config["UPLOAD_FOLDER"] = UPLOAD_PATH
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"

Session(app)

@app.route('/')
def welcome_page():
    return render_template("landing.html")

@app.route('/home', methods=['GET', 'POST'])
def home_page():
    if request.method == 'POST':
        user_folder = None

        if("folder" not in session):
            ip = request.remote_addr
            port = request.environ.get('SERVER_PORT')

            user_folder = f"{ip}P{port}"
            session["folder"] = user_folder
        else:
            user_folder = session["folder"]

        user_folder = file.create_storage(user_folder)

        upload = request.files['file']

        extension = upload.filename.rsplit(".", 1)[1]
        upload.filename = time.time()
        path = f"{user_folder}\\{upload.filename}.{extension}"
        upload.save(path)

        option = request.form.get("options")
        print(user_folder)
        res = image.to_file(path, session["folder"], option)
        return redirect(url_for("home_page", img=res["image"], plt=res["plot"]))
    else:
        curr = None
        if("folder" in session):
            curr = session["folder"]

        options = {
            "manual" : "Manual",
            "cv" : "Grayscale with cv",
            "cv_equal" : "Grayscale with cv with histogram equalizer"
        }
        img = request.args.get("img")
        plt = request.args.get("plt")

        img = f"/{curr}/{img}"
        plt = f"/{curr}/{plt}"
        
        return render_template("home.html", options=options, img=img, plt=plt)
