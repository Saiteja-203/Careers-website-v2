from flask import Flask, render_template,jsonify,request
from database import load_jobs_from_db,load_job_from_db

app = Flask(__name__)

@app.route('/')
def func():
  Jobs=load_jobs_from_db()
  return render_template('home.html',jobs=Jobs)

@app.route("/job/<id>")
def show_job(id):
  job=load_job_from_db(id)
  if job==None:
    return "Not Found",404
  return render_template('jobpage.html',job=job)

@app.route("/job/<id>/apply",methods=['post'])
def apply_to_job(id):
  data=request.form
  return render_template('application_submitted.html',application=data)



@app.route("/api/jobs")
def list_jobs():
  Jobs=load_jobs_from_db()
  return jsonify(Jobs)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
