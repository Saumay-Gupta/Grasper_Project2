import spacy
import nltk
# nltk.download('stopwords')
from nltk.corpus import stopwords
# nltk.download('punkt_tab')
from nltk.tokenize import word_tokenize
# import string
import json
from textblob import TextBlob

nlp = spacy.load("en_core_web_sm")

def analyze_text(text,s):
    result1 = ""
    result2 = ""
    result3 = ""
    if("segment" in s):
        blob = TextBlob(text)
        polarity = blob.sentiment.polarity
    
        if polarity > 0.1:
            sentiment = "positive"
        elif polarity < -0.1:
            sentiment = "negative"
        else:
            sentiment = "neutral"
    
        result1 = sentiment
        # return {
        #     # "text": text,
        #     "sentiment": sentiment,
        #     "polarity_score": round(polarity, 2)
        # }
    if("keyphrase" in s):
        # Preprocessing the text
        stop_words = set(stopwords.words("english"))
        tokens = word_tokenize(text)
    
        # Remove punctuation and stop words
        tokens = [word.lower() for word in tokens if word.isalpha() and word.lower() not in stop_words]
    
        # Use spaCy for noun phrase extraction
        doc = nlp(" ".join(tokens))
        key_phrases = [chunk.text for chunk in doc.noun_chunks]
    
        result2 = key_phrases
    if("entity" in s):
        # Process the text using the NLP model
        doc = nlp(text)
        # Extract entities and their labels
        entities = [(ent.text, ent.label_) for ent in doc.ents]
        # Print or return the entities
        # for entity, label in entities:
        #     print(f"Entity: {entity} | Label: {label}")
        # return entities
        result3 = entities
    output = {
        "segment": result1,
        "key": result2,
        "entity": result3
    }
    return json.dumps(output)

if __name__ == "__main__":
    import sys
    input_text = sys.argv[1]
    input_text2 = sys.argv[2]
    print(analyze_text(input_text,input_text2))
