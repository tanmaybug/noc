from fastapi import UploadFile
from config.config import settings

def validate(file: UploadFile):
    # file_type = file.content_type
    # print(file.size)

    MAX_FILE_SIZE = settings.MAX_FILE_SIZE  
    MIN_FILE_SIZE = settings.MIN_FILE_SIZE  

    accepted_file_types = [
        "image/png",
        "image/jpeg",
        "image/jpg",
        "png",
        "jpeg",
        "jpg",
    ]

    if file.content_type not in accepted_file_types:
        print("type error")
        return False
    elif file.size is not None and file.size > MAX_FILE_SIZE and file.size < MIN_FILE_SIZE:
        print("size error")
        return False
    else:
        return True