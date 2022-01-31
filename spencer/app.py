from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def index():
#    title = "Spencer Hurrle"
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

    <a href="http://192.168.1.14:8001/api/v1/namespaces/default/services/webapp-service:80/proxy/how-did-we-get-here">This way to the future!(pending)</a>
    '''
    #return render_template("index.html")
    return html


@app.route('/how-did-we-get-here')
def how():
#    title = "The Journey"
    html = '''
    <title>The Journey</title>
    <h1>How Did We Get Here?</h1>
    <h4>(Fancy pictures and more color coming soon)</h4>

    <a href="http://192.168.1.14:8001/api/v1/namespaces/default/services/webapp-service:80/proxy/1">Take a look at the process</a>
    '''
    return html
#    return render_template("journey.html")


@app.route('/1')
def firstSteps():
    html = '''
    <h1>It Began With An App</h1>
    <ul>
        <li>This app was developed before anything else because I wanted to try deploying something that was my own</li>
        <li>I created the first page of my site and created the Dockerfile</li>
        <li>Initially it was just the one page with my 60 second pitch, until I improvised using it as a way to present</li>
    </ul>

    <a href="http://192.168.1.14:8001/api/v1/namespaces/default/services/webapp-service:80/proxy/2">What's a Dockerfile?<br/></a>
    <a href="http://192.168.1.14:8001/api/v1/namespaces/default/services/webapp-service:80/proxy/">Home</a>
    '''
    return html


@app.route('/2')
def servingJenkins():
    html = '''
    <h1>Docker Implementation</h1>
    <ul>
        <li>Used the Dockerfile to build a container with my app image</li>
        <li>Once I established that the image was working, I set up a jenkins pipeline<br/>to grab updates periodically and ensure that the app image stays up to date</li>
        <li>I tried to do webhooks, but was unable to establish that link. Ultimately I ended up setting Jenkins to build every 5 minutes</li>
    </ul>

    <a href="http://192.168.1.14:8001/api/v1/namespaces/default/services/webapp-service:80/proxy/3">You'll Never Believe What I Did Next<br/></a>
    <a href="http://192.168.1.14:8001/api/v1/namespaces/default/services/webapp-service:80/proxy/1">Back<br/></a>
    <a href="http://192.168.1.14:8001/api/v1/namespaces/default/services/webapp-service:80/proxy/">Home</a>
    '''
    return html 


@app.route('/3')
def kubernetes():
    html = '''
    <h1>Kubernetes</h1>
    <ul>
        <li>Once the app is running well in my Docker container, it's time to deploy the pods!</li>
        <li>I took time to really comprehend how the deployment and service yaml files interact with each other and their roles in pod orchestration</li>
        <li>Even after cracking down with k8s, I was still unable to connect to my pods. Found that it was because my deployment file needed<br/>a containerPort identified under deployment containers. I also needed a proxy set up to <br/> reach my pods inside the VM</li>
    </ul>

    <a href="http://192.168.1.14:8001/api/v1/namespaces/default/services/webapp-service:80/proxy/4">Any Ansible?<br/></a>
    <a href="http://192.168.1.14:8001/api/v1/namespaces/default/services/webapp-service:80/proxy/2">Back<br/></a>
    <a href="http://192.168.1.14:8001/api/v1/namespaces/default/services/webapp-service:80/proxy/">Home</a>
    '''
    return html


@app.route('/4')
def ansible():
    html = '''
    <h1>Ansible</h1>
    <ul>
        <li>Ansible was used to automate tool installation for this project</li>
        <li>Kubernetes and Docker were both installed with Ansible</li>
    </ul>

    <a href="http://192.168.1.14:8001/api/v1/namespaces/default/services/webapp-service:80/proxy/5">Moving Forward<br/></a>
    <a href="http://192.168.1.14:8001/api/v1/namespaces/default/services/webapp-service:80/proxy/3">Back<br/></a>
    <a href="http://192.168.1.14:8001/api/v1/namespaces/default/services/webapp-service:80/proxy/">Home</a>
    '''
    return html


app.route('/5')
def conclusion():
    html = '''
    <h1>Wrapping Up</h1>
    <h3>Challenges</h3>
    <ol>
        <li>Exposing my app to the public was the biggest challenge for me<br/>I overcame this challenge by researching my issue until I found the appropriate fix</li>
        <li>Another challenge was figuring out how to decorate the app in Flask. Since this was not a goal of the <br/>project, it was kept on the back burner most of the time.<br/>I overcame this issue by deciding to go with a white background/black text theme. Kidding! I did not get through this challenge.
        <li>Time management was an challenge for me. The project is finished, but not nearly as well as I would have liked.<br/>I would say that I just barely overcame this issue</li>
    </ol>

    <h3>Goals</h3>
    <ul>
        <li>Achieve a connection between Ansible and an AWS EC2 for easy configuration</li>
        <li>Learn more about Flask usage and layout</li>
        <li>Improve time management and efficiency</li>
        <li>Gain a deeper understanding of networking concepts</li>
    </ul>

    <a href="http://192.168.1.14:8001/api/v1/namespaces/default/services/webapp-service:80/proxy/4">Back<br/></a>
    <a href="http://192.168.1.14:8001/api/v1/namespaces/default/services/webapp-service:80/proxy/">Home</a>
    '''
    return html

app.run(host='0.0.0.0', port=5000)
