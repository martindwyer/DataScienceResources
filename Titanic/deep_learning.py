import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
import matplotlib.pyplot as plt

from sklearn.preprocessing import MinMaxScaler

import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation, Dropout
from tensorflow.keras.callbacks import EarlyStopping

from numba import cuda

def deep_learning(train):
    X = train.drop(['Survived','Surname','Age','Fare'],axis=1)
    y = train['Survived']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20,
                                                        random_state=101)

    scaler = MinMaxScaler()

    scaler.fit(X_train)

    X_train = scaler.transform(X_train)
    X_test = scaler.transform(X_test)

    model = Sequential()

    model.add(Dense(units=8, activation='relu'))
    model.add(Dense(units=4, activation='relu'))
    model.add(Dense(units=2, activation='relu'))

    model.add(Dense(units=1, activation='sigmoid'))

    model.compile(loss='binary_crossentropy', optimizer='adam')

    early_stop = EarlyStopping(monitor='val_loss', mode='min', verbose=1, patience=25)

    model.fit(x=X_train,
              y=y_train,
              epochs=400,
              validation_data=(X_test, y_test), verbose=1,
              callbacks=[early_stop]
              )

    model_loss = pd.DataFrame(model.history.history)

    model_loss.plot()
    plt.show()

    predictions = model.predict_classes(X_test)

    print(classification_report(y_test, predictions))
    print(confusion_matrix(y_test, predictions))

    cuda.select_device(0)
    cuda.close()
    print('CUDA memory released: GPU0')
    
