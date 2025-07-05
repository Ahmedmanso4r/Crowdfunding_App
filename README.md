# Crowd-Funding Console App

A Python-based console application for managing crowd-funding campaigns, with user authentication and project management features, backed by PostgreSQL for data persistence.

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

### Database
- **PostgreSQL Backend**:
  - Proper relational database structure
  - Tables for users and projects with relationships
  - Data integrity through foreign keys
- **Secure Data Handling**:
  - Parameterized queries to prevent SQL injection
  - Transaction management for data consistency

## Technical Implementation

- **Python 3** for application logic
- **PostgreSQL** for data persistence
- **psycopg2** library for database connectivity
- **Command-line interface** with intuitive menus
- **Input validation** for all user inputs
- **Modular design** for easy maintenance

## Setup Instructions

### Prerequisites
- Python 3.x installed
- PostgreSQL server installed and running
- psycopg2 package (`pip install psycopg2-binary`)

### Configuration
1. Create a PostgreSQL database named `crowdfunding`
2. Update the `DB_CONFIG` dictionary in the code with your database credentials
3. The application will automatically initialize the required tables on first run

### Running the Application
python crowdfunding.py