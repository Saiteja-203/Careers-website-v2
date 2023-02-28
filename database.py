from sqlalchemy import create_engine,text
from decouple import config
string=config('db_con_string')
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
        jobs.append(dict(row))
    return jobs