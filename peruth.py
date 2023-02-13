from flask import Flask,jsonify,request,redirect,url_for

app = Flask(__name__)

@app.route("/articles")
def get_articles():
    articles=[
        {
            "id":1,
            "name":"Long time",
            "author":"Kenta Romes",
            "Description":"Getting better always"
        },
        {
            "id":2,
            "name":"Forever yours",
            "author":"Debby",
            "Description":"No and Always going forward"
        },
        {
            "id":3,
            "name":"Quick and Loud",
            "author":"Anthomy kk",
            "Description":"Tomorrow goes away and today lasts longer"
        }
    ]
    return jsonify(articles)


if __name__=='__peruth__':
    app.run()
