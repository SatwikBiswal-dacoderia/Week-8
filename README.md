# Python File Handling and Text Analysis 🐍

## Introduction

This repository contains my Python practice programs focused on **file handling, text processing, and character analysis**. These exercises are part of my ongoing Python learning journey and represent a step toward working with files and extracting useful information from text.

The main objective of these exercises was to learn how to create text files, write and read their contents, search for specific words, count words, and analyse text by identifying vowels, uppercase letters, lowercase letters, spaces, and digits.

## 📂 Programs

### 1. Creating a Text File, Entering Text, and Printing Its Contents

This program practises creating a text file, entering text into it, and displaying the stored contents.

**Concepts Practised:**
- File handling
- Creating and opening files
- Writing text to a file
- Reading file contents
- Printing output

### 2. Printing File Contents on Different Lines

This program practises displaying text from a file with each line printed separately.

**Concepts Practised:**
- Reading text files
- Newline characters
- Line-by-line output
- String formatting

This exercise helps develop an understanding of how text and line breaks are handled in files.

### 3. Checking Whether a Word Exists in a File

This program checks whether a particular word exists in a text file and displays the appropriate result.

**Concepts Practised:**
- File reading
- String searching
- Conditional statements
- User input
- Boolean conditions

This exercise introduces a basic method of searching text stored in a file.

### 4. Counting the Number of Words in a File

This program counts the words present in a text file.

**Concepts Practised:**
- File handling
- String methods
- Word splitting
- Lists
- Counting elements

This exercise helps me understand how file contents can be processed to extract simple statistics.

### 5. Counting Vowels, Uppercase Letters, Lowercase Letters, Spaces, and Digits

This program analyses text and counts different character categories, including vowels, uppercase letters, lowercase letters, spaces, and digits.

**Concepts Practised:**
- String traversal
- Loops
- Conditional statements
- Character checking
- Counters
- String methods such as `isupper()`, `islower()`, and `isdigit()`

This exercise helps me understand how to examine individual characters and calculate useful information about a piece of text.

## 🧠 Key Concepts Learned

Through these exercises, I practised:

- Creating and handling text files
- Writing data to files
- Reading file contents
- Processing text line by line
- Searching for words in text
- Counting words
- Iterating through strings
- Identifying vowels
- Checking uppercase and lowercase letters
- Identifying spaces and digits
- Using conditions and counters
- Extracting information from text

## 📄 Understanding File Handling

File handling allows a Python program to store information in files and access it later.

Python provides the built-in `open()` function to work with files. Common file modes include:

- `r` — read an existing file
- `w` — write to a file, creating it if necessary and replacing existing contents
- `a` — append text to an existing file or create it if it does not exist

A simple example of writing to and reading from a text file is:

```python
with open("sample.txt", "w") as file:
    file.write("Hello, Python!")

with open("sample.txt", "r") as file:
    content = file.read()
    print(content)
```

Using `with open(...)` helps ensure that the file is properly closed after the operation.

## 🔤 Understanding Text Analysis

Text analysis involves examining a string or file to identify patterns and count specific elements.

For example, Python can check whether a character is uppercase, lowercase, or a digit using built-in string methods. Loops and counters can then be used to count how many characters belong to each category.

These techniques are useful foundations for text-processing applications, log analysis, and other data-handling tasks.

## 🛠️ Technologies Used

- **Programming Language:** Python 3
- **Code Editor:** Visual Studio Code
- **Built-in Features:** File handling, strings, loops, and conditional statements

## ▶️ How to Run

1. Install Python 3 on your computer.
2. Clone or download this repository.
3. Open the project folder in VS Code or another Python-compatible editor.
4. Make sure any required text file is available in the correct location.
5. Run the Python program:

```bash
python filename.py
```

Replace `filename.py` with the name of the Python file you want to execute.

## 🎯 What I Learned

These exercises helped me understand how Python can work with information stored outside a program.

I practised creating files, writing and reading text, searching for words, counting words, and examining individual characters. I also strengthened my understanding of loops, conditional statements, string methods, and counter variables.

These skills will help me as I continue learning Python and move toward more practical programming projects.

## 📈 Learning Progress

- **Week 1:** Beginner Python projects
- **Week 2:** Basic problem-solving and string operations
- **Week 3:** List and tuple operations
- **Week 4:** Dictionary operations, calculations, and grading logic
- **Week 5:** Set operations and duplicate handling
- **Week 6:** Functions, recursion, and recursive list operations
- **Week 7:** While loops, number sequences, list traversal, and multiplication tables
- **Current Practice:** File handling, text processing, word searching, and character counting

## 🚀 What's Next?

My Python learning journey is still ongoing. I will continue exploring Python concepts, practising problem-solving, and building programs that apply these concepts together.

My goal is to develop strong programming fundamentals that will eventually support my learning in **Artificial Intelligence and Machine Learning (AIML), data structures, software development, and engineering projects**.

---

*This repository is part of my journey toward building strong programming, AIML, and software development skills through consistent hands-on practice.*

**Learn → Build → Understand → Share → Repeat**

*Master the fundamentals, then build.*
