
## 🔧 Installation

Before running the project, we **strongly recommend creating a virtual environment** to avoid conflicts with other Python packages on your system.

### 1. Create and activate a virtual environment

**On Windows:**


```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 2. Install Required Packages

Install all required dependencies using:
```bash
pip install -r requirements.txt
```

### 3. Run the GUI

Once dependencies are installed and the environment is activated, launch the GUI:
```bash
python GUI.py
```

## 🧹 To Clean Up

To remove all packages inside the virtual environment:
```bash
pip freeze > requirements.txt
pip uninstall -y -r requirements.txt
```

Or simply delete and recreate the environment:
```bash
rm -rf venv               # macOS/Linux
rmdir /s /q venv          # Windows
```
