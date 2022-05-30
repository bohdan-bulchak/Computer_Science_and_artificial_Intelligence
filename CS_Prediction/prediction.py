from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.svm import SVC
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import train_test_split
import numpy as np

X = np.load('X_public300.npy', allow_pickle=True)
y = np.load('y_public300.npy', allow_pickle=True)
E = np.load('X_eval300.npy', allow_pickle=True)


# Class marks encoding 180-200
oht = ColumnTransformer(
    [('one_hot_encoder', OneHotEncoder(),
      [180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199])],
    remainder='passthrough')

X_encoded = oht.fit_transform(X)
E_encoded = oht.transform(E)

# Combine data
X = np.hstack((X[:, 0:180], X_encoded[:, 0:180]))
E = np.hstack((E[:, 0:180], E_encoded[:, 0:180]))

# Split on train and test data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=1)

# Standardize data
sc = StandardScaler()
X_train[:, 0:180] = sc.fit_transform(X_train[:, 0:180])
X_test[:, 0:180] = sc.transform(X_test[:, 0:180])
E[:, 0:180] = sc.transform(E[:, 0:180])

# Fill missing num values 0-180 columns
si = SimpleImputer(missing_values=np.nan, strategy='mean')
X_train[:, 0:180] = si.fit_transform(X_train[:, 0:180])
X_test[:, 0:180] = si.transform(X_test[:, 0:180])
E[:, 0:180] = si.transform(E[:, 0:180])


# SVM algorithm with rbf kernel will be used for data classification
svm = SVC(kernel='poly', random_state=0, C=20,  degree=2, gamma='auto')

svm.fit(X_train, y_train)

y_predict = svm.predict(X_test)
E_predict = svm.predict(E)
print(roc_auc_score(y_test, y_predict))

np.save('y_predikcia.npy', E_predict)
