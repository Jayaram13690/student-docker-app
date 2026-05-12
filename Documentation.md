# Dockerized Python OOP Student Management System

## 📌 Project Title
Dockerized Python Student Management System using OOP Concepts

---

# 📖 Project Overview

This project demonstrates how to:
- Develop a Python application using Object-Oriented Programming (OOP)
- Containerize the application using Docker
- Build and run Docker containers
- Push Docker images to Docker Hub

The application manages student details such as:
- Student ID
- Student Name
- Marks
- Total
- Percentage
- Result

---

# 🎯 Objectives

The main objectives of this project are:

- Understand Docker fundamentals
- Learn how Docker containers work
- Implement OOP concepts in Python
- Create and run Docker images
- Deploy Docker images to Docker Hub

---

# 🛠 Technologies Used

| Technology | Purpose |
|---|---|
| Python 3.11 | Application development |
| Docker | Containerization |
| Docker Hub | Cloud image repository |
| VS Code / Terminal | Development environment |

---

# 📁 Project Structure

```text
student-docker-app/
│
├── app.py
└── Dockerfile
```

---

# 🐍 Python Application Explanation

## 📄 File: `app.py`

This file contains the Student Management System developed using Python OOP concepts.

---

# 🔹 Step 1: Creating the Class

```python
class Student:
```

### Explanation
- `class` is used to create a blueprint for objects.
- `Student` is the class name.

The class represents student data and behavior.

---

# 🔹 Step 2: Constructor Method

```python
def __init__(self, student_id, name, marks):
```

### Explanation
The constructor initializes object data automatically when an object is created.

### Parameters

| Parameter | Purpose |
|---|---|
| `student_id` | Stores student ID |
| `name` | Stores student name |
| `marks` | Stores subject marks |

---

# 🔹 Step 3: Instance Variables

```python
self.student_id = student_id
self.name = name
self.marks = marks
```

### Explanation
- `self` refers to the current object.
- These variables store object-specific data.

---

# 🔹 Step 4: Total Calculation Method

```python
def calculate_total(self):
    return sum(self.marks)
```

### Explanation
- Calculates total marks using Python’s `sum()` function.
- Returns total marks.

Example:

```text
[85, 90, 88] → 263
```

---

# 🔹 Step 5: Percentage Calculation

```python
def calculate_percentage(self):
```

### Explanation
- Calculates percentage by dividing total marks by number of subjects.

### Formula

```text
Percentage = Total Marks / Number of Subjects
```

---

# 🔹 Step 6: Result Calculation

```python
def get_result(self):
```

### Explanation
Checks student performance using conditions.

| Percentage | Result |
|---|---|
| ≥ 75 | Distinction |
| ≥ 50 | Pass |
| < 50 | Fail |

---

# 🔹 Step 7: Display Method

```python
def display_details(self):
```

### Explanation
Displays all student details:
- Student ID
- Name
- Marks
- Total
- Percentage
- Result

---

# 🔹 Step 8: Creating Objects

```python
student1 = Student(101, "Jayaram", [85, 90, 88])
student2 = Student(102, "Rahul", [45, 50, 55])
```

### Explanation
Objects are created from the `Student` class.

Each object stores separate student data.

---

# 🔹 Step 9: Calling Methods

```python
student1.display_details()
student2.display_details()
```

### Explanation
Calls the display method for each object.

---

# 🐳 Docker Explanation

Docker is used to package the Python application and its dependencies into a container.

---

# 📄 Dockerfile Explanation

## File: `Dockerfile`

```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY . .
CMD ["python", "app.py"]
```

---

# 🔹 Line-by-Line Explanation

## 1️⃣ Base Image

```dockerfile
FROM python:3.11-slim
```

### Explanation
- Downloads official lightweight Python image.
- Acts as base operating environment.

---

## 2️⃣ Working Directory

```dockerfile
WORKDIR /app
```

### Explanation
Sets `/app` as the working directory inside container.

---

## 3️⃣ Copy Files

```dockerfile
COPY . .
```

### Explanation
Copies all project files into Docker container.

---

## 4️⃣ Run Application

```dockerfile
CMD ["python", "app.py"]
```

### Explanation
Runs the Python application automatically when container starts.

---

# 🚀 Building Docker Image

## Command

```bash
docker build -t student-app .
```

---

# 🔹 Command Explanation

| Part | Meaning |
|---|---|
| `docker build` | Builds Docker image |
| `-t` | Adds image tag |
| `student-app` | Image name |
| `.` | Current directory |

---

# ▶️ Running Docker Container

## Command

```bash
docker run -it student-app
```

### Explanation
Starts a container using the created image.

---

# ✅ Output

```text
----- Student Details -----
Student ID : 101
Name       : Jayaram
Marks      : [85, 90, 88]
Total      : 263
Percentage : 87.67%
Result     : Distinction
```

---

# ☁️ Docker Hub Explanation

Docker Hub is a cloud repository used to store Docker images online.

---

# 🔐 Docker Login

```bash
docker login
```

### Purpose
Authenticates Docker account.

---

# 🏷 Tagging Docker Image

```bash
docker tag student-app jayaram3437/student-app:v1
```

---

# 🔹 Tag Format

```text
username/repository-name:version
```

Example:

```text
jayaram3437/student-app:v1
```

---

# 📤 Push Image to Docker Hub

```bash
docker push jayaram3437/student-app:v1
```

### Explanation
Uploads Docker image to Docker Hub.

---

# 📥 Pull Image from Docker Hub

```bash
docker pull jayaram3437/student-app:v1
```

---

# 🔄 Run Pulled Image

```bash
docker run jayaram3437/student-app:v1
 or 
docker run -it jayaram3437/student-app:v1
```

---

# 🧠 OOP Concepts Used

| OOP Concept | Implementation |
|---|---|
| Class | `Student` |
| Object | `student1`, `student2` |
| Constructor | `__init__()` |
| Methods | `calculate_total()` |
| Encapsulation | Data stored inside objects |
| Abstraction | Result logic hidden in methods |

---

# ✅ Advantages of Docker

| Advantage | Description |
|---|---|
| Portability | Runs anywhere |
| Lightweight | Faster than virtual machines |
| Isolation | Separate environment |
| Consistency | Same behavior everywhere |
| Scalability | Easy deployment |

---

# 📌 Conclusion

This project successfully demonstrates:
- Python OOP concepts
- Docker containerization
- Docker image creation
- Running containers
- Docker Hub integration

The application was successfully built, containerized, executed, and deployed using Docker technologies.

---
