from flask import Flask, render_template
import database

app = Flask(__name__)

@app.route('/')
def land_homepage():
  experiences = database.load_all_experiences_from_db()
  return render_template('homepage.html',
                        experiences=experiences)

@app.route('/experience/<id>')
def land_experiencepage(id):
  experience = database.load_experience_from_db(id)[0]
  return render_template('experiencepage.html',
                        experience=experience)

if __name__ == '__main__': 
  app.run(host='0.0.0.0', debug=True)