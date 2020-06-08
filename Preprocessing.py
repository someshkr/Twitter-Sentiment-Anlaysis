# -*- coding: utf-8 -*-
"""
Created on Sun May 24 11:42:20 2020

@author: SOMESH
"""
import re
import nltk
#nltk.download()
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords


class Prep_text:

    def Preprocessing_text(self,text):
        lemmatizer = WordNetLemmatizer()
        text = text.lower()
        text = re.sub('\W+',' ', text)
        text = nltk.word_tokenize(text)    
        text = [lemmatizer.lemmatize(word) for word in text if word not in set(stopwords.words('english'))]   
        return text
    
    round1 = lambda x: Preprocessing_text(self,x)