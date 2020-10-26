from nltk.corpus import stopwords
import nltk


def clean_stop_words(sentence, language='russian'):
	stop_words = set(stopwords.words(language))
	words = nltk.word_tokenize(sentence)
	without_stop_words = [word for word in words if not word in stop_words]
	return without_stop_words


print(clean_stop_words("Привет какая будет погода на завтра?"))