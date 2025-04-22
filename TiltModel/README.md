
# Image Classification GUI with Keras

This project is a simple GUI application that uses a trained Keras model to classify images. It includes a graphical interface (`GUI.py`) and a pre-trained model (`keras_model.h5`) with corresponding labels.

## 📁 Project Structure

- `GUI.py`: Python script for the graphical user interface.
- `keras_model.h5`: Pre-trained Keras model file.
- `labels.txt`: List of class labels corresponding to the model output.
- `requirements.txt`: Python dependencies.
- `test.ipynb`: Jupyter Notebook for testing or experimentation.

## 📦 Setup Instructions

### 1. Create a Virtual Environment

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

## 🔍 Notes

- Make sure `keras_model.h5` and `labels.txt` are in the same directory as `GUI.py`.
- Use `test.ipynb` to experiment with the model outside of the GUI.
