from sqlalchemy import create_engine, text

db_connection_string = "mysql+pymysql://1kjvtaq3qs50aw1ogso6:pscale_pw_eLZgn4DstA5BjmFQGGZqrqNJfGnKuWHFZAg6rxXxwzF@aws.connect.psdb.cloud/footyacademy?charset=utf8mb4"

engine = create_engine(
  db_connection_string, 
  connect_args= {
    "ssl": {
      "ssl_ca": "/etc/ssl/cert.pem"
    }  
  })

#with engine.connect() as conn:
  #result = conn.execute(text("select * from training_groups"))

  #result_dicts = []
  #for row in result.all():
    #result_dicts.append(row._mapping)

  #print(result_dicts)
  
  #print("type(result):", type(result))
  #result_all = result.all()
  #print("type(result.all()):", type(result_all))
  #first_result = result_all[0]
  #print("type(first_result):", type(first_result))
  #first_result_dict = first_result._mapping ###USE ._mapping TO GET THE DICTIONARY
  #print("type(first_result_dict):", type(first_result_dict))
  #print(first_result_dict)