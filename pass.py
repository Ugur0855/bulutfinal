''' 
Burada kullanıcı şifreleri hash içerikleri oluşturulmuştur.
Hash değerleri değişmemesi için sadece bir kere çalıştırılmalıdır, 
ardından settings.py dosyasında giriş bilgileri güncellenmelidir. 
'''

from passlib.hash import pbkdf2_sha256

hashadminsifresi = pbkdf2_sha256.hash("bulut")
print ("Admin şifresi(bulut): " + hashadminsifresi)

hashogrencisifresi = pbkdf2_sha256.hash("ugur")
print ("Öğrenci şifresi(ugur): " + hashogrencisifresi)

print("Doğrulama admin: ")
print(pbkdf2_sha256.verify("bulut", hashadminsifresi))

print("Doğrulama öğrenci: ")
print(pbkdf2_sha256.verify("ugur", hashogrencisifresi))