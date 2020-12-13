python a3/train.py -i in/covid_training.tsv -o model/model-OV.pickle
python a3/train.py -i in/covid_training.tsv -o model/model-FV.pickle -f
python a3/predict.py -i in/covid_test_public.tsv -m model/model-OV.pickle -t out/trace_NB-BOW-OV.txt -e out/eval_NB-BOW-OV.txt
python a3/predict.py -i in/covid_test_public.tsv -m model/model-FV.pickle -t out/trace_NB-BOW-FV.txt -e out/eval_NB-BOW-FV.txt

