from flask import Flask, render_template, flash, redirect, url_for
from forms import FeedbackForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'

@app.route('/')
def home():
    return render_template('layout/home.html')

@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
    form = FeedbackForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        message = form.message.data
        flash('Thank you for your feedback!', 'success')
        return redirect(url_for('home'))
    return render_template('layout/feedback.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
