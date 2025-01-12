import os 


def check_os():
    """ 
    Checking the operating system of the User for smooth experience 

    Args:
        None
    Returns:
        str: The operating system of the user.
    Example:
        check_os()
        This will return the operating system of the user.
        => 'windows'
        => 'linux'
        => 'mac'

    """

    if os.name == 'nt':
        return 'windows'
    elif os.name == 'posix':
        return 'linux'
    else:
        return 'mac'
