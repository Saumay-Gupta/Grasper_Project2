# from transformers import pipeline
# from keybert import KeyBERT
# import spacy
import json

# Load models once globally
# sentiment_model = pipeline("sentiment-analysis")
# keybert_model = KeyBERT()
# try:
#     ner_model = spacy.load("en_core_web_sm")
# except OSError:
#     import os
#     os.system("python -m spacy download en_core_web_sm")
#     ner_model = spacy.load("en_core_web_sm")

def analyze_text(text,m):
    # key_phrases = keybert_model.extract_keywords(text, top_n=5, keyphrase_ngram_range=(1, 2))
    # doc = ner_model(text)
    # entities = [{'text': ent.text, 'label': ent.label_} for ent in doc.ents]
    if(m == "segment"):
        # sentiment = sentiment_model(text)
        return json.dumps(text+"segment")
    if(m == "keyphrase"):
        return json.dumps(text+"keyphrase")
    if(m == "entity"):
        return json.dumps(text+"entity")
    return json.dumps(text)

if __name__ == "__main__":
    import sys
    input_text = sys.argv[1]
    input_value = sys.argv[2]
    print(analyze_text(input_text,input_value))
