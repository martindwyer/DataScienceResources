from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

def logistic_regression(train):

    X = train[['Fare','na']]
    y = train['Survived']

    X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.30,
        random_state=101)

    logistic_model = LogisticRegression(max_iter=1000)

    logistic_model.fit(X_train,y_train)

    predictions = logistic_model.predict(X_test)

    print(classification_report(y_test, predictions))

