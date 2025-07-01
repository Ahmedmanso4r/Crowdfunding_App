import re
import json
import datetime
from getpass import getpass

USERS_FILE = "users.json"
PROJECTS_FILE = "projects.json"

users = []
projects = []

def load_data():
    global users, projects
    try:
        with open(USERS_FILE, 'r') as f:
            users = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        users = []
    
    try:
        with open(PROJECTS_FILE, 'r') as f:
            projects = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        projects = []

def save_data():
    with open(USERS_FILE, 'w') as f:
        json.dump(users, f)
    with open(PROJECTS_FILE, 'w') as f:
        json.dump(projects, f)

def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def is_valid_egyptian_phone(phone):
    pattern = r'^01[0125][0-9]{8}$'
    return re.match(pattern, phone) is not None

def is_valid_password(password):
    return len(password) >= 6

def is_valid_date(date_str):
    try:
        datetime.datetime.strptime(date_str, '%Y-%m-%d')
        return True
    except ValueError:
        return False

def register():
    print("\n--- Registration ---")
    first_name = input("First Name: ").strip()
    last_name = input("Last Name: ").strip()
    
    while True:
        email = input("Email: ").strip()
        if not is_valid_email(email):
            print("Invalid email format. Please try again.")
            continue
        
        if any(user['email'] == email for user in users):
            print("Email already registered. Please use a different email.")
            continue
        break
    
    while True:
        password = getpass("Password: ").strip()
        if not is_valid_password(password):
            print("Password must be at least 6 characters long.")
            continue
        
        confirm_password = getpass("Confirm Password: ").strip()
        if password != confirm_password:
            print("Passwords do not match. Please try again.")
            continue
        break
    
    while True:
        mobile_phone = input("Mobile Phone (Egyptian number): ").strip()
        if not is_valid_egyptian_phone(mobile_phone):
            print("Invalid Egyptian phone number. It should start with 010, 011, 012, or 015 and be 11 digits.")
            continue
        break
    
    user = {
        'first_name': first_name,
        'last_name': last_name,
        'email': email,
        'password': password,  
        'mobile_phone': mobile_phone,
        'active': True
    }
    
    users.append(user)
    save_data()
    print("\nRegistration successful! You can now login.")
    return user

def login():
    print("\n--- Login ---")
    email = input("Email: ").strip()
    password = getpass("Password: ").strip()
    
    for user in users:
        if user['email'] == email and user['password'] == password:
            if user.get('active', True):
                print(f"\nWelcome back, {user['first_name']}!")
                return user
            else:
                print("Your account is not active. Please contact support.")
                return None
    
    print("Invalid email or password.")
    return None

