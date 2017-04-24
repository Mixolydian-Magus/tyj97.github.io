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

@app.route('/base')
def base():
        return render_template('base.html')
	
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
			
@app.route('/action')
def action():
	return render_template('action.html')
		
@app.route('/awkwardzombie')
def awkwardzombie():
	return render_template('awkwardzombie.html')
		
@app.route('/comedy')
def comedy():
	return render_template('comedy.html')
		
@app.route('/Ctrl+Alt+Del')
def ctrl_alt_del():
	return render_template('Ctrl+Alt+Del.html')
		
@app.route('/fantasy')
def fantasy():
	return render_template('fantasy.html')
	
@app.route('/gag-a-day')
def gag_a_day():
	return render_template('gag-a-day.html')
		
@app.route('/Katie Tiedrich')
def katie_tiedrich():
	return render_template('Katie Tiedrich.html')
		
@app.route('/paranatural')
def paranatural():
	return render_template('paranatural.html')
	
@app.route('/parody')
def parody():
	return render_template('parody.html')
		
@app.route('/slice of life')
def slice_of_life():
	return render_template('slice of life.html')
		
@app.route('/Tim Buckley')
def tim_buckley():
	return render_template('Tim Buckley.html')
		
@app.route('/Zack Morrison')
def zack_morrison():
	return render_template('Zack Morrison.html')
	
if __name__ == '__main__':
	app.run() # Run application
