from sqlalchemy import create_engine, text
import os

db_connection_string = os.environ['DB_CONNECTION_STRING']



engine = create_engine(
  db_connection_string, 
  connect_args= {
    "ssl": {
      "ssl_ca": "/etc/ssl/cert.pem"
    }  
  })

def load_training_groups_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from training_groups"))
    training_groups = []
    for row in result.all():
      training_groups.append(row._mapping)
    return training_groups
