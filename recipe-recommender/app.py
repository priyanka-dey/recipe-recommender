from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/ingredients', methods=['GET', 'POST'])
def ingredients():
	if request.method == 'POST':
		ingredients = request.form.getlist('ing[]')
		print(ingredients)
		# we will need to parse out the data so that it can pretty print
		data = [
			[
				'Asparagus Sandwich',
				['Asparagus', 'Cream Cheese', 'Tarragon', 'Salt', 'Black Pepper', 'Parmesan cheese', 'Butter', 'Bread'],
					[
						'Preheat the over to 400 F.',
						'Boil or steam the chopped asparagus for 3 minutes and then submerge in cold water. Mix the cooked asparagus with the softened cream cheese and tarragon, then add salt and pepper to taste.',
						'Melt the butter in a saucepan. Take each slice of bread and dip it into the melted butter and then sprinkle Parmesan cheese on one side of each piece.',
						'Spread about 1/2 cup of the cream-cheese/asparagus filling on a slice of bread on the non-coated side, and top with another slice, leaving the Parmesan-coated sides on the outside.'
						'Place assembled sandwiches on a greased sheet and bake in oven for 15-20 minutes, turning over once so both sides are browned.'
					]
			],
			[
				'Brownie in a Mug',
				['Flour', 'Sugar', 'Cocoa', 'Water', 'Canola oil', 'Vanilla'],
				[
					'Mix together all ingredients in a ramekin or other oven or microwave safe dish.',
					'Microwave for 1 minute.',
					'Bake in oven at 350 for 20 minutes or until toothpick comes out clean.'
				]
			]
		]
		return render_template('recipes.html', data=data)
	return render_template('ingredients.html')

@app.route('/')
def index():
	return render_template('index.html')

if __name__ == '__main__':
	app.run(debug=True)
