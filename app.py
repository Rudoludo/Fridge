from flask import Flask, render_template, redirect, url_for, request , session
from cs50 import SQL
from flask_session import Session


app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


db = SQL("sqlite:///notes.db")
notes = db.execute("SELECT title,id, created_at AS date FROM tasks")

@app.route("/")
def index():

    notes = db.execute("SELECT title,id, created_at AS date FROM tasks")

    if len(notes) == 0:
        return redirect(url_for("addnote"))

    error = request.args.get("error")
    return render_template("index.html", data=notes, error = error)

"""     else:
        return render_template("index.html", data=notes)  """


@app.route("/notes" , methods=["GET", "POST"])
def show_note():

    #show note from global view
    notes = db.execute("SELECT title,id, created_at AS date FROM tasks")

    if request.method == "POST":
        noteIndex = request.form.get("noteIndex")
        print(noteIndex)
        return render_template("index.html", data=notes, index = noteIndex)

    #show the next note in the list after deleting one from the single view, instead of restarting the browsing from 0
    else:
        if session["resumeIndex"] :
            noteIndex = session["resumeIndex"]
            session["resumeIndex"]= 0
        else:
            noteIndex = 0
        return render_template("index.html", data=notes, index = noteIndex)


@app.route("/note/delete", methods=["POST"])
def delete():

    if request.method == "POST":

        #deleting from single view
        if not request.form.get("deleteId"):

            id = request.form.get("deleteIdS")
            #saving the index to resume browsing from the last viewved note
            deletedIndex = request.form.get("deleteIndex")

            db.execute("DELETE from tasks WHERE id =(?)", id)
            notes = db.execute("SELECT title, id,  created_at AS date FROM tasks")
            lenght = len(notes)

            if lenght == 0:
                return redirect(url_for("addnote"))

            else:
                #saving the index of the deleted note to resume viewing
                session["resumeIndex"] = int(deletedIndex)
                return redirect(url_for("show_note"))


        #deleting from Global view
        id = request.form.get("deleteId")
        db.execute("DELETE from tasks WHERE id =(?)", id)

        # updating notes after delete
        notes = db.execute("SELECT title, id,  created_at AS date FROM tasks")
        lenght = len(notes)

        if lenght == 0:
            return redirect(url_for("addnote"))

        else:
            return render_template("global.html", notes=notes, lenght=lenght)



@app.route("/addnote", methods=["GET", "POST"])
def addnote():

    notes = db.execute("SELECT title, created_at AS date FROM tasks")
    lenght = len(notes)

 # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure note was submitted
        if not request.form.get("new_note"):
            return redirect(url_for("addnote"))
        else:
            db.execute("INSERT INTO tasks (title) VALUES(?)", request.form.get("new_note"))
            session["resumeIndex"] = lenght
            return redirect(url_for("show_note"))


    # User reached route via GET (as by clicking a link or via redirect)
    else:
        #error code for reached notes limit
        if lenght >= 8:
            return redirect(url_for("index", index = 0, error = 8))
        else:
            return render_template("addnote.html", lenght = lenght)



@app.route("/global")
def global_view():
    notes = db.execute("SELECT title, id,  created_at AS date FROM tasks")
    lenght = len(notes)

    if len(notes) == 0:
        return render_template("addnote.html", lenght = 0)
    else:
        return render_template("global.html", notes = notes, lenght = lenght)


if __name__ == "__main__":
    app.run(debug=True)
