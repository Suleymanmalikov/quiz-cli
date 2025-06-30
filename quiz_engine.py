from utils import write_wrong_answer_questions, empty_wrong_answer_questions

abcd = ["A", "B", "C", "D", "E", "F"]


def formatting_questions(question):
    print(f"\n{question['id']}. {question['question']}")
    print("\nChoices: ")
    for i in range(len(question["options"])):
        print(f"{abcd[i]}. {question['options'][i]}")


def check_answer(question, user_input):
    if user_input not in [
        letter.lower() for letter in abcd[: len(question["options"])]
    ]:
        return False

    selected_index = abcd.index(user_input.upper())
    selected_answer = question["options"][selected_index]

    correct_answer = question["answer"]
    return selected_answer == correct_answer


def explanation_for_wrong_answer(result, question):
    if result == False:
        write_wrong_answer_questions(question)
        print(
            f" - Correct answer:   {question['answer']!r}. \n - Explanation: {question["explanation"]} \n - Source: {question['slide_reference']}"
        )


def load_all_questions(questions):

    total = 0
    for question in questions:
        formatting_questions(question)
        user_input = input("Your answer: ").lower()
        result = check_answer(question, user_input)
        print(result)
        explanation_for_wrong_answer(result, question)
        total += 1
        if total % 10 == 0:
            continue_exit = input("\nDo you want to continue (Y/n): ").lower()
            if continue_exit == "n":
                exit()
        else:
            input()
