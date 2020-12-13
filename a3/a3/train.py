import argparse
import pickle

from a3.naivebayes.naive_bayes import NaiveBayes
from a3.parser.tokenizer import parse_file, tweet_to_datapoints, filter_vocabulary


def train(input_file: str, output_file: str, use_filter: bool) -> None:
    datapoints = tweet_to_datapoints(
        parse_file(input_file)
    )

    if use_filter:
        datapoints = filter_vocabulary(datapoints, 2)

    model = NaiveBayes()
    model.train(datapoints)

    pickle.dump(model, open(output_file, "wb"))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog="Train the model", description="A program to train the naive bayes classifier")
    parser.add_argument('--input', '-i', help="Path to the input file to use", type=str, default="in/covid_training.tsv")
    parser.add_argument('--filter', '-f', help="Enables vocabulary filtering", action="store_true")
    parser.add_argument('--output', '-o', help="Path to where the serialized model should be saved", type=str, default="model/bayes.pickle")
    args = parser.parse_args()

    train(args.input, args.output, args.filter)
