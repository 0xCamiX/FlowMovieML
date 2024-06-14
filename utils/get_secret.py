import os


def get_secret(secret_name):
    return os.environ[secret_name]


def __main__():
    key = get_secret("AZURE_STORAGE_CONNECTION_STRING")
    print(os.path.realpath(__file__))
    return key


if __name__ == "__main__":
    __main__()


