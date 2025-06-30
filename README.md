# 🧠 Quiz CLI - Interactive Exam Preparation Tool

A powerful command-line quiz application designed for effective exam preparation with smart wrong-answer tracking and multiple study modes.

## ✨ Features

- **📚 Multiple Quiz Modes**: Choose from three different study approaches
- **🔄 Smart Review System**: Automatically tracks wrong answers for focused review
- **🎲 Randomization**: Shuffle questions to avoid memorizing order
- **📊 Progress Tracking**: Shows results and detailed explanations instantly
- **⏸️ Batch Learning**: Pause every 10 questions to prevent fatigue
- **💾 Persistent Storage**: Saves your progress and mistakes for future sessions

## 🚀 Quick Start

### Prerequisites

- Python 3.7 or higher
- No external dependencies required (uses only standard library)

### Installation

1. **Clone or download** this repository
2. **Navigate** to the project directory:
   ```bash
   cd quiz-cli
   ```
3. **Run** the quiz:
   ```bash
   python main.py --help
   ```

## 📖 Usage

### Basic Commands

```bash
# Take all questions in order
python main.py --all

# Take all questions in random order
python main.py --shuffle

# Review only previously incorrect answers
python main.py --review
```

### Quiz Modes Explained

#### 🎯 All Mode (`--all`)

- Presents all questions in their original order
- Perfect for first-time learning or systematic review
- Option to clear previous wrong answers before starting

#### 🎲 Shuffle Mode (`--shuffle`)

- Randomizes question order to test true understanding
- Prevents pattern memorization
- Great for final exam preparation

#### 🔍 Review Mode (`--review`)

- Shows only questions you previously answered incorrectly
- Implements spaced repetition learning
- Perfect for targeted improvement

### Example Session

```bash
$ python main.py --shuffle
Do you want to empty the wrong questions (Y/n): n

1. What is the default Python version mentioned in the lecture?

Choices:
A. 3.10
B. 3.11
C. 3.12
D. 2.7
Your answer: c
True
```

## 📁 Project Structure

```
quiz-cli/
├── main.py              # Main application entry point
├── quiz_engine.py       # Core quiz logic and question handling
├── utils.py             # Utility functions for file operations
├── quiz_questions.json  # Main question database
├── wrong_answer.json    # Tracks incorrectly answered questions
├── Pipfile             # Python dependency management
└── README.md           # This file
```

## 🗃️ Question Format

Questions are stored in JSON format with the following structure:

```json
{
  "id": 1,
  "question": "What is the default Python version mentioned in the lecture?",
  "type": "multiple_choice",
  "options": ["3.10", "3.11", "3.12", "2.7"],
  "answer": "3.12",
  "explanation": "Slide 12 explicitly states Python 3.12 as the version used.",
  "slide_reference": "lecture_01.pdf#12"
}
```

### Supported Question Types

- **Multiple Choice**: 2-6 options (A, B, C, D, E, F)
- **True/False**: Binary choice questions

## 🎯 Learning Features

### Smart Wrong Answer Tracking

- Automatically saves questions you answer incorrectly
- Prevents duplicate entries
- Allows focused review of weak areas

### Immediate Feedback

For every question, you receive:

- ✅ **Correct/Incorrect** status
- 📝 **Detailed explanation**
- 📄 **Source reference** for further study

### Progress Management

- Pause every 10 questions to prevent cognitive overload
- Option to continue or exit at natural break points
- Clear wrong answer history when starting fresh

## 🛠️ Customization

### Adding Your Own Questions

1. Open `quiz_questions.json`
2. Add questions following the JSON format above
3. Ensure unique IDs for each question
4. Include explanations and source references

### Modifying Quiz Behavior

Key settings in `quiz_engine.py`:

- **Question batch size**: Modify the `total % 10` condition
- **Answer options**: Extend the `abcd` array for more choices
- **Display format**: Customize `formatting_questions()` function

## 🐛 Troubleshooting

### Common Issues

**"Error: quiz_questions.json not found!"**

- Ensure the JSON file exists in the same directory as main.py
- Check file permissions

**"Error: Invalid JSON in quiz_questions.json"**

- Validate your JSON syntax using an online JSON validator
- Common issues: missing commas, unmatched brackets

**No questions in review mode**

- This means you haven't answered any questions incorrectly yet
- Try other modes first to build up your wrong answer database

## 🤝 Contributing

Feel free to enhance this tool! Some ideas:

- Add more question types (fill-in-the-blank, ordering)
- Implement scoring statistics
- Add colored terminal output
- Create a web interface
- Export results to CSV

## 📝 License

This project is open source. Feel free to use, modify, and distribute as needed for educational purposes.

## 🙏 Acknowledgments

Perfect for students preparing for:

- Programming courses
- Certification exams
- Technical interviews
- Academic assessments

---

**Happy studying! 🎓**

_Built with ❤️ for effective learning_
