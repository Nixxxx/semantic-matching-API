import spacy
import pandas as pd
# load the pretrained language model from spacy, for test, choose the smalles LM
nlp = spacy.load("en_core_web_md")
# read csv files from source_segments.csv whose pattern is like "label_id_long;label_id;parent_id;segment_description;label_name"
# since the NLP realted information only relies on segment_description and label_name, one brief idea is to combine them.
df = pd.read_csv(r'source_segments.csv', delimiter=';', encoding='ISO-8859-1')
df['semantic_content'] = df['segment_description'].fillna('#') + " | " + df['label_name'].fillna('#')
semantic_contents = df['semantic_content'].tolist()

# send this list to spacy LM pipeline
docs = list(nlp.pipe(semantic_contents))
