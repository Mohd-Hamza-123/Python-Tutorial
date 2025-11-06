from flask import Flask 

app = Flask(__name__)

age = 55
name = 'Hamza'
email = 'hamza@gmail.com'
p = "Firebase is a Backend-as-a-Service (BaaS) platform developed by Google. It provides a collection of cloud-based tools and services that help developers build, improve, and scale web and mobile applications quickly without managing servers or complex infrastructure."
# age is a variable , and it store 55
age = 44.4435495383534985478589
@app.route("/")
def home():
    return f"{round(age)}"

app.run(debug=True) 