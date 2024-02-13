from scp import app, db

if __name__ == '__main__':
    with app.app_context():
        app.run(debug=True)
