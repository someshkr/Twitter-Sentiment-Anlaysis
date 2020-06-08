# -*- coding: utf-8 -*-
"""
Created on Sun May 24 11:26:17 2020

@author: SOMESH
"""
import pandas as pd
from textblob import TextBlob

class Sent_Sub:
    def sentimentCreation(df,col_name,pol):
        df[col_name] = df['content'].apply(pol)
        df.loc[df[col_name] > 0 , 'Sentiment'] = 'POSITIVE'
        df.loc[df[col_name] < 0 , 'Sentiment'] = 'NEGATIVE'
        df.loc[df[col_name] == 0 , 'Sentiment'] = 'NEUTRAL'
        return df
    
    def subjectiveCreation(df,col_name,sub):
        df[col_name] = df['content'].apply(sub)
        df.loc[df[col_name] > 0 , 'Subjective'] = 'SUBJECTIVE'
        df.loc[df[col_name] < 0 , 'Subjective'] = 'OBJECTIVE'
        df.loc[df[col_name] == 0 , 'Subjective'] = 'NEUTRAL'
        return df
