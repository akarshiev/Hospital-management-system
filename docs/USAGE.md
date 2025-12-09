# Detailed Usage Guide (English)

## Overview

The Hospital Management System is a desktop application for managing patient records, finding suitable doctors, and viewing medical statistics. The application uses a tabbed interface with three main sections.

---

## Main Window

The application window is divided into three tabs:

1. **Patient Registration** — Manage patient records
2. **Doctors** — View doctor directory
3. **Statistics** — View analytics and charts

---

## Patient Registration Tab

### Adding a Patient

1. Fill in the following fields:
   - **Patient Name** (required)
   - **Age** (required, 1-120)
   - **Illness** (required)
   - **Phone Number** (optional)
2. Click **"Add Patient"** button
3. A confirmation message will appear

### Patient List

The right panel shows all registered patients with:
- Name, age, and illness information
- Phone number and registration date
- Action buttons:
  - **Edit** — Modify patient details
  - **Delete** — Remove patient (requires confirmation)
  - **Find Doctor** — Shows recommended doctor

### Searching Patients

- Type in the search box to filter patients by name or illness
- The list updates in real-time as you type

---

## Doctors Tab

View all available doctors with:
- Name and specialty
- Room number
- Phone number
- Working hours
- Keywords for automated matching

---

## Statistics Tab

Shows visual statistics including:
- **Total patient count**
- **Age group distribution** (0-18, 19-35, 36-55, 56+)
- **Doctor workload** (patients per specialty)

Click **"Refresh Statistics"** to update the data.

---

## Data Persistence

- Patient data is automatically saved to `patients.json`
- Data persists between application restarts
- The JSON file is created automatically on first patient addition

---

## Important Notes

- The application requires `customtkinter` library (install via `pip install customtkinter`)
- Patient data is stored locally and is not shared across devices
- Always check the doctor recommendation before making medical decisions
- The doctor matching is keyword-based and should be used as a reference only
