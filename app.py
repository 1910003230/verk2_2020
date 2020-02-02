from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
	return '<h1>Verkefni 2...</h1><a href="/partA">Part A Kennitala</a><h1></h1><a href="/partB">Part B Fréttir</a> '

listiA= [['Nikki:', '1910003230'], ['Kaleb:', '0104004340']]

@app.route('/sida/1910003230')
def suma():
	return '<h1>Þversuma</h1> Þversumma kennitölunnar <b>1910003230</b> er <b>19</b>'

@app.route('/sida/0104004340')
def suma1():
	return '<h1>Þversuma</h1> Þversumma <b>0104004340</b> er <b>16</b>'

@app.route('/partA')
def sida1():
	return render_template("verk2A.html", listiA=listiA) 

@app.route('/partB')
def sida2():
	return render_template("verk2B.html", listiA=listiA)

if __name__ == "__main__":
	app.run(debug=True)
                    