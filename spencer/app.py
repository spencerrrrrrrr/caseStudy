from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def index():
    html = '''
    <title>Spencer Hurrle</title>
    <h2>Professional Software Development and Process Automation</h2>
    <h3>About Me:</h3>
    <p>My name is Spencer Hurrle, and I’m currently a DevOps Student
         at Per Scholas. I’m pursuing a career in DevOps so that I can 
         fill out more of my personal potential. I always aim to achieve 
         the most effective and transparent solutions in my work. In 
         addition to being technically proficient, I love to collaborate 
         with others and pool the best ideas into one amazing product.</p>

    <a href="{{ url_for('how-did-we-get-here') }}">Take a look at the process</a>
    '''
    #return render_template("index.html", title=title)
    return html


@app.route('/how-did-we-get-here')
def how():
    html = '''
    <title>The Journey</title>
    <h1>How Did We Get Here?</h1>
    '''
    return html

app.run(host='0.0.0.0', port=5000)
