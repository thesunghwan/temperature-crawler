from flask import Flask, Response
app = Flask(__name__)

@app.route("/")
def hello():
    #data = open("sample.csv")

    with open("sample.csv") as fp:
        csv = fp.read()
    #csv = '1,2,3\n4,5,6\n'
    return Response(
        csv,
        mimetype="text/csv",
        headers={"Content-disposition":
                 "attachment; filename=sample.csv"})
    #return "Hello World!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8000")