def create_project(user):
    print("\n--- Create Project ---")
    title = input("Project Title: ").strip()
    details = input("Project Details: ").strip()
    
    while True:
        try:
            total_target = float(input("Total Target (EGP): ").strip())
            if total_target <= 0:
                print("Target must be a positive number.")
                continue
            break
        except ValueError:
            print("Invalid amount. Please enter a number.")
    
    while True:
        start_date = input("Start Date (YYYY-MM-DD): ").strip()
        if not is_valid_date(start_date):
            print("Invalid date format. Please use YYYY-MM-DD.")
            continue
        break
    
    while True:
        end_date = input("End Date (YYYY-MM-DD): ").strip()
        if not is_valid_date(end_date):
            print("Invalid date format. Please use YYYY-MM-DD.")
            continue
        
        if end_date <= start_date:
            print("End date must be after start date.")
            continue
        break
    
    project = {
        'title': title,
        'details': details,
        'total_target': total_target,
        'start_date': start_date,
        'end_date': end_date,
        'owner_email': user['email'],
        'created_at': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
    
    projects.append(project)
    save_data()
    print("\nProject created successfully!")
    return project

def view_all_projects():
    print("\n--- All Projects ---")
    if not projects:
        print("No projects found.")
        return
    
    for idx, project in enumerate(projects, 1):
        print(f"\nProject {idx}:")
        print(f"Title: {project['title']}")
        print(f"Details: {project['details']}")
        print(f"Target: {project['total_target']} EGP")
        print(f"Start Date: {project['start_date']}")
        print(f"End Date: {project['end_date']}")
        print(f"Created By: {project['owner_email']}")

def view_user_projects(user):
    print("\n--- Your Projects ---")
    user_projects = [p for p in projects if p['owner_email'] == user['email']]
    
    if not user_projects:
        print("You haven't created any projects yet.")
        return []
    
    for idx, project in enumerate(user_projects, 1):
        print(f"\nProject {idx}:")
        print(f"Title: {project['title']}")
        print(f"Details: {project['details']}")
        print(f"Target: {project['total_target']} EGP")
        print(f"Start Date: {project['start_date']}")
        print(f"End Date: {project['end_date']}")
    
    return user_projects

def edit_project(user):
    user_projects = view_user_projects(user)
    if not user_projects:
        return
    
    while True:
        try:
            project_num = int(input("\nEnter project number to edit (0 to cancel): ").strip())
            if project_num == 0:
                return
            if 1 <= project_num <= len(user_projects):
                break
            print("Invalid project number. Please try again.")
        except ValueError:
            print("Please enter a valid number.")
    
    project_to_edit = user_projects[project_num - 1]
    
    print("\nLeave field blank to keep current value.")
    
    title = input(f"New Title [{project_to_edit['title']}]: ").strip()
    details = input(f"New Details [{project_to_edit['details']}]: ").strip()
    
    while True:
        total_target = input(f"New Target [{project_to_edit['total_target']}]: ").strip()
        if not total_target:
            break
        try:
            total_target = float(total_target)
            if total_target <= 0:
                print("Target must be a positive number.")
                continue
            break
        except ValueError:
            print("Invalid amount. Please enter a number.")
    
    while True:
        start_date = input(f"New Start Date [{project_to_edit['start_date']}]: ").strip()
        if not start_date:
            break
        if not is_valid_date(start_date):
            print("Invalid date format. Please use YYYY-MM-DD.")
            continue
        break
    
    while True:
        end_date = input(f"New End Date [{project_to_edit['end_date']}]: ").strip()
        if not end_date:
            break
        if not is_valid_date(end_date):
            print("Invalid date format. Please use YYYY-MM-DD.")
            continue
        
        current_start = start_date if start_date else project_to_edit['start_date']
        if end_date <= current_start:
            print("End date must be after start date.")
            continue
        break
    
    # Edit project
    if title:
        project_to_edit['title'] = title
    if details:
        project_to_edit['details'] = details
    if total_target:
        project_to_edit['total_target'] = total_target
    if start_date:
        project_to_edit['start_date'] = start_date
    if end_date:
        project_to_edit['end_date'] = end_date
    
    save_data()
    print("\nProject updated successfully!")

def delete_project(user):
    user_projects = view_user_projects(user)
    if not user_projects:
        return
    
    while True:
        try:
            project_num = int(input("\nEnter project number to delete (0 to cancel): ").strip())
            if project_num == 0:
                return
            if 1 <= project_num <= len(user_projects):
                break
            print("Invalid project number. Please try again.")
        except ValueError:
            print("Please enter a valid number.")
    
    project_to_delete = user_projects[project_num - 1]
    projects.remove(project_to_delete)
    save_data()
    print("\nProject deleted successfully!")

def search_by_date():
    print("\n--- Search Projects by Date ---")
    while True:
        date_str = input("Enter date to search (YYYY-MM-DD): ").strip()
        if not is_valid_date(date_str):
            print("Invalid date format. Please use YYYY-MM-DD.")
            continue
        break
    
    found_projects = []
    for project in projects:
        if project['start_date'] <= date_str <= project['end_date']:
            found_projects.append(project)
    
    if not found_projects:
        print(f"No projects found running on {date_str}.")
        return
    
    print(f"\nProjects running on {date_str}:")
    for idx, project in enumerate(found_projects, 1):
        print(f"\nProject {idx}:")
        print(f"Title: {project['title']}")
        print(f"Details: {project['details']}")
        print(f"Target: {project['total_target']} EGP")
        print(f"Start Date: {project['start_date']}")
        print(f"End Date: {project['end_date']}")
        print(f"Created By: {project['owner_email']}")

# Main application
def main():
    load_data()
    current_user = None
    
    while True:
        if not current_user:
            print("\n=== Crowd-Funding Console App ===")
            print("1. Register")
            print("2. Login")
            print("3. Exit")
            
            choice = input("Enter your choice: ").strip()
            
            if choice == '1':
                register()
            elif choice == '2':
                current_user = login()
            elif choice == '3':
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
        else:
            print("\n=== Main Menu ===")
            print("1. Create Project")
            print("2. View All Projects")
            print("3. View Your Projects")
            print("4. Edit Project")
            print("5. Delete Project")
            print("6. Search Projects by Date")
            print("7. Logout")
            
            choice = input("Enter your choice: ").strip()
            
            if choice == '1':
                create_project(current_user)
            elif choice == '2':
                view_all_projects()
            elif choice == '3':
                view_user_projects(current_user)
            elif choice == '4':
                edit_project(current_user)
            elif choice == '5':
                delete_project(current_user)
            elif choice == '6':
                search_by_date()
            elif choice == '7':
                current_user = None
                print("Logged out successfully.")
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()