python a3/train.py -i in/covid_training.tsv -o model/demo-model-OV.pickle
python a3/train.py -i in/covid_training.tsv -o model/demo-model-FV.pickle -f
python a3/predict.py -i in/test_set00.tsv -m model/demo-model-OV.pickle -t out/demo-trace_NB-BOW-OV.txt -e out/demo-eval_NB-BOW-OV.txt
python a3/predict.py -i in/test_set00.tsv -m model/demo-model-FV.pickle -t out/demo-trace_NB-BOW-FV.txt -e out/demo-eval_NB-BOW-FV.txt
