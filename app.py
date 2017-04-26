from flask import Flask # Import Flask package
from flask import render_template # Import render_template function
app = Flask(__name__) # Construct Flask object named 'app'

'''
@app.route() defines the URLs that route to the index() function.
The URLs will be appended to the end of the base URL.
Links within HTML files should use the defined routes (for example '/index') as
the values for href attributes.

URLs that will call the index() function if running app.py on localhost:
	http://localhost:5000/
	http://localhost:5000/index
'''
@app.route('/') # URL for function (default for home page)
@app.route('/index') # Secondary URL for function
def index():
	return render_template('index.html') # located in templates/
	
@app.route('/about')
def about():
	return render_template('about.html')
	
@app.route('/comics')
def comics():
	return render_template('comics.html') # Example of argument passing to HTML template

@app.route('/authors')
def authors():
	return render_template('authors.html')

@app.route('/genres')
def genres():
	return render_template('genres.html')

@app.route('/Katie_Tiedrich')
def Katie_Tiedrich():
	return render_template('Katie Tiedrich.html')

@app.route('/Tim_Buckley')
def Tim_Buckley():
	return render_template('Tim Buckley.html')

@app.route('/Zack Morrison')
def Zack_Morrison():
	return render_template('Zack Morrison.html')

@app.route('/Awkward_Zombie')
def Awkward_Zombie():
	return render_template('awkward zombie.html')

@app.route('/Paranatural')
def Paranatural():
	return render_template('paranatural.html')

@app.route('/Ctrl+Alt+Del')
def CtrlAltDel():
	return render_template('Ctrl+Alt+Del.html')

@app.route('/action')
def action():
	return render_template('action.html')

@app.route('/comedy')
def comedy():
	return render_template('comedy.html')

@app.route('/fantasy')
def fantasy():
	return render_template('fantasy.html')

@app.route('/gag-a-day')
def gagaday():
	return render_template('gag-a-day.html')

@app.route('/parody')
def parody():
	return render_template('parody.html')

@app.route('/slice_of_life')
def slice_of_life():
	return render_template('slice of life.html')

if __name__ == '__main__':
	app.run() # Run application
