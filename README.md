### 🧪 ****Word Matching Function — Overview**** - **Pytest Test Suite**

This project tests a Python function that counts how many times a word appears in a string as a **standalone match**.
The test suite validates normal behaviour, edge cases, and invalid inputs.

🔹 **Function**: count_word_matches(text, target)
✔ **Purpose**

The function:

1. Accepts two inputs:

 - `text` → a string of words

 - `target` → a single word to search for

2. Counts how many times the target appears as a standalone word

   - Matching is **case-insensitive**

3. Returns the total number of matches.

📍 The implementation is located in:

    main.py

**🧠 How the Function Works**

**1. Word Matching Logic**

- A **standalone word** is defined as a sequence of characters separated by spaces.

- Matching is case-insensitive

`Example: "Cat" matches "cat"`

**2. Input Handling**

- The function splits the input text into words using spaces as delimiters.

- If either `text` or `target` is empty, the function returns:

0
**3. Counting Matches**

- Words are normalized to the same case

- Python’s `list.count()` is used to count exact matches in the split word list

| Text | Target | Expected Result | Notes |
|------|--------|-----------------|-------|
| `"The cat sat on the mat"` | `"cat"` | **1** | Only standalone match |
| `"Dog dog DOG dOg"` | `"dog"` | **4** | Case-insensitive |
| `"Hello world"` | `"world"` | **1** | Basic match |
| `"hello hello HELLO"` | `"hello"` | **3** | Multiple matches |
| `"No matches here"` | `"yes"` | **0** | No occurrences |
| `"catcat cat catdog"` | `"cat"` | **1** | Only standalone counts |
| `"a a a"` | `"a"` | **3** | Single-character matches |

### Exercise 2: Edge Case Testing ###
Test the **count_word_matches** function using parameterized tests. Focus on empty inputs, spaces, and punctuation. Implemented test cases are found in the test_count_word_matches_edge_cases.py file.

## ⚠️ Edge Case Test Scenarios

| Scenario | Text | Target | Expected | Notes |
|----------|------|--------|----------|-------|
| Empty text | `""` | `"word"` | **0** | No input text |
| Empty target | `"hello world"` | `""` | **0** | Nothing to match |
| Both empty | `""` | `""` | **0** | Function handles empty inputs |
| Multiple spaces | `"hello  world"` | `"world"` | **1** | Extra spaces ignored |
| Leading/trailing spaces | `" cat "` | `"cat"` | **1** | Trimmed during split |
| Punctuation limitation | `"cat,dog cat"` | `"cat"` | **1** | Only space-separated words counted |
| Single character | `"x y z"` | `"x"` | **1** | Works for short tokens |

### Exercise 3: Negative Testing ###
Test the function for invalid inputs like None, integers, or lists to ensure it raises the appropriate exceptions. Implemented test cases are found in the test_count_word_matches_negative.py file.

## ❌ Negative Test Scenarios (Invalid Inputs)

| Scenario | Text Input | Target Input | Expected Exception | Purpose |
|----------|------------|--------------|--------------------|---------|
| None text | `None` | `"word"` | **TypeError** | Reject non-string text |
| None target | `"hello world"` | `None` | **TypeError** | Reject non-string target |
| Integer text | `123` | `"word"` | **TypeError** | Enforce type safety |
| Integer target | `"hello world"` | `456` | **TypeError** | Prevent invalid comparisons |
| List as text | `["hello","world"]` | `"world"` | **TypeError** | Only strings allowed |
| List as target | `"hello world"` | `["world"]` | **TypeError** | Validate parameter type |

▶️ Running the Tests

1️⃣ Install pytest

    Install pytest in your environment (PyCharm terminal or system terminal):

    pip install pytest
2️⃣ Execute the test suite

From the project root directory, run:

    pytest -v

Or simply:

    pytest
