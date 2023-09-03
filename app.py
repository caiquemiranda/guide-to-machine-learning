from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('End_to_End_Machine_Learning_Project.html')

if __name__ == '__main__':
    app.run()
