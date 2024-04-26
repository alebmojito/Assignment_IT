import random

# Function to generate CRC checksum
def generate_crc(data):
    crc = 0xFFFF
    polynomial = 0x1021
    for byte in data:
        crc ^= (byte << 8)
        for _ in range(8):
            if crc & 0x8000:
                crc = (crc << 1) ^ polynomial
            else:
                crc <<= 1
            crc &= 0xFFFF
    return crc

# Simulate data transmission with errors
def simulate_transmission(data):
    # Introduce errors in transmission with a probability of 10%
    corrupted_data = bytearray(data)
    for i in range(len(corrupted_data)):
        if random.random() < 0.1:
            corrupted_data[i] ^= 0xFF
    return corrupted_data

# Main function to demonstrate error detection using CRC checksum
def main():
    # Original data
    original_data = b'RMIT'
    print(original_data , type(original_data))
    # Simulate transmission with possible errors
    transmitted_data = simulate_transmission(original_data)
    print()
    # Check CRC checksum of transmitted data
    transmitted_crc = generate_crc(transmitted_data)
    
    # Check CRC checksum of received data
    received_crc = generate_crc(transmitted_data)
    print(transmitted_data , hex(transmitted_crc) , hex(received_crc))
    # Compare CRC checksums to detect errors
    try:
        if transmitted_crc == received_crc:
            print("No errors detected. Data is intact:", transmitted_data.decode())
        else:
            print("Errors detected in transmitted data. Data may be corrupted.")
    except UnicodeDecodeError as e : 
        print(e)

if __name__ == "__main__":
    main()
