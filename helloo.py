from flask import Flask
app=Flask(__name__)
@app.route('/')
def helloo():
    return("Hello World, this is shreya ")
if __name__ == "__main__":
    app.run(debug=True)