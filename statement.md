# Project Statement

## 1. Problem Statement
Managing student records on paper or messy Excel sheets is a headache. It is slow, disorganized, and risky files get lost, coffee gets spilled on them, and finding a specific student's details can take forever. Plus, without a proper login system, anyone can accidentally change or delete important data.

This project solves that by moving everything to a secure, digital system where data is safe, organized, and easy to find.

## 2. Scope of the Project
The **Student Management System (SMS)** is a straightforward Python application built to handle the day-to-day management of student data.
* **What it does:** It acts as a digital ledger. You can add new students, update their info, or remove them when they leave.
* **How it works:** It is a lightweight console app that runs on your computer. It uses JSON files to save data, so you don't need to install complex database servers or have an internet connection to use it.
* **Future-proof:** Right now, it handles basic details, but the code is written in a way that makes it easy to add features like attendance tracking or report cards later.

## 3. Target Users
* **School Admins:** The main users who need to input and manage student data without sorting through piles of paper.
* **Teachers/Faculty:** Those who need to quickly look up a student's Roll Number or contact details.
* **Small Institutes:** Coaching centers or small schools that need a free, simple tool to manage their students.

## 4. High-Level Features
* **Secure Login:** A login system (Admin vs. User) to make sure only authorized people can add or delete records.
* **Full Control (CRUD):** You have full power to **C**reate new records, **R**ead/View them, **U**pdate details, and **D**elete old ones.
* **Auto-Save:** The system uses Python's `json` module to save every change instantly. If you close the app, your data is still there when you come back.
* **Smart Search:** No need to scroll through hundreds of names, just type a Roll Number to find a student instantly.
* **Error Prevention:** The system stops you from making common mistakes, like entering the same Roll Number twice.
