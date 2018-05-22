import socket 

def retbanner(ipaddr, port):
	try:
		socket.setdefaulttimeout(2)
		s = socket.socket()
		s.connect((ipaddr, port))
		banner = s.recv(1024)
		return banner
	except:
		return

def main():
	ip1 = "192.168.178.54"
	ip2 = "192.168.178.4"
	port = 21

	banner1 = retbanner(ip1, port)
	if banner1:
		print("[+] " + str(ip1) + ": " + str(banner1) + " [+]")
	else:
		print("[-] No response from host [-]")

	banner2 = retbanner(ip2 ,port)
	if banner2:
		print("[+] " + str(ip1) + ": " + str(banner1) + " [+]")
	else:
		print("[-] No response form host [-]")

if __name__ == "__main__":
	main()