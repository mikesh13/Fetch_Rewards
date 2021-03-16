'''
Author: Micheal Shieh
Date: 3/12/2021

This file contains the code for the web service to perform the comparison.
'''
from flask import Flask, render_template, request, redirect, url_for
from config import DevConfig
from CompareText import CompareTxt


app = Flask(__name__)
app.config.from_object(DevConfig)


@app.route('/')
def index():
	'''
	Opens index page
	'''
	return render_template("index.html")


@app.route('/compare_text', methods=['GET', 'POST'])
def compare_text():
	'''
	Opens the campare_text page for user to input the two texts,
	and a number for the maximum lengh of n-grams if they want to specify.
	'''
	return render_template("compare_text.html")


@app.route('/result', methods=['GET', 'POST'])
def result():
	'''
	Opens the result page
	
	When responding to a POST request, it will perform the comparison and print the result (similarity score).
	In other case, it will send users back to the index page.
	'''
	if request.method == 'POST':
		txt1 = request.form['text1']
		txt2 = request.form['text2']
		n = request.form['gram']

		comparison = CompareTxt(txt1, txt2)
		len_txt1 = len(comparison.template_list)
		len_txt2 = len(comparison.content)

		if len(n) > 0 and (int(n) > len_txt1 or int(n) > len_txt2):
			return redirect(url_for('error'))

		if len(n) > 0:
			comparison.compare(longest_n_gram=int(n))
		else:
			comparison.compare()
		score = str(comparison.get_similarity_score())
		
		return f'The similarity score of the two texts is {score}' 
		

	else:
		return render_template("index.html")


@app.route('/error')
def error():
	'''
	Opens the error page.
	When users input a number n for the n-grams that is longer than the text,
	they will be redirected to this page to notify them about the error.
	
	They will be redirected to the compare_text page afterwards.
	'''
	return render_template("error.html")


if __name__ == '__main__':
	app.run()
