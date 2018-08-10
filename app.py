from flask import Flask
from flask_cqlalchemy import CQLAlchemy
from flask import jsonify

app = Flask(__name__)
app.config['CASSANDRA_HOSTS'] = ['localhost']
app.config['CASSANDRA_KEYSPACE'] = "cz"
db = CQLAlchemy(app)

class Tweets_count_by_lang_tag(db.Model):
    language = db.columns.Text(required=True, primary_key=True)
    tag = db.columns.Text(required=True, primary_key=True)
    qtd = db.columns.BigInt(static=True)

class Most_followed_users_by_process_date(db.Model):
    process_date = db.columns.Text(required=True, primary_key=True)
    followers_count = db.columns.BigInt(required=True, primary_key=True)
    author_id = db.columns.BigInt(required=True, static=True)
    friends_count = db.columns.BigInt(required=True, static=True)
    tag = db.columns.Text(required=True, static=True)
    username = db.columns.Text(required=True, static=True)

@app.route('/')
def landing_page():
    return 'Requisite o endpoint desejado'

@app.route('/users/<string:date>', methods=["GET"])
def get_most_followed_users_by_date(date):
    users = Most_followed_users_by_process_date.objects(process_date=date).limit(5)

    op_json = []
    for item in users:
        op_json.append({
            'username': item.username,
            'qtd_followers': item.followers_count
        })

    resp = jsonify({'users': op_json})
    resp.status_code = 200

    return resp

@app.route("/tags", methods=["GET"])
def get_all_tags():
    t = Tweets_count_by_lang_tag.objects.all()

    op_json = []
    for item in t:
        op_json.append({
            'language': item.language,
            'tag': item.tag,
            'qtd': item.qtd
        })

    resp = jsonify({'tags': op_json})
    resp.status_code = 200

    return resp

@app.route("/tags/<string:lang>", methods=["GET"])
def get_tags_by_language(lang):
    t = Tweets_count_by_lang_tag.objects(language=lang)

    op_json=[]
    for item in t:
        op_json.append({
            'language': item.language,
            'tag': item.tag,
            'qtd': item.qtd
        })

    resp = jsonify({'tags':op_json})
    resp.status_code = 200

    return resp

# main app execution
if __name__ == '__main__':
    app.run()
