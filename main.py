from flask import Flask, render_template, request
from config import DevConfig
from CompareText import CompareTxt


app = Flask(__name__)
app.config.from_object(DevConfig)


@app.route('/')
def index():
	return render_template("index.html")


@app.route('/compare_text', methods=['GET', 'POST'])
def compare_text():
	return render_template("compare_text.html")


@app.route('/result', methods=['GET', 'POST'])
def result():
	if request.method == 'POST':
		txt1 = request.form['text1']
		txt2 = request.form['text2']
		n = request.form['gram']

		comparison = CompareTxt(txt1, txt2)
		len_txt1 = len(comparison.template_list)
		len_txt2 = len(comparison.content)

		if len(n) > 0 and (int(n) > len_txt1 or int(n) > len_txt2):
			return render_template("error.html")

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
	return render_template("error.html")


if __name__ == '__main__':
	app.run()
