from ultralytics import YOLO
import cv2
import os
import numpy as np
from sklearn.cluster import DBSCAN
import time 

model = YOLO("yolo11m_finetuned.pt")

# Carpetas

input_folder = "front_camera"
output_folder = "resultados_plantas"
os.makedirs(output_folder, exist_ok=True)

# Path
image_names = ["1.jpg", "2.jpg", "3.jpg", "4.jpg"]

# centroides
def get_centroid(box):
    x1, y1, x2, y2 = box
    return [(x1 + x2) / 2, (y1 + y2) / 2]

#Procesamiento
for img_name in image_names:
    time_init = time.time()
    image_path = os.path.join(input_folder, img_name)
    img = cv2.imread(image_path)

    #Yolo
    results = model.predict(
        source=image_path,
        conf=0.4,
        task="segment"
    )

    r = results[0]

    # Centroides de ojas
    boxes = r.boxes.xyxy.cpu().numpy()
    centroids = np.array([get_centroid(b) for b in boxes])

    # Clustering
    clustering = DBSCAN(eps=120, min_samples=1).fit(centroids)
    labels = clustering.labels_
    num_plants = len(set(labels))

    # Bordes
    for cluster_id in range(num_plants):
        points = boxes[labels == cluster_id]

        x1 = int(np.min(points[:, 0]))
        y1 = int(np.min(points[:, 1]))
        x2 = int(np.max(points[:, 2]))
        y2 = int(np.max(points[:, 3]))
        plant_centroid = get_centroid ((x1,y1,x2,y2))
        cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 255), 3)
        cv2.circle(img, (int(plant_centroid[0]), int(plant_centroid[1])),5, (0, 255, 255), 10)

        cv2.putText(img, f"Planta {cluster_id+1}",
                    (x1, y1-10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.8, (0, 255, 255), 2)
        time_fin = time.time() - time_init
        cv2.putText(img, f"Tiempo = {time_fin} ",
                    (40, 40),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1, (0, 255, 255), 2)

    # Guardar
    output_path = os.path.join(output_folder, img_name)
    cv2.imwrite(output_path, img)