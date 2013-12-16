import glob
from flask import Flask, render_template, flash, url_for, request
app = Flask(__name__)

PREFIX = 'static/'
ALL_FILES = glob.glob('%spictures/*' % PREFIX)
ALL_FILES.sort()

@app.route("/")
def main():
    index = request.args.get('index', 0, type=int)
    image = getImage()
    return render_template('main.html', image=image, index=index)

@app.route('/next')
def nextImage():
    return getImage(1)

@app.route('/previous')
def previousImage():
    return getImage(-1)

@app.route('/image')
def image(index=None):
    if index == None:
        index = request.args.get('index', 0, type=int)
    image = ALL_FILES[index].replace(PREFIX,'')
    return url_for('static', filename=image)

def getImage(offset=1):
    index = request.args.get('index', 0, type=int)
    nextIndex = (index+offset)%len(ALL_FILES)
    return image(nextIndex)

if __name__ == '__main__':
    app.run('0.0.0.0', debug=True)