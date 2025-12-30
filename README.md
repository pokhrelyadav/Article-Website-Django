# Article Website – EADD Assignment 1 & 2

This project is a **simple Article Website** built using **Django** with a **multilayer and multitier architecture**.  
It includes a Django backend (along with API) and a separate frontend that consumes the API.

---

## Prerequisites

Make sure the following tools are installed on your system:

- Python 3.10 or higher
- Git
- VS Code (recommended)
- Live Server extension (for frontend)
- `uv` (Python package manager).
- Run below command to get uv. It is best alternative of **pip venv**.

```bash
pip install uv
```

---
---

## Project Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/pokhrelyadav/Article-Website-Django.git
```

---

### 2. Navigate to the Project Directory

```bash
cd Article-Website-Django
cd "MultiLayer App"
```

---

### 3. Create a Virtual Environment

```bash
uv venv
```

---

### 4. Install Project Dependencies

```bash
uv pip install -r requirements.txt
```

---

### 5. Activate the Virtual Environment

**Windows (Command Prompt / PowerShell)**

```bash
.venv\Scripts\activate
```

**Windows (Git Bash)**

```bash
source .venv/Scripts/activate
```

**Linux / macOS**

```bash
source .venv/bin/activate
```

---

### 6. Run the Django Application

Make sure you are in the directory where `manage.py` exists.  
You can verify this by running:

```bash
ls
```

or

```bash
dir
```

Open **two terminals** in VS Code and run the following commands:

**Terminal 1 – Start Tailwind CSS**

```bash
python manage.py tailwind start
```

**Terminal 2 – Start Django Development Server**

```bash
python manage.py runserver
```

The main website should now be running.

---

## Frontend (API Usage)

### 7. Configure Frontend API URL

1. Navigate to the **Multitier frontend** folder.
2. Open `index.html`.
3. Update the API URL to match your backend port:

```javascript
const API_URL = "http://localhost:8000/api/v1/articles";
```

> Make sure the port number matches the one shown when running `python manage.py runserver`.

---

### 8. Run the Frontend

- Right-click on `index.html`
- Select **Open with Live Server**

The frontend will now fetch and display data from the Django API.

---

## Notes

- Always activate the virtual environment before running the project.
- Keep Tailwind and Django server running in **separate terminals**.
- If the backend port changes, update it in `index.html`.

---

## Author

**Yadav Pokhrel**

---

Happy Coding 🚀
