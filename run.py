from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def homepage():
    return render_template('index.html')

@app.route('/ksiega1')
def k1():
    return render_template('k1.html')


@app.route('/ksiega2')
def k2():
    return render_template('k2.html')


@app.route('/ksiega3')
def k3():
    return render_template('k3.html')


@app.route('/ksiega4')
def k4():
    return render_template('k4.html')


@app.route('/ksiega5')
def k5():
    return render_template('k5.html')


@app.route('/ksiega6')
def k6():
    return render_template('k6.html')


@app.route('/ksiega7')
def k7():
    return render_template('k7.html')


@app.route('/ksiega8')
def k8():
    return render_template('k8.html')


@app.route('/ksiega9')
def k9():
    return render_template('k9.html')


@app.route('/ksiega10')
def k10():
    return render_template('k10.html')


@app.route('/ksiega11')
def k11():
    return render_template('k11.html')


@app.route('/ksiega12')
def k12():
    return render_template('k12.html')


if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)
