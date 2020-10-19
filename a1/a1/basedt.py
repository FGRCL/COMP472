from sklearn.tree import DecisionTreeClassifier, export_graphviz
from a1 import util

def train_model(training_dataset, features, labels):
    fileName = util.parseFileName(training_dataset)
    
    model = DecisionTreeClassifier()
    model.fit(features, labels)

    # Creating a grpah 
    # To run, I installed graphviz using poetry
    # Then to convert .dot file to png run $ dot -Tpng <FILE_NAME>.dot -o <FILE_NAME>.png
    export_graphviz(
        model,
        out_file=("../out/graphs/"+fileName+"-BaseDT.dot"),
        filled=True
    )
    
    return model