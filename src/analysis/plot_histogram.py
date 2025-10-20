import matplotlib.pyplot as plt
import cv2

def plot_histogram(image_path: str):

    # グレースケールで読み込み
    img = cv2.imread(str(image_path), cv2.IMREAD_GRAYSCALE)

    if img is None:
        return
        
    # 画像とヒストグラムの表示
    plt.figure(figsize=(10, 4))
    plt.subplot(1, 2, 1)
    plt.imshow(img, cmap="gray")
    plt.title("Grayscale Image")
    plt.axis("off")

    # ヒストグラムの表示
    plt.subplot(1, 2, 2)
    plt.hist(img.ravel(), bins=256, range=[0, 256], color="black")
    plt.title("Histogram")
    plt.xlabel("Intensity Value")
    plt.ylabel("Pixel Count")

    # Initialize
    plt.tight_layout()
    plt.show()