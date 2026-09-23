# Patient Management System

A simple command-line/console application for managing patient records — built entirely in Python.

---

## Overview

Patient Management System is a lightweight tool that lets you **create, update, delete, and search** patient records. No external frameworks, databases, or dependencies — just plain Python.

---

## Features

- **Create** — Add a new patient record (name, age, gender, contact info, medical notes, etc.)
- **Update** — Edit details of an existing patient record
- **Delete** — Remove a patient record
- **Search** — Look up a patient by ID, name, or other identifying field

---

## Tech Stack

| Layer      | Technology |
|------------|------------|
| Language   | Python 3.x |
| Storage    | In-memory / file-based (e.g. JSON) — no external database |

---

## Project Structure

```
patient-management-system/
├── main.py             # Entry point — menu-driven CLI
├── patient.py          # Patient class / data model
├── operations.py       # CRUD logic (create, update, delete, search)
├── data/
│   └── patients.json   # Stored patient records (if using file-based storage)
└── README.md
```

*(Adjust file names to match your actual project layout.)*

---

## Getting Started

### Prerequisites
- Python 3.x installed on your machine

### Installation

```bash
git clone https://github.com/<your-username>/patient-management-system.git
cd patient-management-system
```

No additional dependencies are required — the project uses only Python's standard library.

### Running the App

```bash
python main.py
```

---

## Usage

Once running, you'll be presented with a menu like:

```
==== Patient Management System ====
1. Add Patient
2. Update Patient
3. Delete Patient
4. Search Patient
5. View All Patients
6. Exit
Enter your choice:
```

Follow the prompts to manage patient records.

---

## Example Patient Record

```json
{
  "id": 1,
  "name": "Ali Raza",
  "age": 34,
  "gender": "Male",
  "contact": "0301XXXXXXX",
  "notes": "Regular checkup"
}
```

---

## License

Specify your license here (e.g., MIT).

---

## Author

**Engr. Hasnain Zainulabdin**
R&R Digital Solutions

Contact: 03126641281 | [HasnainZainulabdin@gmail.com](mailto:HasnainZainulabdin@gmail.com)
Website: https://hasnainzainulabdin.vercel.app/
