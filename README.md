# Clinic Appointment Scheduling System


This is a command-line based Clinic Appointment Scheduling System built using Python. It allows administrators to register patients and doctors to manage appointments. The system was refactored using clean code practices and SOLID principles to improve structure, readability, and reliability.

## Initial Challenges (Before Refactoring)

At the beginning, the system worked, but it had several practical issues that made it difficult to use and maintain:

* **Everything was in one place**
  One class `ClinicSystem` was responsible for handling patients, appointments, user input, and display logic. This made the code confusing and hard to follow.

* **There were frequent crashes due to user input**
  If a user entered something unexpected (e.g., typing `"Dog"` instead of a number for age), the system would crash. There was no protection against invalid input.

* **No control over data quality**
  Fields like gender and contact number could accept anything. This meant inconsistent and unreliable data (e.g., `"Dog"` as gender or invalid phone numbers).

* **The code was tightly coupled **
  The system directly handled data storage (lists in memory) alongside business logic. This made it hard to switch to another storage system like a database.

* **Difficult to extend**
  Adding new features (like validation, roles, or better storage) required modifying large parts of the code, increasing the risk of breaking existing functionality.

* **Poor readability**
  Long methods and mixed responsibilities made it harder for someone else (or even the same developer later) to understand the code quickly.

---

## ✅ Improvements After Refactoring

The system was redesigned to be cleaner, more structured, and more reliable:

### 🔹 1. Modular Architecture

The project was split into clear modules:

* `models/` → Handles data structures (Patient, Appointment, User)
* `services/` → Contains business logic
* `storage/` → Handles JSON data persistence
* `main.py` → Handles user interaction

This makes the system easier to navigate, debug, and extend.


### 🔹 2. Application of SOLID Principles

* **Single Responsibility Principle (SRP)**
  Each class now has a single, clear purpose. For example, `PatientService` only manages patients, and `AuthService` only handles login.

* **Open/Closed Principle (OCP)**
  The system can be extended (e.g., adding new features like notifications or different storage types) without modifying existing code.

* **Liskov Substitution Principle (LSP)**
  Liskov Substitution Principle was implemented through the use of a storage abstraction. The system depends on a common interface for data storage, allowing different storage implementations (such as JSON or in-memory storage) to be used interchangeably without affecting system behavior.
  
* **Interface Segregation Principle (ISP)**
  Classes only implement what they need, avoiding unnecessary methods.

* **Dependency Inversion Principle (DIP)**
  The system depends on abstractions (`StorageInterface`) rather than concrete implementations. This makes it easy to switch from JSON storage to a database later.


### 🔹 3. Input Validation & Error Handling

The system now actively prevents invalid data:

* Age must be a valid positive number
* Gender only accepts *male* or *female* (case-insensitive)
* Contact numbers follow valid formats
* Try-except blocks prevent crashes from bad input

This makes the system more user-friendly and robust.


### 🔹 4. Persistent Data Storage (JSON)

Instead of storing data temporarily in memory, the system now uses JSON files:

* `users.json`
* `patients.json`
* `appointments.json`

This ensures data is saved and available even after the program is restarted.

---

## Key Benefits

* ✔ Cleaner and more readable code
* ✔ Reduced chances of system crashes
* ✔ Easier to maintain and extend
* ✔ Better user experience through validation
* ✔ Follows industry-relevant software development practices


