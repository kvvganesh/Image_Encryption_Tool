from PIL import Image
import os


VALID_EXTENSIONS = ('.jpg', '.jpeg', '.png', '.bmp', '.gif', '.tiff', '.webp')

def validate_output_path(output_path):
    """Validate that output path has a valid image extension"""
    if not any(output_path.lower().endswith(ext) for ext in VALID_EXTENSIONS):
        raise ValueError(f"Output path must have a valid image extension: {', '.join(VALID_EXTENSIONS)}")

def validate_key(key):
    """Validate that key is in valid range (1-255)"""
    if key < 1 or key > 255:
        raise ValueError("Key must be between 1 and 255")

def xor_encrypt(image_path,key,output_path):
    """XOR encryption - applies XOR operation to all pixels"""
    validate_output_path(output_path)
    validate_key(key)
    image=Image.open(image_path).convert("RGB")

    width,height=image.size

    print(f"Image Size: {width}x{height} pixels")
    print(f"Before: {image.getpixel((0,0))}")

    new_image=Image.new("RGB",(width,height))

    total_pixels=width*height
    processed=0

    for y in range(height):
        for x in range(width):
            r,g,b=image.getpixel((x,y))
            r=r^key
            g=g^key
            b=b^key
            new_image.putpixel((x,y),(r,g,b))
            processed+=1
        
        if y%max(1,height//10)==0:
            percent=int((processed/total_pixels)*100)
            print(f"Progress: {percent}%",end="\r")

    print(f"After: {new_image.getpixel((0,0))}")
    new_image.save(output_path, format="PNG")
    print(f"\nSaved to {output_path}")

def xor_decrypt(image_path,key,output_path):
    """XOR decryption - XOR is self-inverse, so decryption uses same operation"""
    xor_encrypt(image_path,key,output_path)

def encrypt_swap_pixels(image_path,output_path):
    """Swap adjacent pixels - encryption"""
    validate_output_path(output_path)
    image=Image.open(image_path).convert("RGB")
    width,height=image.size

    print(f"Image Size: {width}x{height} pixels")
    print(f"Before: {image.getpixel((0,0))}")

    pixels=image.load()
    all_pixels=[]
    for y in range(height):
        for x in range(width):
            all_pixels.append(pixels[x,y])

    for i in range(0,len(all_pixels)-1,2):
        all_pixels[i],all_pixels[i+1]=all_pixels[i+1],all_pixels[i]

    new_image=Image.new("RGB",(width,height))
    new_pixels=new_image.load()
    idx=0
    for y in range(height):
        for x in range(width):
            new_pixels[x,y]=all_pixels[idx]
            idx+=1

    print(f"After: {new_image.getpixel((0,0))}")
    new_image.save(output_path, format="PNG")
    print(f"Saved to {output_path}")

def decrypt_swap_pixels(image_path,output_path):
    """Swap adjacent pixels - decryption (same operation as encryption)"""
    encrypt_swap_pixels(image_path,output_path)
    
def encrypt_add_key(image_path,key,output_path):
    """Add key to pixel values - encryption"""
    validate_output_path(output_path)
    validate_key(key)
    image=Image.open(image_path).convert("RGB")
    width,height=image.size

    print(f"Image Size: {width}x{height} pixels")
    print(f"Before: {image.getpixel((0,0))}")

    new_image=Image.new("RGB",(width,height))

    for x in range(width):
        for y in range(height):
            r,g,b=image.getpixel((x,y))
            r=(r+key)%256
            g=(g+key)%256
            b=(b+key)%256
            new_image.putpixel((x,y),(r,g,b))

    print(f"After: {new_image.getpixel((0,0))}")
    new_image.save(output_path, format="PNG")
    print(f"Saved to {output_path}")

def decrypt_subtract_key(image_path,key,output_path):
    """Subtract key from pixel values - decryption"""
    validate_output_path(output_path)
    validate_key(key)
    image=Image.open(image_path).convert("RGB")
    width,height=image.size

    print(f"Image Size: {width}x{height} pixels")
    print(f"Before: {image.getpixel((0,0))}")

    new_image=Image.new("RGB",(width,height))

    for x in range(width):
        for y in range(height):
            r,g,b=image.getpixel((x,y))
            r=(r-key)%256
            g=(g-key)%256
            b=(b-key)%256
            new_image.putpixel((x,y),(r,g,b))

    print(f"After: {new_image.getpixel((0,0))}")
    new_image.save(output_path, format="PNG")
    print(f"Saved to {output_path}")

def display_menu():
    print("\n=== ENCRYPTION OPTIONS ===")
    print("1. XOR Encrypt")
    print("2. Swap Pixels Encrypt")
    print("3. Add Key Encrypt")
    print("\n=== DECRYPTION OPTIONS ===")
    print("4. XOR Decrypt")
    print("5. Swap Pixels Decrypt")
    print("6. Subtract Key Decrypt")
    print("\n=== EXIT ===")
    print("7. Exit")
    print("="*45)

def main():
    print("welcome to the image encrypt/decrypt tool!")
    print("Note: provide full path to image, eg: C:\\Users\\User\\Pictures\\image.jpg")
    print("Output path must include a file extension (jpg, png, bmp, gif, tiff, webp)")

    while True:
        display_menu()
        choice=input("Enter your choice: ").strip()

        if choice=="1":
            image_path=input("Enter image path: ").strip()
            try:
                key=int(input("Enter key (0-255): ").strip())
            except ValueError:
                print("Invalid key. Please enter a number between 0-255.")
                continue
            output_path=input("Enter output path: ").strip()
            try:
                xor_encrypt(image_path,key,output_path)
            except FileNotFoundError:
                print(f"Error: Input image file not found: {image_path}")
            except Exception as e:
                print(f"Error: {e}")

        elif choice=="2":
            image_path=input("Enter image path: ").strip()
            output_path=input("Enter output path: ").strip()
            try:
                encrypt_swap_pixels(image_path,output_path)
            except FileNotFoundError:
                print(f"Error: Input image file not found: {image_path}")
            except Exception as e:
                print(f"Error: {e}")

        elif choice=="3":
            image_path=input("Enter image path: ").strip()
            try:
                key=int(input("Enter key (0-255): ").strip())
            except ValueError:
                print("Invalid key. Please enter a number between 0-255.")
                continue
            output_path=input("Enter output path: ").strip()
            try:
                encrypt_add_key(image_path,key,output_path)
            except FileNotFoundError:
                print(f"Error: Input image file not found: {image_path}")
            except Exception as e:
                print(f"Error: {e}")

        elif choice=="4":
            image_path=input("Enter image path: ").strip()
            try:
                key=int(input("Enter key (0-255): ").strip())
            except ValueError:
                print("Invalid key. Please enter a number between 0-255.")
                continue
            output_path=input("Enter output path: ").strip()
            try:
                xor_decrypt(image_path,key,output_path)
            except FileNotFoundError:
                print(f"Error: Input image file not found: {image_path}")
            except Exception as e:
                print(f"Error: {e}")

        elif choice=="5":
            image_path=input("Enter image path: ").strip()
            output_path=input("Enter output path: ").strip()
            try:
                decrypt_swap_pixels(image_path,output_path)
            except FileNotFoundError:
                print(f"Error: Input image file not found: {image_path}")
            except Exception as e:
                print(f"Error: {e}")

        elif choice=="6":
            image_path=input("Enter image path: ").strip()
            try:
                key=int(input("Enter key (0-255): ").strip())
            except ValueError:
                print("Invalid key. Please enter a number between 0-255.")
                continue
            output_path=input("Enter output path: ").strip()
            try:
                decrypt_subtract_key(image_path,key,output_path)
            except FileNotFoundError:
                print(f"Error: Input image file not found: {image_path}")
            except Exception as e:
                print(f"Error: {e}")

        elif choice=="7":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__=="__main__":
    main()
