import pandas as pd
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import recall_score
from sklearn.metrics import precision_score
from sklearn.metrics import f1_score
from sklearn.model_selection import StratifiedKFold
from joblib import dump, load
import numpy as np


def train():
    df = pd.read_table("datos.txt", delimiter=",", header=None)
    Y= df.iloc[:,-1:]
    df.drop(df.columns[len(df.columns)-1], axis=1, inplace=True)

    #Test del modelo
    skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=1)
    lista_acc=list()
    lista_recall=list()
    lista_precision=list()
    lista_fscore=list()

    testModel = GaussianNB()

    for train_index, test_index in skf.split(df, Y):
        x_train_fold, x_test_fold = df.iloc[train_index], df.iloc[test_index]
        y_train_fold, y_test_fold = Y.iloc[train_index], Y.iloc[test_index]
        testModel.fit(x_train_fold, y_train_fold.values.ravel())

        testOutput= testModel.predict(x_test_fold)

        lista_acc.append(accuracy_score(testOutput, y_test_fold))
        lista_fscore.append(f1_score(testOutput, y_test_fold))
        lista_precision.append(precision_score(testOutput, y_test_fold))
        lista_recall.append(recall_score(testOutput, y_test_fold,zero_division=0))

    #Output estadisitcas
    f = open("statsModelo.txt", "w")
    f.write("Accuracy: {valor} \n".format(valor= np.mean(lista_acc)))
    f.write("F-score: {valor} \n".format(valor= np.mean(lista_fscore)))
    f.write("Precision: {valor} \n".format(valor= np.mean(lista_precision)))
    f.write("Recall: {valor}".format(valor= np.mean(lista_recall)))
    f.close()

    '''
    X_train, X_test, y_train, y_test = train_test_split(df, Y, test_size=0.3, random_state=0)

    
    testModel.fit(X_train, y_train.values.ravel())
    testOutput= testModel.predict(X_test)
    tn, fp, fn, tp = confusion_matrix(y_test, testOutput).ravel()
    
    #recall
    recall = recall_score(y_test, testOutput)
    #precision
    precision = precision_score(y_test, testOutput)
    #f-score
    f1score = f1_score(y_test, testOutput)
    #accuracy
    score= accuracy_score(y_test, testOutput)
    print(score)
    '''
    
    clf = GaussianNB()
    clf.fit(df, Y.values.ravel())
    
    #name= '{name}.joblib'.format(name=modelName)
    #y_pred = clf.predict(X_test)
    dump(clf, "modeloEVOKA.joblib")
    return 1


def load_model(*args):
    
    clf = load('modeloEVOKA.joblib')
    predi= np.array(args).reshape(1,-1)
    
    
    return clf.predict(predi)[0]
    
    

'''
pred= [18,4263,5000,20100,167,1]
print(load_model(pred))
'''

