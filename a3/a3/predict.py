import argparse
import pickle
import sys

from a3.naibebayes.naive_bayes import NaiveBayes
from a3.parser.tokenizer import parse_file, tweet_to_datapoints, filter_vocabulary


def predict(input_file, model_file, output_file):
    model: NaiveBayes = pickle.load(open(model_file, 'rb'))

    for datapoint in parse_file(input_file):
        prediction = model.predict(datapoint[1])
        output_file.write(str(prediction))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="Predict with a model", description="A program to make predictions with a model")
    parser.add_argument('--input', '-i', help="Path to the tweets to predict", type=str, default="in/covid_test_public.tsv")
    parser.add_argument('--model', '-m', help="Path to the serialized model", type=str, default="model/bayes.pickle")
    parser.add_argument('--output', '-o', help="Path to the output file", type=open, default=sys.stdout)
    args = parser.parse_args()

    predict(args.input, args.model, args.output)
