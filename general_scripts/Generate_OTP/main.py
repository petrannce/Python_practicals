import secrets

def generate_otp(length):
    """
    Generate a one-time password (OTP) of a specified length.
    
    Args:
        length (int): Length of the OTP. Default is 6.
    
    Returns:
        str: Generated OTP as a string.
    """
    if length <= 0:
        raise ValueError("Length must be a positive integer.")
    
    # Generate a random OTP
    otp = secrets.token_hex(length // 2)
    
    # Ensure the OTP is of the specified length
    return otp[:length]

if __name__ == "__main__":
    # Example usage
    otp_length = 6
    otp = generate_otp(otp_length)
    print(f"Generated OTP: {otp}")