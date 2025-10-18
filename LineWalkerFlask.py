
import flask
import time 

app = flask.Flask(__name__)
@app.route("/")
def homepage():
    return flask.render_template("panel1.html")

@app.route('/joystick', methods=['POST'])
def joystick():
    direction= dict(flask.request.form)
    x = direction.get('vx')
    y = direction.get('vy')
    speed = direction.get('speed')
    time.sleep(0.1)
    return f"x = {x} , y = {y} , speed = {speed}"

@app.route("/ptz",methods=['POST'])
def ptz():
    try:
        direction1 = dict(flask.request.form)
        direction1 = direction1.get('direction')
        print(f"direction is:{direction1}")
        return f"PTZ moved {direction1}"
    except():
        return "Eror in PTZ"

@app.route('/emergency_stop',methods=['POST'])
def emergency_stop():

    return "emergency stop has activated!!!"

@app.route('/mode',methods=['post'])
def mode():
    mode = dict(flask.request.form)
    mode= mode.get('mode')
    return mode

app.run(host="127.0.0.1",port=5000)
