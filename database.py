from sqlalchemy import create_engine,text
import os
from dotenv import load_dotenv
load_dotenv()
string=os.getenv('db_con_string')

db_cs=string
engine=create_engine(
    db_cs,
    connect_args={
    "ssl":{
        "ssl_ca":"/etc/ssl/cert.pem"
    }
    }
)
def load_jobs_from_db():
  with engine.connect() as conn:
    result=conn.execute(text('select * from jobs'))

    jobs=[]
    for row in result.all():
        jobs.append(dict(row._mapping))
    return jobs
def load_job_from_db(id):
  with engine.connect() as conn:
    result=conn.execute(text('select * from jobs where id= :val'),val=id)
    row=result.all()
    if len(row)==0:
      return None
    else:
      return dict(row[0]._mapping)

def add_application_to_db(id,data):
  with engine.connect() as conn:
    query=text(
      '''insert into applications (job_id,full_name,email,
      linkedin_url,education,work_experience,resume_url)
       values(:job_id,:full_name,:email,:linkedin_url,:education
       ,:work_experience,:resume_url)''')
    conn.execute(query,job_id=id,full_name=data['full_name'],email=data['email'],linkedin_url=data['linkedin_url'],education=data['education'],work_experience=data['work_experience'],resume_url=data['resume_url'])