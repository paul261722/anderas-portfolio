from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_mail import Mail, Message

app = Flask(__name__)
CORS(app)

# Gmail config (replace with your email + app password)
app.config.update(
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT=587,
    MAIL_USE_TLS=True,
    MAIL_USERNAME='your_email@gmail.com',
    MAIL_PASSWORD='your_app_password'
)

mail = Mail(app)

@app.route('/api/contact', methods=['POST'])
def contact():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    message = data.get('message')

    mail.send(
        Message(
            subject=f"Portfolio Message from {name}",
            sender=app.config['MAIL_USERNAME'],
            recipients=['your_email@gmail.com'],
            body=f"From: {name}\nEmail: {email}\n\nMessage:\n{message}"
        )
    )

    return jsonify({'status': 'success', 'message': 'Message sent'})

if __name__ == '__main__':
    app.run(debug=True)
