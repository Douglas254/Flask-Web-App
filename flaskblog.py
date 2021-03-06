from flask import Flask, render_template, url_for
app = Flask(__name__)


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


if __name__ == '__main__':
    app.run(debug=True)
