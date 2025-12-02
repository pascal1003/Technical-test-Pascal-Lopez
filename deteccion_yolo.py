from ultralytics import YOLO
import cv2
import os

model = YOLO("yolo11m_finetuned.pt")

# Carpetas
input_folder = "front_camera"
output_folder = "resultados"
os.makedirs(output_folder, exist_ok=True)

# Path
image_names = ["1.jpg", "2.jpg", "3.jpg", "4.jpg"]

#Procesamiento
for img_name in image_names:

    image_path = os.path.join(input_folder, img_name)

    results = model.predict(
        source=image_path,
        conf=0.4,
        task="segment"
    )

    
    annotated = results[0].plot()
    
    # guardar resultados
    output_path = os.path.join(output_folder, img_name)
    cv2.imwrite(output_path, annotated)
