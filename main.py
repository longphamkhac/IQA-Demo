from flask import Flask, render_template, url_for, redirect, request, flash
import os

app = Flask(__name__)

app.config['SECRET_KEY'] = "5791628bb0b13ce0c676dfde280ba245"
app.config["PREVIEW_IMG"] = "preview.svg"
app.config["SAVE_PATH"] = "static"


@app.route("/")
def main():
    image_file = url_for("static", filename = "mats/" + app.config["PREVIEW_IMG"])

    return render_template("main.html", image_file = image_file, result = "Fair")

# @app.route("/upload-image", methods = ["POST", "GET"])
# def upload_image():
#     if request.method == "POST":

#         if request.files["image"].filename != "":
#             image = request.files["image"]
            
#             image_file = os.path.join(app.config["SAVE_PATH"], image.filename)
#             image.save(image_file)

#             return render_template("main.html", image_file = image_file)
#             # return redirect(request.url)

#         else:
#             pass
#     return redirect(url_for("main"))

@app.route("/confirm", methods = ["POST", "GET"])
def confirm():
    if request.method == "POST":
        out = request.form.get("p")
        print(out)
        flash("Review successfully!")

    return redirect(url_for("main"))

if __name__ == "__main__":
    app.run(debug = True)
