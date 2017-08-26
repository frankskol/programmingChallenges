import os
import zipfile
import sys

def main(path):
	if not os.path.exists(path):
		print("Arquivo {} não existe".format(path))
		sys.exit(-1)
	else:
		try:
			zfile = zipfile.ZipFile(path)
			zfile.extractall()
			print ("Arquivos extraídos")
		except (RuntimeError):
			password = input("Arquivo com senha, digite a senha:\n")
			zfile.extractall(pwd = bytes(password, 'utf-8'))
			print ("Arquivos extraídos")
if __name__ == "__main__":
	main(sys.argv[1])