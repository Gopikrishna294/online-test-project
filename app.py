from flask import Flask,render_template,request
import pymysql
app = Flask(__name__)

db=None
cur=None

def connectDB():
    global db;
    global cur;
    db = pymysql.connect(host='localhost',
		user='root',
		password='',
		database='itvedhant')
    #create cursor
    cur = db.cursor()

def disconnectDB():
    db.close()

def insertRecords(Sname,Sid):
    connectDB()
    insertquery='insert into stuexam(StudentN,StudentID) values("{}","{}")'.format(Sname,Sid)
    cur.execute(insertquery)
    db.commit()
    disconnectDB()
    got()

@app.route('/',methods=['GET','post'])
def index():
        #Sname=request.args.get('Sname')
        #Sid=request.args.get('Sid')
        #insertRecords(Sname,Sid)
        if request.method=='POST':
           Sname=request.form['Sname']
           Sid=request.form['Sid']
           insertRecords(Sname,Sid)
        return render_template('index.html')

def got():
    return render_template('menubar.html')

@app.route('/menubar')
def menubar():
    return render_template('menubar.html')

@app.route('/aptitude')
def aptitude():
    return render_template('aptitude.html')

@app.route('/english')
def english():
    return render_template('english.html')

@app.route('/math')
def math():
    return render_template('math.html')

@app.route('/gk')
def gk():
    return render_template('gk.html')


if __name__=='__main__':
    app.run(debug=True)
