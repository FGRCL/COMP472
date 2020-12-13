[Repository URL](https://github.com/FGRCL/COMP472)
# Installing a3
use `poetry install` to install the environment then `poetry shell` to activate it  

# Running a3
activate your python environment if necessary

## Training the Model

***NOTE: Pre-generated models trained on the default training set can be found in the 'model' folder***

***NOTE: The default training and testing datasets can be found in the 'in' folder***

use `train.py` to train the model. The script has the following arguments.

```
  -h, --help    show this help message and exit
  --input/-i.   Path to the input file to use
  --filter/-f   Enables vocabulary filtering
  --output/-o,  Path to where the serialized model should be saved
```

Note: The model will be saved in a .pickle file at the location specified in the --output argument.

example: `python a3/train.py -i in/covid_training.tsv -o model/model-OV.pickle `

## Making a Prediction

use `predict.py` to make predictions on some testing set using the model created through the train.py script, which is saved in a .pickle file. The script has the following arguments.

```
  -h, --help,   show this help message and exit
  --input/-i,   Path to the tweets to predict
  --model/-m,   Path to the serialized model
  --trace/-t,   Path to the trace file
  --eval/-e,    Path to the eval file
```
example: `python a3/predict.py -i in/covid_test_public.tsv -m model/model-OV.pickle -t out/trace_NB-BOW-OV.txt -e out/eval_NB-BOW-OV.txt `

you can also use the convenient script `./create_all_output.sh` to train create the model and generate predictions using the default dataset.
