# Crowd-Funding Console App

A Python-based console application for managing crowd-funding campaigns with user authentication and project management features, using JSON files for data persistence.

## Project Idea

Crowdfunding is the practice of funding a project or venture by raising small amounts of money from a large number of people. This console application provides a platform where users can create, manage, and explore fundraising campaigns, similar to popular platforms like GoFundMe or Kickstarter, but in a command-line interface.

## Features

### Authentication System
- **User Registration**:
  - First name and last name
  - Email validation and uniqueness check
  - Password confirmation with minimum length requirement
  - Egyptian mobile phone number validation
- **User Login**:
  - Secure authentication using email and password
  - Session management for logged-in users

### Project Management
- **Create Projects**:
  - Title and details
  - Total funding target (in EGP)
  - Start and end dates with validation
- **View Projects**:
  - Browse all available projects
  - View only your own created projects
- **Edit Projects**:
  - Modify any field of your projects
  - Preserve existing values if no changes are made
- **Delete Projects**:
  - Remove your own projects
  - Confirmation before deletion
- **Search Projects**:
  - Find projects active on a specific date

### Data Storage
- **JSON File Storage**:
  - `users.json` for storing user data
  - `projects.json` for storing project data
  - Automatic creation of files on first run
  - Simple and portable data format

## Technical Implementation

- **Python 3** for application logic
- **JSON files** for data persistence
- **Standard library modules** (json, datetime, re, getpass)
- **Command-line interface** with intuitive menus
- **Input validation** for all user inputs
- **Modular design** for easy maintenance

## Setup Instructions

### Prerequisites
- Python 3.x installed

### Running the Application
1. Save the code to a file (e.g., `crowdfunding.py`)
2. Run the application:
python crowdfunding.py