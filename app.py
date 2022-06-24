from flask import Flask, request, jsonify , render_template

from chat import get_response

app = Flask(__name__,static_folder='static',
            template_folder='templates')


@app.get('/')
def index_get():
    return render_template("base.html")

@app.post('/predict')
def predict():
    text = request.get_json().get("message")
    # Checking if the text is valid or not
    response = get_response(text)
    message = {"answer": response}
    return jsonify(message)

if __name__ == '__main__':
    app.run(debug=True)