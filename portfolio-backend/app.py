from flask import Flask, request, jsonify
from flask_mail import Mail, Message
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'your-portfolio-email@gmail.com'      # 🔁 use portfolio Gmail
app.config['MAIL_PASSWORD'] = 'nysoratbdrxmmkab'         # 🔁 use the app password

mail = Mail(app)

@app.route('/api/portfolio-contact', methods=['POST'])
def portfolio_contact():
    data = request.get_json()
    msg = Message(
        subject=f"New Message from {data['name']}",
        sender=data['email'],
        recipients=['anderapaul22@gmail.com'],
        body=data['message']
    )
    mail.send(msg)
    return jsonify({'status': 'success', 'message': 'Message sent!'})

if __name__ == '__main__':
    app.run(debug=True)
