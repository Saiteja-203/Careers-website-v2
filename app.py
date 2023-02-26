from flask import Flask, render_template,jsonify

app = Flask(__name__)
JOBS=[
  {
    'id':1,
    'title':'Data Analyst',
    'location':'Bengaluru,India',
    'Salary':'Rs.10,00,000'
  },
  {
    'id':2,
    'title':'Data Scientist',
    'location':'Bengaluru,India',
    'Salary':'Rs.30,00,000'
  },
  {
    'id':3,
    'title':'Backend Engineer',
    'location':'Remote',
    'Salary':'Rs.20,00,000'
  },
  {
    'id':4,
    'title':'Full Stack Engineer',
    'location':'Delhi',
    'Salary':'Rs.25,00,000'
  },
  {
    'id':5,
    'title':'ML-OPS Engineer',
    'location':'Seatle',
    'Salary':'$1,20,000'
  }
]

@app.route('/')
def func():
  return render_template('home.html',
                         jobs=JOBS,company_name='GET')
@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
