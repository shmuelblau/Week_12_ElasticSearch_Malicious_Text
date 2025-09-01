import pandas as pd
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer


class Processor:
    

    @staticmethod
    def loadnitk():
        nltk.download('vader_lexicon')# Compute sentiment labels
    

    @staticmethod
    def get_emotion(text):

        score=SentimentIntensityAnalyzer().polarity_scores(text)

        return "positive" if score["compound"] > 0.5 else "negative" if score["compound"] < -0.5 else "neutral"
    
    @staticmethod
    def get_weapon( text:str , weapons):
        result = []
        for weapon in weapons:
            if weapon.lower() in text.lower():
                result.append(weapon)
        return result

    
        