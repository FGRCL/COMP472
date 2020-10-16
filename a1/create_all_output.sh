python a1/main.py -m bayes -tr dataset/train_1.csv -ts dataset/test_with_label_1.csv -o out/bayes_1.csv
python a1/main.py -m bayes -tr dataset/train_2.csv -ts dataset/test_with_label_2.csv -o out/bayes_2.csv
python a1/main.py -m basedt -tr dataset/train_1.csv -ts dataset/test_with_label_1.csv -o out/basedt_1.csv
python a1/main.py -m basedt -tr dataset/train_2.csv -ts dataset/test_with_label_2.csv -o out/basedt_2.csv
python a1/main.py -m perceptron -tr dataset/train_1.csv -ts dataset/test_with_label_1.csv -o out/perceptron_1.csv
python a1/main.py -m perceptron -tr dataset/train_2.csv -ts dataset/test_with_label_2.csv -o out/perceptron_2.csv
python a1/main.py -m basemlp -tr dataset/train_1.csv -ts dataset/test_with_label_1.csv -o out/basemlp_1.csv
python a1/main.py -m basemlp -tr dataset/train_2.csv -ts dataset/test_with_label_2.csv -o out/basemlp_2.csv