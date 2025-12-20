from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    title = 'Home Page'
    return render_template('index.html', title=title)

@app.route('/about')
def about():
    title = 'About Page'
    name = 'Nattawut'
    email = 'std.67122420215@ubru.ac.th'
    mobile = '0836804693'
    age = 20
    return render_template('about.html',
                            name=name,
                            email=email,
                            mobile=mobile,
                            age=age)

@app.route('/favorite/foods')
def favorite_foods():
    title = 'Favorite Foods'
    foods = ['Pad kraprao', 'moo ping', 'Kai tod', 'Tom Kha Gai', 'Pad Thai']
    return render_template('favorite_foods.html',
                            foods=foods)

@app.route('/favorite/spots')
def favorite_spots():
    title = 'Favorite Spots'
    spots = ['Basketball', 'Boxing', 'Football']
    return render_template('favorite_spots.html',
                            spots=spots)

@app.route('/favorite/movies')
def favorite_movies():      
    title = 'Favorite Movies'
    movies = ['Avatar', 'The Lord of the Rings', 'Jaws', 'john wick', 'Home Alone']
    return render_template('favorite_movies.html',  
                            movies=movies) 

if __name__ == "__main__":
    app.run(debug=True)