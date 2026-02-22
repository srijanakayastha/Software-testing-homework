🧪 Word Matching Function — Pytest Test Suite
📌 Overview
This repository demonstrates professional Python testing practices using pytest. It focuses on validating a text-processing function through parameterized tests, edge-case coverage, and negative testing.
The goal of this project is to showcase:
* Clean test design
* Robust validation of real-world input scenarios
* Defensive programming practices
* Maintainable test architecture
This project is suitable as a portfolio example for QA, backend, and Python developer roles.

🧠 Core Functionality
🔹 count_word_matches(text, target)
The function counts how many times a target word appears as a standalone word in a string.
✔ Behavior
* Case-insensitive matching
* Words are separated by spaces
* Only exact standalone matches are counted
* Returns 0 if inputs are empty
* Raises TypeError for invalid input types
📍 Implementation Location


main.py


🧪 Testing Strategy
The test suite is designed to mirror real production-level validation layers.

✅ 1. Functional Tests (Parameterized)
File:


test_count_word_matches_basic.py

Validates:
* Normal usage scenarios
* Case-insensitive matching
* Word boundary handling
* Multiple occurrences
These tests ensure the function behaves correctly for typical inputs.

⚠️ 2. Edge-Case Tests
File:


test_count_word_matches_edge_cases.py

Covers:
* Empty strings
* Extra whitespace
* Leading/trailing spaces
* Single-character words
* Punctuation handling limitations
These tests ensure stability when processing messy real-world text.

❌ 3. Negative Tests (Defensive Validation)
File:


test_count_word_matches_negative.py

Ensures the function properly rejects invalid inputs:
* None
* Integers
* Lists
* Non-string parameters
This demonstrates type safety enforcement and error handling.

🧰 Tech Stack
* Python 3
* Pytest
* Parameterized testing
* Exception validation
* CLI-based test execution

⚙️ Setup & Installation
Clone the repository:


git clone <your-repo-url>
cd <repo-name>

Install dependencies:


pip install pytest


▶️ Running the Test Suite
Run all tests:


pytest -v

Or simply:


pytest


📁 Project Structure


.
├── main.py
├── test_count_word_matches_basic.py
├── test_count_word_matches_edge_cases.py
├── test_count_word_matches_negative.py
└── README.md



