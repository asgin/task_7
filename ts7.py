from flask import Flask, render_template, request
from ts import *

app = Flask(__name__)

@app.route('/report')
def return_report():
    return render_template('report.html', table=return_res(calculate(), read_abbreviations()))

@app.route('/report/drivers')
def driv():
    return render_template('drivers.html', drivers=return_res(calculate(), read_abbreviations()))

@app.route('/report/drivers/')
def use_args():
    order = request.args.get('order')
    driver_id = request.args.get('driver_id')
    if order and order =='desc':
        d = return_res(calculate(), read_abbreviations())    
        d = sorted(d, key=lambda x: x[1], reverse=True)    
        return render_template('drivers.html', drivers=d)
    if driver_id:
            return render_template('drivers_id.html', s=calculate(), d_id=driver_id, s1=read_abbreviations())

if __name__ == '__main__':
    app.run(debug=True)