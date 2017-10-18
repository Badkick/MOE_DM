
from flask import Flask
from flask import request, url_for, redirect, session, render_template
app = Flask("firstFormApplication")
app.secret_key = "very_important_secret"



@app.route("/")
@app.route("/<configuration_list_name>")
def generate_form(configuration_list_name=None):
    from database import Configuration, ConfigurationList
    # If no "configuration_list_name" parameter is provided, redirect to "default"
    if configuration_list_name is None:
        return redirect(url_for("generate_form", configuration_list_name="default"))
    existing_configuration_list = ConfigurationList.query.filter_by(name=configuration_list_name).first()
    # If no existing configuration list, then create a new one
    if existing_configuration_list is None:
        new_configuration_list = ConfigurationList()
        new_configuration_list.name = configuration_list_name
        db.session.add(new_configuration_list)
        db.session.commit()
        existing_configuration_list = new_configuration_list
    # Render the form usign the current configuration list
    return render_template("form.html", configuration_list=existing_configuration_list)


@app.route("/form_handler", methods=["POST"])
def form_handler():
    from database import Configuration
    configuration_list_id = request.form["configuration_list_id"]
    configuration_list_name = request.form["configuration_list_name"]
    configuration_text = request.form["configuration_text"]

    # Create a new configuration
    new_configuration = Configuration()
    new_configuration.label = configuration_text
    new_configuration.isDone = False
    new_configuration.configuration_list_id = configuration_list_id # Make the link between Configuration and ConfigurationList

    db.session.add(new_configuration)
    db.session.commit()

    return redirect(url_for("generate_form", configuration_list_name=configuration_list_name))


@app.route('/delete/<configuration_id>')
def configuration_remove(configuration_id):
    from database import Configuration
    Configuration.query.filter_by(id=configuration_id).delete()
    return redirect(url_for("generate_form", configuration_list_name="default"))

    



if __name__ == "__main__":
    # Create the DB
    from database import db
    print("creating database")
    db.create_all()
    print("database created")
    app.jinja_env.auto_reload = True
    app.run(host="127.0.0.1", port=8080, debug=True)


