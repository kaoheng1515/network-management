Network Management
# Network Management

A Django-based tool for managing and monitoring network configurations.

## Installation

Follow these steps to install and run the network management tool on your operating system.

### Prerequisites
- **Python 3.8+**: Ensure Python is installed.
  - **Windows**: Download from [python.org](https://www.python.org) and add to PATH.
  - **macOS**: Install via Homebrew (`brew install python`) or [python.org](https://www.python.org).
  - **Linux**: Install via package manager (e.g., `sudo apt install python3 python3-pip` for Ubuntu).
- **Git**: Install for your OS (see abovelia64bit
  - **Windows**: Download from [git-scm.com](https://git-scm.com).
  - **macOS**: Install via Homebrew (`brew install git`) or Xcode (`xcode-select --install`).
  - **Linux**: Install via package manager (e.g., `sudo apt install git` for Ubuntu).
- **pip**: Included with Python 3.8+.
- **Virtual Environment**: Use `venv` (included with Python) or `virtualenv`.
- Optional: A database like PostgreSQL or SQLite (default).

### Installation Steps

#### Windows
1. **Clone the Repository**:
   - You’ll see (venv) in your prompt..
   - Run:
     ```bash
     git clone https://github.com/kaoheng1515/network-management.git
     cd network-management
2. **Set Up a Virtual Environment:**:
   - Open Git Bash or Command Prompt.
   - Run:
     ```bash
     python -m venv venv
     venv\Scripts\activate
3. **Install Dependencies:**:
   - Ensure requirements.txt exists (see below to generate it).
   - Run:
     ```bash
     pip install -r requirements.txt
4. **Configure Environment Variables:**:
   - Create a .env file in the project root:
   - Run:
     ```bash
     SECRET_KEY=your-secret-key-here
     DEBUG=True
     DATABASE_URL=sqlite:///db.sqlite3
  - Generate a SECRET_KEY using a tool like djecrety.
  - Install python-decouple:
    ```bash
     pip install python-decouple
5. **Run Migrations::**:
   - Run:
     ```bash
     python manage.py migrate
5. **Start the Development Server:**:
   - Run:
     ```bash
     python manage.py runserver
  - Access at http://localhost:8000.
#### macOS
1. **Clone the Repository**:
   - Open Terminal.
   - Run:
     ```bash
     git clone https://github.com/kaoheng1515/network-management.git
     cd network-management
2. **Set Up a Virtual Environment:**:
   - Run:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
3. **Install Dependencies:**:
   - Run:
     ```bash
     pip install -r requirements.txt
4. **Install Dependencies:**:
   - Create a .env file:
   - Run:
     ```bash
     SECRET_KEY=your-secret-key-here
     DEBUG=True
     DATABASE_URL=sqlite:///db.sqlite3
  - Install python-decouple:
     ```bash
     pip install python-decouple
5. **Run Migrations:**:
   - Run:
     ```bash
     python3 manage.py migrate
6. **Start the Development Server:**:
   - Run:
     ```bash
     python3 manage.py runserver
  - Access at http://localhost:8000.
# Screenshot 
/Users/mac-404/Desktop/network-management/images/Home.png
/Users/mac-404/Desktop/network-management/images/Edit.png
