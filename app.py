from flask import Flask, render_template, request, send_file
from model import predict_doctors  # Import the function from model.py

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        login_hour = int(request.form['login_time'])
        doctors = predict_doctors(login_hour)

        if doctors is None:
            return render_template("index.html", message="No doctors found for this time range.")

        return render_template("index.html", doctors=doctors, file_url="doctor_predictions.xlsx")
    
    except Exception as e:
        return str(e)

@app.route('/download')
def download():
    return send_file("doctor_predictions.xlsx", as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
