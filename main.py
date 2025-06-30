import argparse
import random

from utils import read_questions
from quiz_engine import (
    load_all_questions,
    empty_wrong_answer_questions,
)


def main():
    parser = argparse.ArgumentParser(
        description="Choose one quiz mode: --all, --shuffle, or --review"
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--all", action="store_true", help="Ask all questions in order")
    group.add_argument(
        "--shuffle", action="store_true", help="Ask all questions in random order"
    )
    group.add_argument(
        "--review", action="store_true", help="Ask only previously incorrect questions"
    )

    args = parser.parse_args()

    if args.all:
        questions = read_questions("quiz_questions.json")
        user_empty_or_not = input("Do you want to empty the wrong questions (Y/n): ")
        if user_empty_or_not != "n":
            empty_wrong_answer_questions()
        load_all_questions(questions)
    elif args.shuffle:
        questions = read_questions("quiz_questions.json")
        if not questions:
            print("No questions found to shuffle.")
            return
        random.shuffle(questions)
        user_empty_or_not = input("Do you want to empty the wrong questions (Y/n): ")
        if user_empty_or_not != "n":
            empty_wrong_answer_questions()
        load_all_questions(questions)
    elif args.review:
        questions = read_questions("wrong_answer.json")
        load_all_questions(questions)


if __name__ == "__main__":
    main()
