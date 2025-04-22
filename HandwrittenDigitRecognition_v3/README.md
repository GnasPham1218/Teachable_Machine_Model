
# Handwritten Digit Recognition GUI

This project provides a simple handwritten digit recognition application using a trained Keras model. Users can test digit classification through a graphical interface or directly via notebook.

## 📁 Project Files

- `GUI.py`: GUI for digit recognition.
- `keras_model.h5`: Trained Keras model for recognizing digits.
- `labels.txt`: Contains labels/classes predicted by the model.
- `requirements.txt`: Required dependencies.
- `test.ipynb`: Notebook for testing the model.
- `1.png`: Sample image input for testing.

## ⚙️ Setup Instructions

### Step 1: Create a Virtual Environment

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Run the Application

Launch the GUI with:
```bash
python GUI.py
```

Or use `test.ipynb` in Jupyter Notebook to run the model and classify images programmatically.

## 🧽 Optional Cleanup

Uninstall all installed packages:
```bash
pip freeze > requirements.txt
pip uninstall -y -r requirements.txt
```

Or delete and recreate the virtual environment.

---

Make sure all files are in the same directory when running the application.
