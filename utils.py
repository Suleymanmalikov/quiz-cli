import json


def read_questions(filename):
    try:
        with open(filename, "r") as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print(f"Error: {filename} not found!")
        return []
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON in {filename}")


def write_wrong_answer_questions(question):
    try:
        with open("wrong_answer.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = []

    if not any(q["id"] == question["id"] for q in data):
        data.append(question)
        with open("wrong_answer.json", "w") as outfile:
            json.dump(data, outfile)


def empty_wrong_answer_questions():
    data = []
    with open("wrong_answer.json", "w") as outfile:
        json.dump(data, outfile)
