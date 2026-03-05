import cv2
import os

HEATMAP_FOLDER = "heatmaps"

def generate_heatmap(image_path):

    img = cv2.imread(image_path)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    heatmap = cv2.applyColorMap(gray, cv2.COLORMAP_JET)

    overlay = cv2.addWeighted(img,0.6,heatmap,0.4,0)

    filename = os.path.basename(image_path)

    output_path = os.path.join(HEATMAP_FOLDER, filename)

    cv2.imwrite(output_path, overlay)

    return output_path