

## ✅ **What is FastAPI?**

FastAPI is a **modern**, **fast (high-performance)** web framework for building APIs with **Python 3.7+**.
It is used to create RESTful APIs quickly and efficiently, leveraging **Python type hints** for data validation and documentation.

---

## 🎯 **Why is FastAPI Used?**

| Feature                   | Explanation                                                                       |
| ------------------------- | --------------------------------------------------------------------------------- |
| ✅ **Speed**               | One of the fastest Python frameworks, comparable to Node.js & Go.                 |
| 📦 **Data validation**    | Built-in using **Pydantic** with automatic request validation.                    |
| 📝 **Auto Documentation** | Comes with **Swagger UI** and **ReDoc** for free API docs.                        |
| 🧠 **Type safety**        | Uses Python type hints for better editor support, autocompletion & static checks. |
| 🔒 **Security**           | Built-in OAuth2, JWT, and other modern security standards.                        |
| 📁 **Async support**      | Supports `async` and `await` out of the box for non-blocking APIs.                |
| 🌐 **Production ready**   | Used by Netflix, Uber, Microsoft, etc.                                            |

---

## 🚀 Why is FastAPI Fast?

FastAPI is **fast** because:

### 1. **Asynchronous support (AsyncIO)**

* Handles many requests at once using `async def` without blocking threads.

### 2. **Starlette (ASGI framework)**

* FastAPI is built on **Starlette** which is a lightweight ASGI (Asynchronous Server Gateway Interface) toolkit.
* Starlette provides routing, middleware, background tasks, WebSockets, and more.

### 3. **Pydantic (for validation)**

* FastAPI uses **Pydantic** to parse and validate request bodies using Python type annotations.
* It makes runtime data parsing extremely fast and memory efficient.

---

## 🔌 How FastAPI Uses **Starlette** and **Pydantic**

### ✅ **Starlette**:

* Acts as the **core web toolkit** behind FastAPI.
* Handles:

  * Request/response cycle
  * Middleware
  * Routing
  * WebSockets
  * Background tasks

### ✅ **Pydantic**:

* Used to **validate and parse** incoming JSON/data using Python classes.
* Automatically rejects wrong input.
* Used for both:

  * Request body models
  * Response models


