def validate_ip(ip_address):
    # Split the IP address by dots
    parts = ip_address.split('.')

    # Check if we have exactly 4 parts
    if len(parts) != 4:
        return False

    for part in parts:
        # Check if the part is numeric
        if not part.isdigit():
            return False

        # Convert to integer and check range
        num = int(part)
        if not (0 <= num <= 255):
            return False

        # Check for leading zeros
        if part != str(num):
            return False

    return True


# Example usage
print(validate_ip("192.168.0.1"))  # True
print(validate_ip("127.0.0.1"))  # True
print(validate_ip("256.100.50.0"))  # False
print(validate_ip("192.168.0"))  # False
