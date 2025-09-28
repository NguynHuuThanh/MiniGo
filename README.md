# MiniGo Compiler Project

This repository contains the source code for a compiler implementation for **MiniGo**, a simplified subset of the Go programming language (Golang). The compiler is built using **ANTLR 4** for Lexing and Parsing, and the subsequent phases (AST generation, Semantic Checking, and Code Generation) are implemented in **Python**. The target environment for the generated code is the **Java Virtual Machine (JVM)**.

---

## 1. MiniGo Language Overview

MiniGo is designed to focus on the core concepts of compiler construction without the complexity of Go's full feature set (like goroutines, channels, or the extensive standard library).

| Feature | Description |
|---------|-------------|
| **Data Types** | Primitive types include `int`, `float`, `boolean`, and `string`. |
| **Composite Types** | Supports `struct` (grouping fields of different types) and `interface` (defining a set of method prototypes). |
| **Variables & Constants** | Declared using `var` and `const`. Supports type inference. Variables of string, struct, array, and interface types are passed by reference; others are passed by value. |
| **Arrays** | Fixed-size, multi-dimensional arrays (e.g., `var arr [5]int`). Indexed from 0. |
| **Functions & Methods** | Supports standard `func` declarations and methods associated with struct types using a receiver argument. |
| **Control Flow** | Includes `if/else if/else` statements and `for` loops (basic conditional, traditional initialization/condition/update, and range iteration over arrays). Also includes `break` and `continue`. |
| **Entry Point** | Every MiniGo program must contain a mandatory `main` function with no parameters and no return values (`func main()`). |
| **Built-in Functions** | Provides I/O functions: `getInt()`, `putIntLn(i int)`, `getString()`, `putStringLn(s string)`, `putLn()`. |

---

## 2. Environment Setup (ANTLR & Python)

The compiler project relies on **Python** (for implementation) and **Java** (for running ANTLR).

### Prerequisites

- **JAVA JDK:** Ensure the Java Development Kit is installed and accessible via your system's path.  
- **Python 3:** Install Python 3.12.x or compatible version.

### ANTLR Setup

1. **Download ANTLR JAR**
   - Download ANTLR runtime library file: `antlr-4.9.2-complete.jar`

2. **Set Environment Variable**
   - Linux/macOS:
     ```bash
     export ANTLR_JAR="/path/to/antlr-4.9.2-complete.jar"
     ```
   - Windows (Command Prompt):
     ```cmd
     set ANTLR_JAR="C:\path\to\antlr-4.9.2-complete.jar"
     ```

3. **Install Python Runtime**
   ```bash
   pip install antlr4-python3-runtime==4.9.2

### How to build
1. **Build the compiler**
   ```cd src
      python3 run.py gen
   ```

2. **Testing with 100 testcases for each module**
   ```cd src
      python3 run.py test LexerSuite
      python3 run.py test ParserSuite
      python3 run.py test ASTGenSuite
      python3 run.py test CheckerSuite
      python3 run.py test CodeGenSuite
   ```
