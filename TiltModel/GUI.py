import cv2
import numpy as np
from PIL import Image, ImageTk, ImageOps
import tkinter as tk
from tkinter import Label, Button
from keras.models import load_model

# Load model and labels
model = load_model("keras_model.h5", compile=False)
class_names = open("labels.txt", "r").readlines()

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Nhận dạng bằng mô hình Keras")
root.geometry("600x500")

# Biến toàn cục
captured_image = None
photo_label = None
result_label = None


# Hàm mở webcam và chụp ảnh
def open_camera():
    global captured_image, photo_label, result_label

    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Không mở được camera")
        return

    cv2.namedWindow("Press SPACE to capture, ESC to exit")

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frame = cv2.flip(frame, 1)
        cv2.imshow("Press SPACE to capture, ESC to exit", frame)

        key = cv2.waitKey(1)

        if key % 256 == 27:  # ESC để thoát
            break
        elif key % 256 == 32:  # SPACE để chụp
            captured_image = frame.copy()
            break

    cap.release()
    cv2.destroyAllWindows()

    if captured_image is not None:
        # Hiển thị ảnh đã chụp
        image = cv2.cvtColor(captured_image, cv2.COLOR_BGR2RGB)
        img_pil = Image.fromarray(image)
        img_pil_resized = img_pil.resize((300, 300))
        tk_image = ImageTk.PhotoImage(img_pil_resized)

        if photo_label is None:
            photo_label = Label(root, image=tk_image)
            photo_label.image = tk_image
            photo_label.pack()
        else:
            photo_label.configure(image=tk_image)
            photo_label.image = tk_image

        # Dự đoán
        predict_image(img_pil)


# Hàm dự đoán
def predict_image(img_pil):
    global result_label

    size = (224, 224)
    image = ImageOps.fit(img_pil, size, Image.Resampling.LANCZOS)
    image_array = np.asarray(image)
    normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    data[0] = normalized_image_array

    prediction = model.predict(data)
    index = np.argmax(prediction)
    class_name = class_names[index].strip()
    confidence_score = prediction[0][index]

    # Hiển thị kết quả
    result_text = f"Dự đoán: {class_name}\nĐộ tin cậy: {confidence_score:.2f}"
    if result_label is None:
        result_label = Label(root, text=result_text, font=("Arial", 14))
        result_label.pack(pady=10)
    else:
        result_label.configure(text=result_text)


# Nút chụp ảnh
capture_btn = Button(root, text="📷 Chụp ảnh", font=("Arial", 16), command=open_camera)
capture_btn.pack(pady=20)

# Chạy ứng dụng
root.mainloop()
