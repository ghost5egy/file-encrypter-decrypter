from core.crypter import cryptMsg
from core.file import filestream
import sys

def main():
	crypter = cryptMsg('this is my key')
	data = ''
	with open(sys.argv[1],'rb') as f :
		data = crypter.encrypt(str(f.read()))
	print(crypter.decrypt(data.decode()))

	with open('decrypted.txt','wb') as f :
		f.write(crypter.decrypt(data).encode())

	with open('encrypted.txt','wb') as f :
		f.write(data)

if __name__ == '__main__':
        main()
