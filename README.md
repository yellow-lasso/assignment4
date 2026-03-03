# Congressional Trade Disclosure Analysis Tool (CLI Prototype)

## Overview

This project is the command-line prototype for a Congressional Trade Disclosure Analysis Tool. The purpose of the application is to allow users to record and review publicly disclosed congressional stock trades in a structured format. This version of the application is implemented as a simple command-line interface (CLI) and stores data in memory during program execution.

The CLI prototype demonstrates the core interaction flow of the application before later transitioning to structured data storage, persistence, and a web interface.

---

## Features

The current prototype provides three primary actions through a menu-driven interface:

1. **Add a Trade**
   - Prompts the user to enter information about a congressional stock trade.
   - The trade is stored in memory during the program's execution.

2. **List All Trades**
   - Displays all recorded trades stored in the program’s global data list.

3. **Exit**
   - Safely terminates the application.

The menu continuously loops until the user chooses to exit.

---

## Data Storage

For this prototype version:

- All data is stored in a single global variable (`TRADES`).
- Each trade is stored as a formatted string.
- Data exists **only for the duration of the program session**.
- No external files or databases are used in this version.

Future iterations of the project will introduce structured data models and persistent storage.

---

## Running the Application

1. Ensure Python is installed on your system.
2. Open a terminal in the project directory.
3. Run the script:

```bash
python app.py