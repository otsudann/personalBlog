from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello World</p>"

@app.route("/hello/<name>")
def hello_name(name):
    return f"Hello {name}!"

@app.route("/blog/<int:postID>")
def show_blog(postID):
    return f"Blog number {postID}"

@app.route("/rev/<float:revNO>")
def revision(revNO):
    return f"Revision number {revNO}"

if __name__ == "__main__":
    app.run()
