from PIL import Image
from PIL.ImageOps import invert
from generate import georgian

if __name__ == '__main__':
    for i, _ in enumerate(georgian):
        img = Image.open(f"alphabet/direct/letter_{str(i + 1).zfill(2)}.png").convert('L')
        img = invert(img)
        img.save(f"alphabet/inverse/letter_{str(i + 1).zfill(2)}.png")
