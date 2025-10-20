import matplotlib.pyplot as plt
import cv2

def grayscale(image_path: str):

    # 画像読み込み（元画像はBGR）
    original = cv2.imread(image_path)

    # グレースケールに変換
    gray = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)

    # ２つ画像の比較
    plt.figure(figsize=(10, 4))

    # 左：元画像
    plt.subplot(1, 2, 1)
    plt.imshow(original[:, :, ::-1])  # BGR → RGB
    plt.title("Original")
    plt.axis("off")

    # 右：グレースケール
    plt.subplot(1, 2, 2)
    plt.imshow(gray, cmap="gray")
    plt.title("Grayscale")
    plt.axis("off")

    plt.tight_layout()
    plt.show()
