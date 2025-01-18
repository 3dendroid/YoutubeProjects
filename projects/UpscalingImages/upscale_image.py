import os
import tkinter as tk
from tkinter import filedialog, messagebox

import cv2


def upscale_image(image_path, scale):
    # Загружаем изображение
    image = cv2.imread(image_path, cv2.IMREAD_COLOR)
    if image is None:
        raise FileNotFoundError(f"Изображение {image_path} не найдено. Убедитесь, что путь указан правильно.")

    # Получение новых размеров изображения
    height, width = image.shape[:2]
    new_width, new_height = int(width * scale), int(height * scale)

    # Масштабируем изображение с помощью bicubic interpolation
    upscaled_image = cv2.resize(image, (new_width, new_height), interpolation=cv2.INTER_CUBIC)

    return upscaled_image


class SimpleUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Upscaler")
        self.root.geometry("400x200")

        self.image_path = None

        # UI элементы
        self.label = tk.Label(root, text="Выберите изображение для масштабирования:")
        self.label.pack(pady=10)

        self.select_button = tk.Button(root, text="Выбрать файл", command=self.select_file)
        self.select_button.pack(pady=5)

        self.scale_label = tk.Label(root, text="Введите коэффициент масштабирования:")
        self.scale_label.pack(pady=5)

        self.scale_entry = tk.Entry(root)
        self.scale_entry.pack(pady=5)
        self.scale_entry.insert(0, "4.0")  # Значение по умолчанию

        self.start_button = tk.Button(root, text="Масштабировать", command=self.start_upscale)
        self.start_button.pack(pady=20)

    def select_file(self):
        self.image_path = filedialog.askopenfilename(
            filetypes=(("Image files", "*.jpg;*.jpeg;*.png"), ("All files", "*.*"))
        )
        if self.image_path:
            messagebox.showinfo("Файл выбран", f"Выбран файл: {self.image_path}")
            print(f"Выбран файл: {self.image_path}")
        else:
            print("Файл не выбран.")

    def start_upscale(self):
        if not self.image_path:
            messagebox.showerror("Ошибка", "Сначала выберите изображение!")
            return

        scale_text = self.scale_entry.get()
        try:
            scale = float(scale_text)
            if scale <= 0:
                raise ValueError("Коэффициент масштабирования должен быть положительным!")
        except ValueError:
            messagebox.showerror("Ошибка", "Введите корректный коэффициент масштабирования!")
            return

        try:
            # Масштабируем изображение
            result_image = upscale_image(self.image_path, scale)

            # Подготавливаем корректное место для сохранения
            default_dir = os.path.dirname(os.path.abspath(__file__))  # Директория текущего файла
            filename = os.path.basename(self.image_path).rsplit(".", 1)[0] + "_upscaled.jpg"
            output_path = os.path.join(default_dir, filename)

            # Сохраняем результат
            cv2.imwrite(output_path, result_image)

            messagebox.showinfo("Успех", f"Масштабированное изображение сохранено:\n{output_path}")
            print(f"Изображение сохранено по пути: {output_path}")
        except Exception as e:
            messagebox.showerror("Ошибка", f"Произошла ошибка: {e}")
            print(f"Ошибка: {e}")


if __name__ == "__main__":
    root = tk.Tk()
    app = SimpleUI(root)
    root.mainloop()
