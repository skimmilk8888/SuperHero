from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline

class MachineLearning(object):
    def __init__(self):
        # Initialize classifier and vectorizer
        self.clf = Pipeline([('tfidf', TfidfVectorizer(min_df=1, ngram_range=(1, 2))),
                             ('clf', MultinomialNB(alpha=.01)),
                            ])

    def init_training(self):
        self.x_train = []
        self.y_train = []

    def add_training_data(self, data, label):
        self.x_train.append(data)
        self.y_train.append(label)

    # Train classifier
    # Can also use grid search to optimize accuracy, like
    '''
    parameters = {'tfidf__ngram_range': [(1, 1), (1, 2)],
                  'clf__alpha': (.01, .001),
    }
    gs_clf = GridSearchCV(clf, parameters, n_jobs=-1)
    '''
    def train(self):
        self.clf.fit(self.x_train, self.y_train)

    # Predict result
    # We can roughly estimate the accuracy using cross validation, like
    '''
    result = clf.predict(test_dc + test_marvel)
    baseline = [0 for x in range(len(test_dc))] + [1 for x in range(len(test_marvel))]
    print np.sum(result == baseline) / float(len(result))
    '''
    def predict(self, data):
        return self.clf.predict([data])[0]