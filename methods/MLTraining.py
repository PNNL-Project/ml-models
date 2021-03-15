from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score, plot_confusion_matrix
from sklearn.neighbors import KNeighborsClassifier


"""
Helper Methods for ML Training
"""

def label_list_to_dict(label_list):
    """
    This maps the labels to the index location and returns it as a dictionary (key=label, val=index in list)
        args:
            label_list list List of prediction lables
        returns:
            label_dict dict Dictionary of  
    """
    label_dict = {}
    for idx, label in enumerate(label_list):
        label_dict[label] = idx
    return label_dict
        
def train_random_forest(X_train, X_test, y_train, y_test):
    """
    This trains a random forest ml model
        returns:
            rand_tree The random forest model
            confusion_matrix The confusion matrix plot for the random forest
    """
    rand_tree = RandomForestClassifier()
    rand_tree.fit(X_train, y_train)
    y_pred = rand_tree.predict(X_test)
    print(accuracy_score(y_test,y_pred))
    print(classification_report(y_test, y_pred))
    return rand_tree, plot_confusion_matrix(rand_tree, X_test, y_test, normalize="true")

def train_decision_tree(X_train, X_test, y_train, y_test):
    """
    This trains a decision tree ml model
        returns:
            tree The decision tree model
            confusion_matrix The confusion matrix plot
    """
    tree = DecisionTreeClassifier()
    tree = tree.fit(X_train, y_train)
    y_pred = tree.predict(X_test)
    print(accuracy_score(y_test,y_pred))
    print(classification_report(y_test, y_pred))
    return tree, plot_confusion_matrix(tree, X_test, y_test, normalize="true")

def train_knn(X_train, X_test, y_train, y_test):
    """
    This trains a decision tree ml model
        returns:
            knn_tree The knn model
            confusion_matrix The confusion matrix plot
    """
    knn_tree = KNeighborsClassifier(n_neighbors = 21)
    knn_tree.fit(X_train, y_train)
    y_pred = knn_tree.predict(X_test)
    print(accuracy_score(y_test,y_pred))
    print(classification_report(y_test, y_pred))
    return knn_tree, plot_confusion_matrix(knn_tree, X_test, y_test, normalize="true")