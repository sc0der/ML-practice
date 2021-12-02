from sklearn.ensemble import RandomForestClassifier
clf = RandomForestClassifier(random_state=0)
X = [[1,  2,  3],  # 2 samples, 3 features
     [11, 12, 13]]
y = [0, 1]  # classes of each sample
pfit = clf.fit(X, y)
pred = clf.predict([[4, 5, 6], [14, 15, 16]])
print(pfit)
print(pred)
RandomForestClassifier(random_state=0)
