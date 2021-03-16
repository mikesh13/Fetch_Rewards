# Data Engineer Coding Exercise

This program is written to compare two texts and return a similarity score between 0 and 1.


0 means completely different and 1 indicates identical.


By running the bash file [run.sh](https://github.com/mikesh13/Fetch_Rewards/blob/main/run.sh), it will start a web service on localhost to perform the comparison.


The decisions I make to develop the solution are:
* I count both words and characters.
* Each word weight the same, no words matter more than others.
* The ordering of words is important to the comparison.
* I evaluate the similarity by using n-grams, which compare two texts using a block of word in order. n represents how many words are in a block. For each comparison, a maximum length is assigned. If the assigned number is 3. The program will run 1-grams, 2-grams, and 3-grams for the comparison. For each n-grams, the ratio of matched n-gram vs total number of n-gram is used to evaluate the similarity.
  * The default n is 3 for the n-grams.
  * The default assumption is all n-grams weight the same, but user can change the weight based on thier preferences.
* I did not use any library for the comparison, but I did use Flask to build a web service. 


The [CompareText.py](https://github.com/mikesh13/Fetch_Rewards/blob/main/CompareText.py) file contains a class for the comparison.
The comparison starts by createing a class object.
```
from CompareText import CompareTxt

txt1 = 'I like you.'
txt2 = 'I love you.'

comparison = CompareTxt(txt1, txt2)
```

Next, you want to make the comparison:
```
# Default longest_n_gram = 3
comparison.compare()

# If you want to specify the longest_n_gram
comparison.compare(5)
```

If you want to change the weight:
```
# New weight must have the same length as the old one, and it must sum up to 1.
comparison.change_weight([0.1, 0.3, 0.6])
```

To check the similarity_score:
```
print(comparison.get_similarity_score())
```

If you want to see the result of each n-grams:
```
print(comparison.similarity_score)
```
