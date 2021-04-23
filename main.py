
from web_navigators.google_search import GoogleSearch, publication_time_since_yesterday
from file_utils.file_utils import write_json_file, write_utf8_json_file, read_json_file, append_to_json_file, append_to_utf8_json_file, read_utf8_json_file
from collections import Counter
import nltk 
from nltk.probability import FreqDist
from nltk.tokenize import word_tokenize
from nltk import pos_tag
from nltk import RegexpParser
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
from nltk.stem.porter import PorterStemmer

# google_driver = GoogleSearch()
# google_driver.search("bitcoin", publication_time_since_yesterday()) 
# url_news = google_driver.get_url_news()
# website_text = google_driver.extract_text_from_url(url_news[2])
# google_driver.close()

# write_json_file('urlsList.txt', url_news)
# write_utf8_json_file('website.txt', website_text)

website_text = read_utf8_json_file('website.txt')

tokenized_text = word_tokenize(website_text)
tokens_tag = pos_tag(tokenized_text)
# append_to_utf8_json_file("nplTest.txt",[item[0] for item in tokens_tag if item[1].startswith('N') or item[1].startswith('V')])
pair_words = nltk.bigrams([item[0] for item in tokens_tag if item[1].startswith('N') or item[1].startswith('V')])
append_to_utf8_json_file("nplTest.txt", list(Counter(pair_words)))

porter_stemmer  = PorterStemmer()
tokens_tag_stemmed = [(porter_stemmer.stem(token), tag) for token, tag in tokens_tag]
pair_stemmed_words = nltk.bigrams([item[0] for item in tokens_tag_stemmed if item[1].startswith('N') or item[1].startswith('V')])
append_to_utf8_json_file("nplTest.txt", list(Counter(pair_stemmed_words)))
# append_to_utf8_json_file("nplTest.txt",[item[0] for item in tokens_tag_stemmed if item[1].startswith('N') or item[1].startswith('V')])
# print(list(nltk.bigrams(tokens_tag_stemmed)))

patterns= "NP: {<[CDJNPV].*>+}"
chunker = RegexpParser(patterns)
output = chunker.parse(tokens_tag_stemmed)
# output.draw()

#Distribution of nouns
text_nouns = [item[0] for item in tokens_tag_stemmed if item[1].startswith('N')]
fdist1 = FreqDist(text_nouns)
# print(fdist1.most_common(50))
fdist1.plot(50, cumulative=True)


