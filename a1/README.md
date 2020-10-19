# Installing a1
use `poetry install` to install the environment then `poetry shell` to activate it  
or  
install the following dependencies manually
```
python = "^3.8"
numpy = "*"
scikit-learn = "*"
matplotlib = "*"
graphviz = "^0.14.2"
pandas = "*"
```
# Running a1
activate your python environment if necessary

## Plotting the datasets
use `plotDataset.py` to plot datasets. The script has the following arguments.
```
  -h, --help      show this help message and exit
  --dataset path  the path to dataset
```
example: `python a1/plotDataset.py --dataset dataset/train_1.csv`


## Making predictions with models
use `main.py` to make model predictions. The script has the following arguments.

```
  -h, --help            show this help message and exit
  --trainingset/-tr, training set path
                        the path to training set
  --testset/-ts, test set path
                        the path to test set
  --output/-o, the path to the ouput file
                        the path to training set
  --model/-m, {bayes, basedt, bestdt, perceptron, basemlp, bestmlp}
                        The model to train

```
example: ` python a1/main.py -tr dataset/train_1.csv -ts dataset/test_with_label_1.csv -o out/GNB-DS1.txt -m bayes       `

you can also use the convenience script `./create_all_output` to generate predictions with all models and datasets.

## Performing a gridsearch

use `main.py` to make a grid search of hyper parameters. Grid search is only available for the bestdt and bestmlp models. The script has the following arguments.

```
--trainingset/-tr, training set path
                        the path to training set
  --validationset/-vs, validation set path
                        the path to the validation set
  --graphoutput/-go, output for the graph
  --model/-m, {bayes, basedt, bestdt, perceptron, basemlp, bestmlp}
                        The model to train
```