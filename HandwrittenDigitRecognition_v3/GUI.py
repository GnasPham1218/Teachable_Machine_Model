import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import cv2
import numpy as np
from keras.models import load_model

# Load model and labels
try:
    model = load_model("keras_model.h5", compile=False)
    class_names = [line.strip() for line in open("labels.txt", "r").readlines()]
except Exception as e:
    messagebox.showerror("Lỗi tải model", f"Không thể tải mô hình hoặc nhãn: {e}")
    exit()


# Hàm tiền xử lý ảnh
def preprocess_image(image):
    img = cv2.resize(image, (224, 224))  # resize theo model
    img = np.asarray(img, dtype=np.float32).reshape(1, 224, 224, 3)
    img = (img / 127.5) - 1  # normalize về [-1, 1]
    return img


# Hàm dự đoán và hiển thị kết quả
def predict_and_show(image):
    processed = preprocess_image(image)
    prediction = model.predict(processed)[0]
    index = np.argmax(prediction)
    result = class_names[index]
    confidence = prediction[index]

    result_label.config(text=f"Kết quả: {result} ({confidence*100:.2f}%)")


# Hàm chọn ảnh
def select_image():
    file_path = filedialog.askopenfilename(
        filetypes=[("Image files", "*.jpg *.png *.jpeg")]
    )
    if file_path:
        image = cv2.imread(file_path)
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        img_pil = Image.fromarray(image_rgb)
        img_tk = ImageTk.PhotoImage(img_pil)
        panel.config(image=img_tk)
        panel.image = img_tk
        predict_and_show(image)


# Giao diện GUI
root = tk.Tk()
root.title("Nhận diện ảnh bằng mô hình Keras")
root.geometry("600x500")

btn_select = tk.Button(root, text="Chọn ảnh từ file", command=select_image)
btn_select.pack(pady=10)


panel = tk.Label(root)
panel.pack(pady=10)

result_label = tk.Label(root, text="Kết quả: ", font=("Arial", 14))
result_label.pack(pady=10)

root.mainloop()
