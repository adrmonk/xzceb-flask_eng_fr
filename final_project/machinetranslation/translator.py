import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

def english_to_french(english_text):
    """ translate english to french """
    translation = language_translator.translate(
    text = english_text,
    model_id = 'en-fr').get_result()
    french_text = translation['translations'][0]['translation']
    return french_text

def french_to_english(french_text):
    """ translate french to english """
    translation = language_translator.translate(
    text = french_text,
    model_id = 'fr-en').get_result()
    english_text = translation['translations'][0]['translation']
    return english_text

english = french_to_english('Bonjour')
print("French 'Bonjour' translated to English is ", english)

english = french_to_english("C'est la vie.")
print('French ', "C'est la vie.", ' translated to English is ', english)

english = french_to_english('Je habite à la rue Dagurerre.')
print("French 'Je habite à la rue Dagurerre.' translated to English is ", english)

french = english_to_french('Hello')
print("English 'Hello' translated to French is ", french)

french = english_to_french('What is your name?')
print("English 'What is your name?' translated to French is ", french)

french = english_to_french('Nice to meet you.')
print("English 'Nice to meet you.' translated to French is ", french)