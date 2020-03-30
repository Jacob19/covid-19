#!usr/bin/python
""" Main Entry point for Gerrit dashboard """

from flask import Flask, render_template
import config
import data

app = Flask(__name__, template_folder="")


@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def index_page():
    """! \brief  Index Page: This is the landing page of the application """
    stats, headers = data.get_stats()
    return render_template('index.html', stats=stats, headers=headers)


if (__name__ == '__main__'):
    """ Main Entry point for the App """
    print("Application Started")
    print("Running on  http://" + config.HOST + ":" + str(config.PORT_NO))
    app.run(host=config.HOST, port=config.PORT_NO, debug=config.DEBUG)
