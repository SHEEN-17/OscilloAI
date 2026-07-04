import argparse
import sys


def train():

    from trainer.train import train

    train()


def evaluate():

    from trainer.evaluate import evaluate

    evaluate()


def predict(image):

    from trainer.predict import predict

    predict(image)


def gui():

    from app.main import main

    main()


def main():

    parser = argparse.ArgumentParser()

    sub = parser.add_subparsers(dest="command")

    sub.add_parser("train")

    sub.add_parser("evaluate")

    gui_parser = sub.add_parser("gui")

    predict_parser = sub.add_parser("predict")

    predict_parser.add_argument("image")

    args = parser.parse_args()

    if args.command == "train":

        train()

    elif args.command == "evaluate":

        evaluate()

    elif args.command == "predict":

        predict(args.image)

    elif args.command == "gui":

        gui()

    else:

        parser.print_help()


if __name__ == "__main__":

    main()