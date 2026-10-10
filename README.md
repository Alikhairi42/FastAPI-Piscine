# 🏊‍♂️ FastAPI Piscine - Intensive ASGI & REST API Bootcamp

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.142+-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Pydantic](https://img.shields.io/badge/Pydantic-v2-E92063?style=for-the-badge&logo=pydantic&logoColor=white)
![Uvicorn](https://img.shields.io/badge/Uvicorn-ASGI-4B8BBE?style=for-the-badge)

## 📌 About The Project
This repository contains my solutions for the **FastAPI Piscine**, a rigorous, 42-Network-style intensive bootcamp designed to teach the inner workings of FastAPI, the ASGI ecosystem, and modern Python backend development.

The curriculum strictly prohibits the use of external frameworks or databases (relying on in-memory process storage) to enforce a deep understanding of core mechanics: **Routing, Pydantic Validation, Dependency Injection, the Event Loop, and Concurrency.**

---

## 📚 Curriculum Breakdown

The piscine is divided into 6 modules (Days), culminating in a full RESTful CRUD API.

### **Day 00: Introduction to the ASGI Ecosystem**
- **Concepts:** ASGI vs WSGI, `uvicorn` server, separating the app instance from the server runner.
- **Key Learnings:** Creating a bare `FastAPI` instance, defining strict JSON responses, and implementing a `/health` availability route.

### **Day 01: Routing and Data Validation**
- **Concepts:** Path Parameters, Query Parameters, and Request Bodies.
- **Key Learnings:** Leveraging **Pydantic `BaseModel`** for automatic data validation. Understanding how FastAPI automatically intercepts bad data and raises `422 Unprocessable Entity` before the path operation is even executed.

### **Day 02: HTTP Status Codes and Exception Handling**
- **Concepts:** Domain rejections vs. Schema failures.
- **Key Learnings:** Manually raising `HTTPException` to handle `404 Not Found` and `400 Bad Request`. Ensuring the server never crashes into a `500 Internal Server Error` due to unhandled `KeyError` exceptions.

### **Day 03: Dependency Injection**
- **Concepts:** The `Depends()` mechanism (FastAPI's powerful alternative to traditional middlewares).
- **Key Learnings:** 
  - Creating a `verify_api_key` dependency to protect specific routes (`401 Unauthorized`).
  - Implementing a `pagination` dependency (`skip`, `limit` using `Query()`) to share logic across multiple endpoints without code duplication.

### **Day 04: RUSH - Library Management System**
- **Concepts:** Bringing it all together in a single, cohesive REST API.
- **Key Learnings:** Building a full CRUD lifecycle for a Book Catalogue. Handling unique ID generation, strict Pydantic payload validation on `POST` and `PUT`, and applying API Key dependencies exclusively to mutating routes while leaving `GET` routes public.

### **Day 05: Background Tasks and Concurrency**
- **Concepts:** The Event Loop, Threadpools, and Non-blocking I/O.
- **Key Learnings:** 
  - The critical difference between `def` (executed in an external threadpool) and `async def` (executed directly on the event loop).
  - Understanding why `time.sleep()` inside an `async def` freezes the entire server, and using `await asyncio.sleep()` instead.
  - Using `BackgroundTasks` to defer heavy synchronous/asynchronous workloads until after the HTTP response is dispatched.

---

## 🚀 Getting Started

### 1. Prerequisites
Ensure you have Python 3.10 or newer installed on your machine.

### 2. Installation & Setup
To test any of the days, you must create an isolated virtual environment and install the required packages.

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/fastapi-piscine.git
cd fastapi-piscine

# Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

# Install dependencies
pip install fastapi uvicorn pydantic

3. Running an Exercise
Navigate to any exercise directory and start the ASGI server using Uvicorn:

Bash

cd day04/
uvicorn main:app --reload
Once the server is running, navigate to the automatic Swagger UI documentation to test the endpoints interactively:
👉 http://127.0.0.1:8000/docs

📖 Recommended Resources
If you are transitioning from Node.js/Express.js (like I did) or just starting with FastAPI, these resources are invaluable:

Official FastAPI Documentation: Arguably one of the best technical documentations in the industry. Start with the Tutorial - User Guide.
Pydantic Documentation: Understand how data validation, serialization, and settings management work under the hood.
Uvicorn ASGI Server: Learn about the lightning-fast ASGI server implementation based on uvloop.
Real Python - Async IO in Python: A deep dive into the Event Loop, Coroutines, and why blocking code is the enemy of async/await.
FastAPI Dependencies (Middleware Alternative): Understand how FastAPI's Depends replaces traditional Node.js route-specific middlewares.
This subject and curriculum were designed by @khairi.