# Import necessary libraries
from flask import Flask, render_template, request
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import joblib
import string
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')

# function to remove punctuation and stopwords
def text_process(text):
    non_punc = [char for char in text if char not in string.punctuation]
    non_punc=''.join(non_punc)
    return [word for word in non_punc.split() if word not in stopwords.words('english')]

# Load the pre-trained model
pipe_spam_model = joblib.load('pipe_spam_model.pkl')

# Create Flask app
app = Flask(__name__)

# Define the home route
@app.route('/')
def home():
    return render_template('index.html')

# Define the prediction route
@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Get the input text from the user
        user_input = [request.form['email_text']]

        prediction = pipe_spam_model.predict(user_input)
        print(prediction[0])
        # Display the result on the result page
        return render_template('result.html', prediction=prediction[0])

if __name__ == '__main__':
    # app.run(debug=True)
    app.run(host="0.0.0.0")
