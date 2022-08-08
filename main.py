from utils import get_by_skill, get_by_pk, get_all, load_candidates
from flask import Flask

app = Flask(__name__)
file = 'candidates.json'
data = get_all(load_candidates(file))


@app.route('/')
def index():
    string = ''
    for i in data:
        string += f'<pre>{i}</pre>'
    return string


@app.route('/candidates/<int:pk>')
def get_candidate(pk):
    user = get_by_pk(pk, data)
    if user:
        url = user.picture
        string = f"<img src='({url})'>"
        string += f'<pre>{user}</pre>'
        return string


@app.route('/skills/<x>')
def get_user(x):
    users = get_by_skill(x, data)
    string = ''
    for i in users:
        string += f'<pre>{i}</pre>'
    return string


if __name__ == '__main__':
    app.run()
