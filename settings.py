DEBUG = True
PORT = 8080
SECRET_KEY = "secret"
WTF_CSRF_ENABLED = True

PASSWORDS = {
    "admin": "$pbkdf2-sha256$29000$/j.HsPYe43yPUerdG2PsPQ$B0RDe/wjJ6JNSds8XNyyU4QtGpGSQU.ApLZOIJv81e0",
            #bulut

    "ogrenci": "$pbkdf2-sha256$29000$GSMkZMy5d85ZqxVi7D3HmA$6A2oz6/IhUFn5sxQxxVGapuMq4CISFIF9slvaA0nbEg",
            #ugur
}

ADMIN_USERS = ["admin"]
