from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)


app.config['SECRET_KEY'] = 'ff1e2033b6671b9129fecaef8e623834'
posts = [
    {
        'author': 'Douglas Obara',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'March 5,2021'
    },
    {
        'author': 'Basil Mutinda',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'March 6,2021'
    }
]


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html', title='about')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        (f'Account created for { form.username.data }!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'douglas@blog.com' and form.password.data == 'password':
            flash('you have been logged in succesful', 'success')
            return redirect(url_for('home'))
        else:
            flash('unsuccessful')
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)
flash
