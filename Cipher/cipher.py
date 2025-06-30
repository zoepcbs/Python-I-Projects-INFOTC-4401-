def create_encode_dict():
    
    input_chars = "abcdefghijklmnopqrstuvwxyz"
    replace_chars = "0123456789!@#$%^&*()+-<>?="
    
    encode_dict = {}
    for i in range(len(input_chars)):
        encode_dict[input_chars[i]] = replace_chars[i]
    
    return encode_dict


def create_decode_dict():
    
    input_chars = "abcdefghijklmnopqrstuvwxyz"
    replace_chars = "0123456789!@#$%^&*()+-<>?="
    
    decode_dict = {}
    for i in range(len(replace_chars)):
        decode_dict[replace_chars[i]] = input_chars[i]
    
    return decode_dict


def encode_message(message, encode_dict):
    
    encoded = ""
    
    for char in message:
        if char.lower() in encode_dict:
            encoded += encode_dict[char.lower()]
        else:
            encoded += char
    
    return encoded


def decode_message(message, decode_dict):

    decoded = ""
    for char in message:
        if char in decode_dict:
            decoded += decode_dict[char]
        else:
            decoded += char
    
    return decoded

def main():
    
    encode_dict = create_encode_dict()
    decode_dict = create_decode_dict()
    
    while True:
        print("\nWelcome to the Secret Message Encoder/Decoder")
        print("1. Encode a message")
        print("2. Decode a message")
        print("3. Exit")
        
        choice = input("\nWhat would you like to do? ")
        
        if choice == "1":
            message = input("Enter a message to encode: ")
            encoded = encode_message(message, encode_dict)
            print(f"Encoded message: {encoded}")
        elif choice == "2":
            message = input("Enter a message to decode: ")
            decoded = decode_message(message, decode_dict)
            print(f"Decoded message: {decoded}")
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
