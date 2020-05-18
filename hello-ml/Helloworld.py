from sklearn import tree
#apple:0 =150,170 (bumpy)
#orange:1 =140,130 (Smooth)
features = [[140,1],[130,1],[150,0],[170,0]]
labels   = [0,0,1,1]

clf = tree.DecisionTreeClassifier()
clf =clf.fit(features,labels)
print(clf.predict([[140,0]]))

