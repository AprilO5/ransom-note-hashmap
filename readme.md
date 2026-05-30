# Ransom Note Hashmap
**Lab GitHub Repo**: [Hash Tables - Ransom Note](https://github.com/learn-co-curriculum/hash-table-ransom-note-lab)

---

## Overview
This project applies a **hash map** pattern to solve a classic technical challenge: determine whether a **ransom note** can be constructed using the letters from a given **magazine**, with each letter used at most once.

In Python, the built-in `dict` type acts as the hash map. It stores **key-value pairs**, which makes it a strong fit for frequency counting, fast lookup, caching, text indexing, and validating data availability.

---

## Task 1: Define the Problem

1. Implement a function that returns `True` if a `ransomNote` can be built using letters from `magazine`, and `False` otherwise.
2. Each letter in `magazine` may only be used **once**.
3. Use a **hash map / dictionary** to track character counts.

**The Challenge**: Demonstrate the ability to use a hash map for character tracking, conditional logic, and a frequency-matching use case.

---

## Task 2: Determine the Design

### Hash Map Functionality

- **File**: `ransom_note.py`
- **Function**:  
  - `can_construct(ransomNote: str, magazine: str) -> bool`  
  - Returns `True` if the ransom note can be formed from magazine letters, `False` otherwise.

### Process

1. Initialize an empty dictionary to store character counts.
2. Loop through `magazine` and count how many times each character appears.
3. Loop through `ransomNote` and check whether each needed character is available.
4. Return `False` early if a character is missing or its count has been depleted.
5. Decrement the count after each character is used.
6. Return `True` when every ransom note character can be matched.

### Key Concepts

| Term | Project Use |
| --- | --- |
| Hash map / dictionary | Stores each magazine character and its count |
| Key | A character from the magazine or ransom note |
| Value | The number of times that character is available |
| `.get()` | Safely reads a count and returns `0` for missing characters |
| Frequency count | Tracks whether enough letters exist to build the note |
| Average lookup time | Dictionary lookup, insert, and update are typically `O(1)` |

---

## Task 3: Develop, Test, and Refine the Code

### Set Up

#### Fork and Clone
1. Go to the provided **GitHub repository link**.  
2. Fork the repository to your GitHub account.  
3. Clone the forked repository to your local machine.

#### Open and Run
1. Open the project in your Python-friendly IDE (VSCode, PyCharm, etc.).  

### Implementation Details

1. **Build the function**:
   - Track letter counts using a dictionary.
   - Decrement counts as you check the ransom note.
   - Return `False` early if a character is missing or depleted.

2. **Run Tests**:
   - Execute the test file with:
     ```bash
     python test_ransom_note.py
     ```
   - Ensure all tests pass before submission.

3. **Push and Merge**:
   - Commit your work regularly.
   - Push the completed solution to GitHub.

---

## Task 4: Document and Maintain

### Best Practice Documentation Steps

- **Comment your logic** when it helps explain hash map operations.
- **Explain your thinking** in function documentation.
- **README**: Ensure this file accurately reflects how to run the project.
- **Clean Up**:
  - Remove any debug prints.
  - Make sure `.gitignore` ignores `.pyc`, `__pycache__`, etc.

---

## Example

```python
can_construct("aa", "aab")
# True
```

The dictionary counts the available magazine letters:

```python
{"a": 2, "b": 1}
```

The function then spends those counts while checking the ransom note.

---

## Submission
Once your lab is complete and all tests are passing:

- Push your code to GitHub.
- Submit the link to your repo through **Canvas using CodeGrade**.
