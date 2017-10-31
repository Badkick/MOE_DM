
from flask import Flask
from flask import request, url_for, redirect, session, render_template
app = Flask("firstFormApplication")
app.secret_key = "very_important_secret"



@app.route("/")
def configuration_list():
    from database import Configuration
    configurations = Configuration.query.all()
    return render_template("index.html", confs=configurations)



#@app.route('/delete/<configuration_id>')
#def configuration_remove(configuration_id):
   # from database import Configuration
   # Configuration.query.filter_by(id=configuration_id).delete()
   # return redirect(url_for("generate_form", configuration_list_name="default"))

@app.route("/creer")
def creer_configuration():
    from database import Configuration
    new_configuration = Configuration()
    return render_template("yaml-form.html", Configuration=new_configuration)

@app.route("/creer/enregistrer", methods=["POST"])
def ajouter_configuration():
    from database import Configuration

    configuration_mutable = request.form["configuration_mutable"]


    new_configuration = Configuration()
    new_configuration.mutable= request.form["configuration_mutable"]
    db.session.add(new_configuration)

    configurations = Configuration.query.all()
    return redirect(url_for("configuration_list()"))




if __name__ == "__main__":
    # Create the DB
    from database import db
    print("creating database")
    db.create_all()
    print("database created")
    app.jinja_env.auto_reload = True
    app.run(host="127.0.0.1", port=8080, debug=True)


