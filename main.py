from nltk.corpus import stopwords
import nltk
import commands
from src.functions import web_api


def clean_stop_words(sentence, language='russian'):
	stop_words = set(stopwords.words(language))
	words = nltk.word_tokenize(sentence)
	without_stop_words = [word for word in words if not word in stop_words]
	return without_stop_words


def check_command(text):

	string_text = ''

	for i in text:
		string_text += i + ' '

	if string_text.lower().strip() in commands.commands["cmd"]["weather"]:
		return web_api.get_weather()


print(check_command(clean_stop_words("какая сейчас погода")))