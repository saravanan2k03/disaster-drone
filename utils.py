import socket

def isInternetAvailable():
    try:
        s = socket.create_connection(
              ("www.google.com", 80))
        if s is not None:
            s.close
        return True
    except OSError:
        pass
    return False