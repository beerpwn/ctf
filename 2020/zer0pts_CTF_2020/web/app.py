import flask
import flask_bootstrap
import os
import pickle
import base64
import datetime

app = flask.Flask(__name__)
app.secret_key = os.urandom(16)
bootstrap = flask_bootstrap.Bootstrap(app)

@app.route('/', methods=['GET'])
def index():
    return notepad(0)

@app.route('/note/<int:nid>', methods=['GET'])
def notepad(nid=0):
    data = load()
    
    if not 0 <= nid < len(data):
        nid = 0
    
    return flask.render_template('index.html', data=data, nid=nid)

@app.route('/new', methods=['GET'])
def new():
    """ Create a new note """
    data = load()
    data.append({"date": now(), "text": "", "title": "*New Note*"})
    flask.session['savedata'] = base64.b64encode(pickle.dumps(data))
    
    return flask.redirect('/note/' + str(len(data) - 1))

@app.route('/save/<int:nid>', methods=['POST'])
def save(nid=0):
    """ Update or append a note """
    if 'text' in flask.request.form and 'title' in flask.request.form:
        title = flask.request.form['title']
        text = flask.request.form['text']
        data = load()
        
        if 0 <= nid < len(data):
            data[nid] = {"date": now(), "text": text, "title": title}
        else:
            data.append({"date": now(), "text": text, "title": title})
        
        flask.session['savedata'] = base64.b64encode(pickle.dumps(data))
    else:
        return flask.redirect('/')
    
    return flask.redirect('/note/' + str(len(data) - 1))

@app.route('/delete/<int:nid>', methods=['GET'])
def delete(nid=0):
    """ Delete a note """
    data = load()

    if 0 <= nid < len(data):
        data.pop(nid)
    if len(data) == 0:
        data = [{"date": now(), "text": "", "title": "*New Note*"}]
    
    flask.session['savedata'] = base64.b64encode(pickle.dumps(data))
    
    return flask.redirect('/')

@app.route('/reset', methods=['GET'])
def reset():
    """ Remove every note """
    flask.session['savedata'] = None
    
    return flask.redirect('/')

@app.route('/favicon.ico', methods=['GET'])
def favicon():
    return ''

@app.errorhandler(404)
def page_not_found(error):
    """ Automatically go back when page is not found """
    referrer = flask.request.headers.get("Referer")
    
    if referrer is None: referrer = '/'
    if not valid_url(referrer): referrer = '/'
    
    html = '<html><head><meta http-equiv="Refresh" content="3;URL={}"><title>404 Not Found</title></head><body>Page not found. Redirecting...</body></html>'.format(referrer)
    
    return flask.render_template_string(html), 404

def valid_url(url):
    """ Check if given url is valid """
    host = flask.request.host_url
    
    if not url.startswith(host): return False  # Not from my server
    if len(url) - len(host) > 16: return False # Referer may be also 404
    
    return True

def load():
    """ Load saved notes """
    try:
        savedata = flask.session.get('savedata', None)
        data = pickle.loads(base64.b64decode(savedata))
    except:
        data = [{"date": now(), "text": "", "title": "*New Note*"}]
    
    return data

def now():
    """ Get current time """
    return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')


if __name__ == '__main__':
    app.run(
        host = '0.0.0.0',
        port = '8001',
        debug=False
    )
