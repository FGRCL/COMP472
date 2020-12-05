import argparse
import pickle
import sys

from a3.naibebayes.naive_bayes import NaiveBayes
from a3.parser.tokenizer import parse_file, tweet_to_datapoints, filter_vocabulary

def predict(input_file, model_file, output_directory):
    model: NaiveBayes = pickle.load(open(model_file, 'rb'))

    trace_file_path = '{}trace_NB-BOW-OV'.format(output_directory)
    trace_file_line_template = "{}  {}  {}  {}  {}\n"
    eval_file_path = '{}eval_NB-BOW-OV.txt'.format(output_directory)
    eval_file_line_template = "{}  {}\n"

    total_instances = 0
    nb_correct_instances = 0
    true_yes = 0
    true_no = 0
    predicted_yes = 0
    predicted_no = 0
    total_yes = 0
    total_no = 0
    
    with open(trace_file_path, 'w+') as trace, open(eval_file_path, 'w+') as eval:
        for datapoint in parse_file(input_file):
            total_instances += 1
            print(datapoint)
            prediction = model.predict(datapoint[1])
            
            if prediction[1] == 'yes':
                predicted_yes += 1
            else:
                predicted_no += 1

            if datapoint[2] == 'yes':
                total_yes += 1
            else:
                total_no += 1

            is_correct_prediction = False
            if datapoint[2] == prediction[1]:
                is_correct_prediction = True
                nb_correct_instances += 1
                if datapoint[2] == 'yes':
                    true_yes += 1
                else :
                    true_no += 1

            # TRACE
            score_scientific = "{:.2e}".format(prediction[0])
            trace.write(trace_file_line_template.format(datapoint[0], prediction[1], score_scientific, datapoint[2], 'correct' if is_correct_prediction else 'wrong'))

        eval.write(eval_file_line_template.format(nb_correct_instances/total_instances,''))
        eval.write(eval_file_line_template.format(true_yes/predicted_yes, true_no/predicted_no))
        eval.write(eval_file_line_template.format(true_yes/total_yes, true_no/total_no))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="Predict with a model", description="A program to make predictions with a model")
    parser.add_argument('--input', '-i', help="Path to the tweets to predict", type=str, default="in/covid_test_public.tsv")
    parser.add_argument('--model', '-m', help="Path to the serialized model", type=str, default="model/bayes.pickle")
    parser.add_argument('--output', '-o', help="Path to the output folder", type=str, default="out/")
    args = parser.parse_args()

    predict(args.input, args.model, args.output)
