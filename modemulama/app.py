from flask import Flask, render_template, url_for, request
import pickle

# Load your model here
with open('modell.pkl', 'rb') as f:
    model = pickle.load(f)

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def home():
    prediction = None
    if request.method == 'POST':
        comment = request.form['area']
        prediction = model.predict([comment])[0]
        prediction_text = "This is our Prediction: {}".format(prediction)
    else:
        prediction_text = None
    return render_template('index.html', prediction=prediction_text)

if __name__ == "__main__":
    app.run(debug=True)
