from PIL import Image, ImageFilter, ImageDraw, ImageFont
import os

def load_image(path):
    return Image.open(path)

def resize_image(img, width, height):
    return img.resize((width, height))

def rotate_image(img, angle):
    return img.rotate(angle)

def convert_to_grayscale(img):
    return img.convert("L")

def blur_image(img, radius=2):
    return img.filter(ImageFilter.GaussianBlur(radius))

def add_text(img, text, position=(10, 10), font_size=20):
    draw = ImageDraw.Draw(img)
    font = ImageFont.load_default()
    draw.text(position, text, fill=255 if img.mode == "L" else (255, 255, 255), font=font)
    return img

def save_image(img, output_path):
    img.save(output_path)
    print(f"Image saved to {output_path}")

def main():
    print("=== Photo Manipulation Tool ===")
    path = input("Enter image file path: ")
    
    if not os.path.exists(path):
        print("File does not exist.")
        return

    img = load_image(path)

    while True:
        print("\nChoose an operation:")
        print("1. Resize")
        print("2. Rotate")
        print("3. Grayscale")
        print("4. Blur")
        print("5. Add Text")
        print("6. Save and Exit")
        
        choice = input("Option: ")

        if choice == "1":
            width = int(input("Width: "))
            height = int(input("Height: "))
            img = resize_image(img, width, height)
        elif choice == "2":
            angle = int(input("Angle (degrees): "))
            img = rotate_image(img, angle)
        elif choice == "3":
            img = convert_to_grayscale(img)
        elif choice == "4":
            radius = float(input("Blur radius: "))
            img = blur_image(img, radius)
        elif choice == "5":
            text = input("Enter text: ")
            x = int(input("X position: "))
            y = int(input("Y position: "))
            img = add_text(img, text, (x, y))
        elif choice == "6":
            output_path = input("Save as (e.g., output.jpg): ")
            save_image(img, output_path)
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
