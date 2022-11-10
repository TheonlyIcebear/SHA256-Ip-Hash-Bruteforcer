import threading, hashlib, time, os
from numba import jit, cuda
from tqdm import tqdm
import numpy as np

class BruteForcer:
	def __init__(self):
		self.target = "846ca2be9e1a2df44175beb37cc8c9b940190db708bb88887743a1d36ed850a5"
		self.found = False
		threads = 1000000
		for x in list(range(threads)):
			threading.Thread(target=self.Bruteforce, args=(threads, x)).start()

	def Hash(self, data):
		return hashlib.sha256((data).encode('utf-8')).hexdigest()

	def Log(self, base, ip, c):
		while True:
			print(f"{base}: {c}: "+'.'.join([str(c) for c in ip])+":>"+self.Hash('.'.join([str(c) for c in ip]))+"\n")

	def Bruteforce(self, threads, base):
		c = 0
		thread = int(base)
		ip = [(base // (256 ** 3))+1, ((base // (256**2)) % 255), ((base // 256) % 255)+1, (base % 255)+1]

		while not (self.Hash('.'.join([str(c) for c in ip])) == self.target or self.found):
			c += 1
			ip = [(base // (256 ** 3))+1, ((base // (256**2)) % 255)+1, ((base // 256) % 255)+1, (base % 255)+1]
			base += threads

			if ip[0] >= 256:
				break

			if thread % 100 == 0:
				print(f"Thread {thread}: {c}: "+'.'.join([str(c) for c in ip])+" :>"+self.Hash('.'.join([str(c) for c in ip]))+"\n")

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