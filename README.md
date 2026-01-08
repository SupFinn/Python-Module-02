> *This project has been created as part of the 42 curriculum by rhssayn.*

# 🌱 Garden Guardian  
### *Data Engineering for Smart Agriculture*

---

## 📌 Description

**Garden Guardian** is a Python project focused on **resilient data engineering** for smart agriculture systems.

Building on previous Python foundations, this project introduces **exception handling**, **fault tolerance**, and **robust system design** through realistic agricultural scenarios. You will simulate sensor data pipelines, handle unexpected failures, and ensure that your digital garden continues to function even when things go wrong.

In real-world farming systems, data is never perfect. Sensors fail, inputs are corrupted, and networks become unreliable. This project teaches you how to design programs that **expect failure and recover gracefully**.

---

## 🎯 Project Objectives

Through this project, you will learn how to:

- 🌾 Validate and protect agricultural data streams  
- 🛑 Handle runtime errors without crashing programs  
- 🧠 Understand Python’s exception hierarchy  
- 🧩 Create and use custom exception types  
- 🧪 Build fault-tolerant systems using `try / except / finally`  
- 🔁 Ensure programs continue running despite errors  

---

## 🧪 Exercises Overview

### 🌡️ Exercise 0 — Agricultural Data Validation Pipeline
Validate temperature data coming from sensors and user input. Learn how to safely convert data types and reject invalid or extreme values without stopping the program.

---

### ⚠️ Exercise 1 — Different Types of Problems
Explore common Python error types such as `ValueError`, `ZeroDivisionError`, `FileNotFoundError`, and `KeyError`. Learn how to catch them individually or together while keeping the program running.

---

### 🧬 Exercise 2 — Making Your Own Error Types
Create custom exception classes tailored to garden-specific problems. Use inheritance to group related errors and simplify error handling logic.

---

### 🧹 Exercise 3 — Finally Block: Always Clean Up
Learn how to use the `finally` block to guarantee cleanup actions, even when errors occur. Simulate opening and closing a watering system reliably.

---

### 🚨 Exercise 4 — Raising Your Own Errors
Detect invalid conditions in your program and raise meaningful errors using `raise`. Learn how to communicate problems clearly through helpful error messages.

---

### 🌿 Exercise 5 — Garden Management System
Combine everything into a complete garden management system. Use custom exceptions, validation, cleanup logic, and error recovery to build a resilient agricultural monitoring program.

---

## ⚙️ Rules & Constraints

- Python **3.10+**
- Code must follow **flake8** standards
- Each exercise must be in its own file
- Programs must **never crash**
- Use clear and simple logic
- Demonstrate both:
  - Normal execution
  - Error handling scenarios
- Use built-in exceptions appropriately
- Include simple docstrings for functions and classes

---

## 🧪 Testing Your Work

Each exercise includes a test function demonstrating:

- Valid input
- Invalid input
- Error recovery
- Continued execution

You can run each file using:

```bash
python3 your_file.py
```

## 👤 Author

**Redouane Hssayn (Finn)/(rhssayn)**
Student at **1337 - 42 Network**

If this project helps you, feel free to ⭐ the repository on GitHub!