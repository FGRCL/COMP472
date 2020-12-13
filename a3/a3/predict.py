import argparse
import pickle
import sys

from a3.naivebayes.naive_bayes import NaiveBayes
from a3.parser.tokenizer import parse_file, tweet_to_datapoints, filter_vocabulary


def predict(input_file, model_file, trace_file, eval_file):
    model: NaiveBayes = pickle.load(open(model_file, 'rb'))

    trace_file_line_template = "{}  {}  {}  {}  {}\n"
    eval_file_line_template = "{}  {}\n"

    total_instances = 0
    nb_correct_instances = 0
    true_yes = 0
    true_no = 0
    predicted_yes = 0
    predicted_no = 0
    total_yes = 0
    total_no = 0

    with open(trace_file, 'w+') as trace, open(eval_file, 'w+') as eval:
        for datapoint in parse_file(input_file):
            total_instances += 1
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
                else:
                    true_no += 1

            # TRACE
            score_scientific = "{:.2e}".format(prediction[0])
            trace.write(trace_file_line_template.format(
                datapoint[0], prediction[1], score_scientific, datapoint[2], 'correct' if is_correct_prediction else 'wrong'))

        accuracy, yes_prec, no_prec, yes_recall, no_recall, yes_F1, no_F1 = calculate_metrics(
            total_instances, nb_correct_instances, true_yes, true_no, predicted_yes, predicted_no, total_yes, total_no)

        eval.write("{}\n".format(accuracy))  # accuracy
        eval.write(eval_file_line_template.format(yes_prec, no_prec))  # precision
        eval.write(eval_file_line_template.format(yes_recall, no_recall))  # recall
        eval.write(eval_file_line_template.format(yes_F1, no_F1))  # F1-measure


def calculate_metrics(total_instances, predicted_instances, true_yes, true_no, pred_yes, pred_no, total_yes, total_no):
    accuracy = predicted_instances / total_instances
    yes_precision = true_yes / pred_yes
    no_precision = true_no / pred_no
    yes_recall = true_yes / total_yes
    no_recall = true_no / total_no
    yes_F1 = (2 * yes_precision * yes_recall)/(yes_precision + yes_recall)
    no_F1 = (2 * no_precision * no_recall)/(no_precision + no_recall)
    return accuracy, yes_precision, no_precision, yes_recall, no_recall, yes_F1, no_F1



if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="Predict with a model", description="A program to make predictions with a model")
    parser.add_argument('--input', '-i', help="Path to the tweets to predict", type=str, default="in/covid_test_public.tsv")
    parser.add_argument('--model', '-m', help="Path to the serialized model", type=str, default="model/bayes.pickle")
    parser.add_argument('--trace', '-t', help="Path to the trace file", type=str, default="out/trace_NB-BOW-OV.txt")
    parser.add_argument('--eval', '-e', help="Path to the eval file", type=str, default="out/eval_NB-BOW-OV.txt")
    args = parser.parse_args()

    predict(args.input, args.model, args.trace, args.eval)
