from flask import Flask, render_template, jsonify
from database import engine
from sqlalchemy import text

app = Flask(__name__)



def load_training_groups_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from training_groups"))
    training_groups = []
    for row in result.all():
      training_groups.append(row._mapping)
    return training_groups

@app.route("/")
def hello_jovian():
  training_groups = load_training_groups_from_db()
  return render_template("home.html", training_groups=training_groups)

@app.route("/api/list_of_training_groups")
def list_training_groups():
  return jsonify(load_training_groups_from_db)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)