# Doctor Login Time Prediction  

This project predicts doctors most likely to log in at a given time using a **Random Forest Classifier** trained on historical login data. It also allows users to download an **Excel report** and send **automated emails** with NPIs.

## Features  
- **Predict doctors** based on login time (±1 hour window).  
- **Download Excel** report with NPI, Speciality, and Region.  
- **Send automated emails** to a given domain.  
- **User-friendly Web Interface** for input and results.  

## Installation  
```sh
git clone https://github.com/Doctor_Prediction.git  
pip install -r requirements.txt  
 
## File structure

│── model.py  # ML model for predictions  
│── app.py  # Flask backend  
│── index.html  # Frontend UI  
│── styles.css  # Styling   
│── cleaned_dataset.csv  # Dataset  
│── requirements.txt  # Dependencies  
│── README.md  

## Final look
![prediction](file:///C:/Users/Stuti/Desktop/Survey/Screenshot%202025-03-15%20235043.png)

