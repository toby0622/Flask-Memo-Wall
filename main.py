# flask framework initialization
from website import create_app

app = create_app()

# only called when itself needs to be executed
# will not be called when itself be referenced
if __name__ == '__main__':
    # automatically refresh the flask web server
    app.run(debug=True)