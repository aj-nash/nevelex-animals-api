from flask import Flask, request, render_template, redirect, flash
from controller import nevelex_api

flask_app = Flask(__name__)
flask_app.debug = True

info = ""

@flask_app.route("/")
def main_page():

    global info

    parsed_animal_list = nevelex_api.animal_list()

    #Put animals in a dictionary and render with the template
    animal_dict = {}

    for i in range(1, len(parsed_animal_list)+1):
        stripped_animal_name = parsed_animal_list[i-1]["commonName"].strip()
        animal_dict[i] = {"common_name" : stripped_animal_name }

    return render_template('animals.html', animal_dict = animal_dict, info = info)

@flask_app.route("/info/<string:animal_name>")
def get_info(animal_name):

    #Store info from a call to the api
    global info
    id = nevelex_api.get_id_for(animal_name)
    info = nevelex_api.animal_info(id)

    return redirect("/")

@flask_app.route("/create", methods=["GET", "POST"])
def create():
    global info
    info = ""

    #Store input data from request
    common_name = request.form.get("common_name", None)
    scientific_name = request.form.get("scientific_name", None)
    family = request.form.get("family", None)
    img_url = request.form.get("image_url")

    if common_name == None or common_name == "none" or common_name == " ":
        flash("Common name is required for creating a new animal entry.")

    else:
        # Renullify null values
        if scientific_name == "none":
            scientific_name = None
        if family == "none":
            family = None
        if img_url == "none":
            img_url = None

        status_code = nevelex_api.create(common_name, scientific_name, family, img_url)

        if (status_code == 200):
            flash("You successfully added a new animal!")
        else:
            flash("Sorry, the web service is down with status_code {}. Try again later.".format(r.status_code))

    return redirect("/")


@flask_app.route("/delete/<string:animal_name>")
def delete(animal_name):
    global info
    id = nevelex_api.get_id_for(animal_name)
    nevelex_api.delete(id)
    info = ""

    return redirect("/")