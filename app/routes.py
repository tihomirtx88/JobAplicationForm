from flask import Blueprint, render_template, request, redirect, url_for, flash
from .models import Form, db
from .services.mail_service import MailService
from datetime import datetime

main = Blueprint("main", __name__)

@main.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        first_name = request.form["first_name"]
        last_name = request.form["last_name"]
        email = request.form["email"]
        date = request.form["date"]
        date_obj = datetime.strptime(date, "%Y-%m-%d")
        occupation = request.form["occupation"]

        form = Form(first_name=first_name, last_name=last_name,
                    email=email, date=date_obj, occupation=occupation)
        db.session.add(form)
        db.session.commit()

        MailService.send_confirmation(email, first_name, last_name, date)

        flash(f"{first_name}, your form was submitted successfully!", "success")
        return redirect(url_for("index.index"))

    return render_template("index.html")

@main.route("/submissions")
def submissions():
    forms = Form.query.all()
    return render_template("submissions.html", forms=forms)

@main.route("/submission/<int:id>")
def submission_detail(id):
    form = Form.query.get_or_404(id)
    return render_template("submission_detail.html", form=form)

@main.route("/about")
def about():
    return render_template("about.html")

@main.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        message = request.form["message"]

        MailService.send_confirmation("admin@example.com", name, "", "N/A")

        flash("Your message was sent successfully!", "success")
        return redirect(url_for("main.contact"))

    return render_template("contact.html")