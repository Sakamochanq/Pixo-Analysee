import analysis.plot_histogram as ph
import assets.filter.grayscale as gs

image_path = "./assets/images/Deer.jpg"

if __name__ == "__main__":
    # ph.plot_histogram(image_path)
    gs.grayscale(image_path)