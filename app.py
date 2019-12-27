from flask import Flask,render_template,request,jsonify, session, redirect, url_for
from hello import Bot

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'


@app.route('/restart')
def restart():
        session['game'] = Bot().__dict__
        return redirect(url_for('show'))


@app.route('/show_board',methods=["GET","POST"])
def show():
        if 'game' not in session:
            session['game'] = Bot().__dict__

        GamePlay = Bot()
        GamePlay.__dict__ = session.get('game')
        row=0
        col=0
        msg = ''
        if GamePlay.state != 0:
                    if GamePlay.state == 1:
                        msg = 'You won!!!'
                    elif GamePlay.state == 3:
                        msg = 'Match drawn'
                    else:
                        msg = 'You lost'

        if request.method=='POST':
                row=request.json['row']
                column=request.json['column']
                GamePlay.play(row,column)
                session['game'] = GamePlay.__dict__
                return jsonify({'board': GamePlay.game})
        return render_template("gamelook.html",gameboard=GamePlay.game, state=GamePlay.state, msg=msg)


if __name__ == '__main__':
        app.run(debug=True)
