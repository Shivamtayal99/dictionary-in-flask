from flask import Flask,render_template
app = Flask(__name__)

@app.route('/dictinflask')
def loopinflask():
    dic1=[{'Shivam':"1",'Shubham':"2",'Monu':"3",'Sonu':'4','Vishal':'5'}]
    return render_template('index.html',list=dic1)

app.run(port=5001,debug=True)
