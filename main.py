from website import create_app

app = create_app()

# secure the web server to be executed
# when actually needs, not accidentally
if __name__ == '__main__':
    # automatically refresh the flask web server
    app.run(debug=True)