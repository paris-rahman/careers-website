from flask import Flask, render_template,jsonify

app = Flask(__name__)

JOBS = [
  {
    "id" : 1,
    "title" : "Data Engineer",
    "location" :"Chennai, India",
    "salary" : "10,00,000 LPA"
  },
  {
    "id" : 2,
    "title" : "Python Backend Developer",
    "location" :"Bangalore,India",
    "salary" : "15,00,000 LPA"
  },
  {
    "id" : 3,
    "title" : "Java Backend Developer",
    "location" :"Mumbai,India",
    "salary" : "20,00,000 LPA"
  }

  
]


@app.route("/")
def hello_world():
  return render_template("home.html",jobs = JOBS)

@app.route("/api/jobs")
def display_jobs():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run(host = "0.0.0.0",debug=True)




