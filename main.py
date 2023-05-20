import module
from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/',methods = ['POST','GET'])
def find_data():
    data_total = ''
    if request.method == 'POST':
        name = request.form.get('movie')
        data_total = module.find_movie(name)
    return render_template('index.html',value = data_total)
if __name__ == '__main__':
    app.run(debug=True)