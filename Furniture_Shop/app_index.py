from Furniture_Shop.libraries.xl_chung import *
import os

@app.route('/', methods=['GET', 'POST'])
def index():

	return render_template('Home/index.html')