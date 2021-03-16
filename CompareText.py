'''
Author: Michael Shieh
Date: 3/12/2021

This file contains the Python class I wrote for the Fetch Rewards Coding Exercise - Data Engineer

This class is an application for a simplified version of Bilingual Evaluation Understudy (BLEU) algorithm.
It takes on two text for comparison purposes, 
and it will return a number between 0 and 1 by calling the function 'get_similarity_score'.
1 means exactly the same, and 0 means completely different.
'''
class CompareTxt:
    def __init__(self, template, content):
        '''
        template: a string contains a text
        content: a string contains a text

        For initialization, first read the two texts
        The first text is assigned as template,
        it is use to compare with the second text,
        which is the content that we want to know how similar it is to the template.
        '''
        self.similarity_score = []
        self.template_list = self._read_txt(template)
        self.template = " ".join(self.template_list)
        self.content = self._read_txt(content)
        
                    
    def _read_txt(self, txt):
        '''
        txt: a string contains a text

        This function takes on a string containing a texts,
        and break it into a list of all words and characters in the text.

        The words and characters in the list are in the same order as in the text.
        '''
        lst = []

        words = txt.split(" ")
        for word in words:
            word = self.transform_word(word.lower())
            for w in word:
                lst.append(w)

        return lst
    

    
    def compare(self, longest_n_gram = 3):
        '''
        longest_n_gram: a number indicate how long should the longest n-gram be, default to 3

        By calling this functions, the two texts will be compared,
        and it will create a list of numbers 
        representing the ratio of matched n-grams vs total number of n-grams.

        Additionally, it will create a default weight for the result of each number of n-grams.
        This weight can be changed by calling the function 'change_weight'.
        '''
        self.weight = [1/longest_n_gram]*longest_n_gram
        num_grams = len(self.content)
        for n in range(1, longest_n_gram + 1):
            sum_proportion = 0.0
            count = 0
            for j in range(0, len(self.content) - n + 1):
                gram = " ".join(self.content[j: j+n])

                if gram in self.template:
                    count += 1

            sum_proportion += count/num_grams
            num_grams -= 1
            self.similarity_score.append(sum_proportion)


    def transform_word(self, word):
        '''
        word: a string contains a word

        This function reads a word and bases on the condition it will return:
         - the exact word if the inputed word does not contain a character: you --> you
         - two words if the word is abbreviated: 'you'll' --> you will
         - a word and a character if the word contains a character in the end: you. --> you .

         The format of the return value is a list.
        '''
        if word[-1] == ',' or word[-1] == '.' or word[-1] == '?' or word[-1] == '!' or word[-1] == ';':
            return [word[:-1], word[-1]]
            
        elif '\'' in word:
            if word == 'don\'t':
                return ['do', 'not']
            elif word == 'doesn\'t':
                return ['does', 'not']
            elif word == 'didn\'t':
                return ['did', 'not']
            elif word == 'won\'t':
                return ['will', 'not']
        
            words = word.split('\'')
            if words[1] == 'll':
                return [words[0], 'will']
            elif words[1] == 's':
                return [words[0], 'is']
            elif words[1] == 're':
                return [words[0], 'are']
            elif words[1] == 'm':
                return [words[0], 'm']
            elif words[1] == 've':
                return [words[0], 'have']
        else:
            return [word]
    

    def get_similarity_score(self):
        '''
        By calling this function,
        it will calculate and return a similarity score of the two texts.

        

        If the two texts have no words in common, it will return 0
        '''
        if sum(self.similarity_score) == 0:
            return 0

        exp = 2.718281828459045
        len_template = len(self.template_list)
        len_content = len(self.content)
        if len_content > len_template:
            bp = 1
        else:
            bp = exp**(1 - (len_template/len_content))
        
        score = exp**sum([self.log(x)*y for x, y in zip(self.similarity_score, self.weight)])

        return round(bp*score, 3)

    
    def change_weight(self, new_weight):
        if len(new_weight) == len(self.weight) and sum(new_weight) == 1:
            self.weight = new_weight
        else:
            print("Invalid weight.")


    def log(self, x):
        if x == 0:
            return -1

        n = 1000.0
        return n*((x**(1/n)) - 1)