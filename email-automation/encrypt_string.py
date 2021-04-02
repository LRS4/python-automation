# -*- coding: utf-8 -*-

from cryptography.fernet import Fernet
import urllib.parse


def encrypt_query_string(string: str, key: bytes) -> str:
    """Encrypts a string

    Encrypts a string using the given key and returns
    a URL friendly string parameter. This can be useful
    for generating URL parameters like for routes like
    /unsubscribe/?id=gAAAAABgZ10gsY1Z1Rz8VhCVxoXm...

    Args:
        string: The string to be encrypted
        key: The secret word

    Returns:
        A URL friendly encrypted string
    """
    encoded_string = string.encode()
    f = Fernet(key)

    encrypted_bytes = f.encrypt(encoded_string)
    print('encrypted_bytes: ' + str(encrypted_bytes))           # outputs gAAAAABgZ17jzX ... i5IizbmI=

    return urllib.parse.quote_from_bytes(encrypted_bytes)


def decrypt_query_string(string: str, key: bytes) -> str:
    """Decrypts a string

    Decrypts a string using the given key and returns
    the original string.

    Args:
        string: The encrypted URL parameter string
        key: The secret word

    Returns:
        The decrypted original string
    """
    f = Fernet(key)
    unquote_url_string = urllib.parse.unquote(string)

    decrypted_string = f.decrypt(unquote_url_string.encode())

    return decrypted_string.decode()


def main():
    key = b'L8AOOamFniJ07yBeFGDpVXR3feqQCfmU9sKcbYXaDJk='
    original_string = "john.doe@organisation.co.uk"

    encrypted_url_string = encrypt_query_string(string=original_string,
                                                key=key)

    decrypted_url_string = decrypt_query_string(string=encrypted_url_string,
                                                key=key)

    print('original_string: ' + original_string)                # outputs john.doe@organisation.co.uk
    print('encrypted_url_string: ' + encrypted_url_string)      # outputs gAAAAABgZ17jzX ... i5IizbmI%3D
    print('decrypted_url_string: ' + decrypted_url_string)      # outputs john.doe@organisation.co.uk


if __name__ == "__main__":
    main()
