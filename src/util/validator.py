import validators
import re


def validate_ip(ip):
    """Function to validate the ip given"""
    if (is_valid_ip(ip) == False):
        print("IP format incorrect")
        return False
    return True


def validate_domain_name(name):
    """Function to validate de domain name given"""
    if (is_valid_domain(name) == False):
        return False
    return True


def validate_ip_and_domain_name(target):
    """Function to validate both ip and domain name given"""
    if (is_valid_ip(target) or is_valid_domain(target)) == True:
        return True
    return False


def is_valid_ip(ip):
    """Auxiliary function to validate ipv4"""
    if (is_valid_ipv4(ip)):
        return True
    else:
        return False


def is_valid_ipv4(ip):
    """Validates IPv4 address"""
    if (ip == ''):
        print("Error. Incorrect input. The ip cannot be blank.")
        return False
    pattern = re.compile(r"""
        ^
        (?:
          # Dotted variants:
          (?:
            # Decimal 1-255 (no leading 0's)
            [3-9]\d?|2(?:5[0-5]|[0-4]?\d)?|1\d{0,2}
          |
            0x0*[0-9a-f]{1,2}  # Hexadecimal 0x0 - 0xFF (possible leading 0's)
          |
            0+[1-3]?[0-7]{0,2} # Octal 0 - 0377 (possible leading 0's)
          )
          (?:                  # Repeat 0-3 times, separated by a dot
            \.
            (?:
              [3-9]\d?|2(?:5[0-5]|[0-4]?\d)?|1\d{0,2}
            |
              0x0*[0-9a-f]{1,2}
            |
              0+[1-3]?[0-7]{0,2}
            )
          ){0,3}
        |
          0x0*[0-9a-f]{1,8}    # Hexadecimal notation, 0x0 - 0xffffffff
        |
          0+[0-3]?[0-7]{0,10}  # Octal notation, 0 - 037777777777
        |
          # Decimal notation, 1-4294967295:
          429496729[0-5]|42949672[0-8]\d|4294967[01]\d\d|429496[0-6]\d{3}|
          42949[0-5]\d{4}|4294[0-8]\d{5}|429[0-3]\d{6}|42[0-8]\d{7}|
          4[01]\d{8}|[1-3]\d{0,9}|[4-9]\d{0,8}
        )
        $
    """, re.VERBOSE | re.IGNORECASE)
    if (pattern.match(ip) is not None):
        return True
    print("Error. The IPv4 format is incorrect.")
    return False


def is_valid_domain(name):
    """Validates domain names"""
    if (validators.domain(name) == True):
        return True
    print("Error. Domain name format is incorrect.")
    return False


def is_valid_register(register):
    if (register == ''):
        print("Error. Incorrect input. The register cannot be blank.")
        return False
    if (register != ''):
        try:
            register = int(register)
        except:
            print("Error. Incorrect input. The given register is not an integer.")
            return False
    if (register < 0 or register > 65535):
        print("Error. Incorrect input. The register should be greater than 0 and less than 65536.")
        return False
    return True


def is_valid_uid(uid):
    if (uid == ''):
        print("Error. Incorrect input. The uid cannot be blank.")
        return False
    if (uid != ''):
        try:
            uid = int(uid)
        except:
            print("Error. Incorrect input. The given uid is not an integer.")
            return False
    if (uid < 0 or uid > 255):
        print("Error. Incorrect input. The uid should be greater than 0 and less than 256.")
        return False
    return True

def is_valid_coil_value(coil_value):
    if (coil_value == ''):
        print("Error. Incorrect input. The coil value cannot be blank.")
        return False
    coil_value_upper = coil_value.upper()
    if (coil_value_upper == "ON" or coil_value_upper == "OFF"):
        return True
    print("Error. Incorrect input. The coil value can only be ON or OFF.")
    return False
