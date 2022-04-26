from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pickle


class UnigramMorphAnalyzer:

    def __init__(self):
        self.end_dict = dict()

    def train(self, x_train, y_train):
        counter = 1
        for word, tag in zip(x_train, y_train):
            word_ending = word[-4:]
            for i in range(len(word_ending)):
                word_end = word_ending[-i:]
                if not word_end:
                    break
                if word_end not in self.end_dict:
                    self.end_dict[word_end] = {tag: counter}
                elif word_end in self.end_dict and tag in self.end_dict[word_end]:
                    counter += 1
                    self.end_dict[word_end] = {tag: counter}
                elif word_end in self.end_dict and tag not in self.end_dict[word_end]:
                    self.end_dict[word_end][tag] = counter
        return self.end_dict

    def predict(self, word):
        stats = dict()
        word_ending = word[-4:]
        for i in range(len(word_ending)):
            word_end = word_ending[-i:]
            if not word_end:
                break
            if word_end in self.end_dict:
                stats = self.end_dict[word_end]
                break
        sum_values = sum(stats.values())
        for key, value in stats.items():
            stats[key] = round(value / sum_values, 3)
        try:
            return max(stats.keys())
        except ValueError:
            return 'UNKN'

    def eval(self, x_test, y_test):
        y_pred = []
        for i in x_test:
            y_pred.append(self.predict(i))
        return round(accuracy_score(y_test, y_pred) * 100, 2)

    def __getitem__(self, item):
        return self.end_dict[item]

    def save(self, file_name):
        with open(file_name, "wb") as f:
            pickle.dump(self, f)

    def load(self, file_name):
        with open(file_name, "rb") as f:
            tagger = pickle.load(f)
        return tagger


def main():
    with open('pos_data.txt', 'r', encoding='utf8') as f:
        x = []
        y = []
        for line in f:
            line = line.split()
            tag = line[1]
            word = line[0].lower()
            x.append(word)
            y.append(tag)
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)
    tagger = UnigramMorphAnalyzer()
    tagger.train(x_train, y_train)
    print(tagger.eval(x_test, y_test))
    print(tagger.predict('я'))
    print(f'Частеречная статистика по указанному окончанию: {tagger["я"]}')
    tagger.save('tagger.pkl')
    tagger = tagger.load('tagger.pkl')
    print(type(tagger))


if __name__ == '__main__':
    main()