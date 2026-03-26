from app import app
from app.contacts import contacts

app.register_blueprint(contacts)

# NO necesitas importar db aquí

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)