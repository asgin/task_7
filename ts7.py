from flask import Flask, render_template
from ts import *

app = Flask(__name__)

@app.route('/')
def start():
    return 'This is answer for 7 task.'

@app.route('/report')
def list_of_drivers_and_times():
    return render_template('report.html', table=return_res(calculate(), read_abbreviations()))

@app.route('/report/drivers/')
def list_of_drivers():
    return render_template('drivers.html', drivers=return_res(calculate(), read_abbreviations()))

@app.route('/report/drivers/order=desc')
def reverse_list_of_drivers():
    d = return_res(calculate(), read_abbreviations())    
    d = sorted(d, key=lambda x: x[1], reverse=True)    
    return render_template('drivers.html', drivers=d)

@app.route('/report/drivers/<driver_id>')
def driver_info(driver_id):
     return render_template('drivers_id.html', s=calculate(), d_id=driver_id, s1=read_abbreviations())

if __name__ == '__main__':
    app.run(debug=True)