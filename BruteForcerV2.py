import threading, hashlib, time, os
from tqdm import tqdm

class BruteForcer:
	def __init__(self):
		self.target = "5c826dec57ead18962537fd6d571c9ef4d6bac15441210a21ddfa894c371e13f"
		
		self.found = False
		self.auth = "6cvAq9HYbse4#c#="
		self.ip = [1, 1, 1, 1]
		for x in list(range(255)):
			self.ip[3] += x
			threading.Thread(target=self.Bruteforce, args=(list(self.ip), x)).start()

	def Hash(self, data):
		return hashlib.sha256((data+self.auth).encode('utf-8')).hexdigest()

	def Log(self, base, ip, c):
		while True:
			print(f"{base}: {c}: "+'.'.join([str(c) for c in ip])+":>"+self.Hash('.'.join([str(c) for c in ip]))+"\n")

	def Bruteforce(self, ip, base):
		time.sleep(0.1)
		base += 1
		c = 0
		while not (self.Hash('.'.join([str(c) for c in ip])) == self.target or self.found):
			c += 1

			ip[3] = base

			ip[2] += 1
			if ip[2] > 255:
				ip[2] = 1

				ip[1] += 1
				if ip[1] > 255:
					ip[1] = 1
					ip[0] += 1
					if ip[0] == 258:
						print("Ip not found!")
						os.system("PAUSE")

			if c % 50000 == 0:
				print(f"Thread {base}: {c}: "+'.'.join([str(c) for c in ip])+" :>"+self.Hash('.'.join([str(c) for c in ip]))+"\n")

		else:
			if not self.found:
				ip = '.'.join([str(c) for c in ip])
				self.found = True
				time.sleep(2.5)
				os.system("cls")
				print(f"Found Ip address {ip}!!")
				print(self.Hash(ip))
				print(ip)
				os.system("PAUSE")
			


if __name__ == "__main__":
	BruteForcer()
