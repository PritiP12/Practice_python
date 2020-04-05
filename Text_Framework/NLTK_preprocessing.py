from interfaces.preprocessing_interface import preprocessing_interface
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.corpus import stopwords
import nltk
import re
from string import punctuation

nltk.download('wordnet')
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')
nltk.download('stopwords')


class NLTK_preprocessing(preprocessing_interface):
    def __init__(self, text):
        self.__text = text
        self.__result = None

    def tokenization(self, parameter_dictionary):
        token_type = parameter_dictionary.get("token_type", "word")
        if token_type == "word":
            res = word_tokenize(self.__text)
        else:
            res = sent_tokenize(self.__text)
        self.__result = res
        return self.__result

    def stemming(self, paramete_dictionary):
        ps = PorterStemmer()
        words = word_tokenize(self.__text)
        Stem_res = []
        for word in words:
            Stem_res.append(ps.stem(word))
        return Stem_res

    def lemmatization(self, parameter_dictionary):
        lemmatizer = WordNetLemmatizer()
        words = word_tokenize(self.__text)
        Lemma_res = []
        for word in words:
            Lemma_res.append(lemmatizer.lemmatize(word))
        return Lemma_res

    def NER(self, parameter_dictionary):
        words = nltk.word_tokenize(self.__text)
        # for i in words[5:]:
        for i in str(words).split('\n'):
            tagged = nltk.pos_tag(words)
            namedEnt = (nltk.ne_chunk(tagged, binary=True))
            return namedEnt
            # namedEnt.draw()

    def POS(self, parameter_dictionary):
        tokens = word_tokenize(self.__text)
        POS_list = (nltk.pos_tag(tokens))
        return POS_list

    def remove_stopword(self, parameter_dictionary):
        stop_words = set(stopwords.words('english'))
        word_tokens = word_tokenize(self.__text)
        filtered_sentence = [w for w in word_tokens if not w in stop_words]
        filtered_sentence = []
        for w in word_tokens:
            if w not in stop_words:
                filtered_sentence.append(w)
        return filtered_sentence

    def Remove_emails(self, parameter_dictionary, ):
        sentence = self.__text
        emails = re.findall("([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)", sentence)
        lst_emails = []
        for mail in emails:
            lst_emails.append(mail)
        return lst_emails

    def remove_html_tags(self, parameter_dictionary):
        text = self.__text
        clean = re.compile('<.*?>')
        return re.sub(clean, '', text)

    def remove_number(self, parameter_dictionary):
        text = self.__text
        result = []
        for i in text:
            if not (i.isdigit()):
                result.append(i)
        return ''.join(result)

    def remove_punctuations(self, parameter_dictionary):
        text = self.__text
        res = []
        for i in text:
            if i not in punctuation:
                res.append(i)
        return ''.join(res)


    def remove_unicode(self, parameter_dictionary):
        text = self.__text
        result = re.sub(r'[^\x00-\x7f]', r'', text)
        return result

    def remove_tags(self, parameter_dictionary):
        text = self.__text
        result = ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)"," ",text).split())
        return result

    def replace_specialcharacter(self,parameter_dictionary):
        text = self.__text
        result = ' '.join(re.sub('[^A-Za-z0-9]+', ' ',text).split())
        return result

if __name__ == "__main__":
    nk = NLTK_preprocessing(
        "I am enjoying writing ;@joy#net"
        ";Hello from shubhamg199630@gmail.com ;<a href='http://example.com/'>\nI linked to <i>example.com</i></a>"
        "some\x00string. with\x15 funny characters")

    print(nk.tokenization({"token type": "word"}))
    print(nk.stemming({}))
    print(nk.lemmatization({}))
    print(nk.NER({}))
    print(nk.POS({}))
    print(nk.remove_stopword({}))
    print(nk.Remove_emails({}))
    print(nk.remove_html_tags({}))
    print(nk.remove_number({}))
    print(nk.remove_punctuations({}))
    print(nk.remove_unicode({}))
    print(nk.remove_tags({}))
    print(nk.replace_specialcharacter({}))
