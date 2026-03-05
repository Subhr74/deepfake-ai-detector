import cv2
import os

HEATMAP_FOLDER="heatmaps"

def generate_heatmap(image_path):

    img=cv2.imread(image_path)

    heatmap=cv2.applyColorMap(img,cv2.COLORMAP_JET)

    overlay=cv2.addWeighted(img,0.6,heatmap,0.4,0)

    filename=os.path.basename(image_path)

    path=os.path.join(HEATMAP_FOLDER,filename)

    cv2.imwrite(path,overlay)

    return path