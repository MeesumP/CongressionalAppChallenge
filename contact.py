from flask import Blueprint, render_template, request, redirect, url_for
from models import db, Ticket

from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, TextAreaField

contact = Blueprint(__name__, 'contact')

@contact.route('/', methods=['POST', 'GET'])
def contact_page():
    class ContactForm(FlaskForm):
        email = StringField(u'Email:', render_kw={'class':"textbox-format"})
        info = TextAreaField(u'Please write your question below:', render_kw={'class':"textbox-format"})
        submit = SubmitField("Submit", render_kw={'class': 'submit_button'})

    form = ContactForm()

    if form.is_submitted():
        result = request.form

        email = result.get('email')
        info = result.get('info')

        ticket = Ticket(email=email, info=info)
        db.session.add(ticket)
        db.session.commit()

        return redirect('/contact/thank-you')

    return render_template('contact.html', form=form)

@contact.route('/thank-you')
def thank_youpage():
    return render_template('aftercontactthank.html')