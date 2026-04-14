import os
import time
import secrets
import string

TRAP_FILENAME = "Secret_Passwords.txt"
CHECK_INTERVAL = 0.5

def generate_garbage(length=10000):
	characters = string.ascii_letters + string.digits + string.punctuation
	return ''.join(secrets.choice(characters) for _ in range(length))

def create_trap():
	with open(TRAP_FILENAME, "w") as f:
		f.write("Google_Account: vartakvarad3@gmail.com\nPassword: Varad@2007v")
	print(f"[*] Trap file '{TRAP_FILENAME}' created. Monitoring for hackers...")

def monitor_trap():
	try:
		last_access = os.path.getatime(TRAP_FILENAME)
	except FileNotFoundError:
		create_trap()
		last_access = os.path.getatime(TRAP_FILENAME)

	try:
		while True:
			try:
				current_access = os.path.getatime(TRAP_FILENAME)
				if current_access != last_access:
					print(f"[!] ALERT: Intrusion detected on {TRAP_FILENAME}!")
					last_access = current_access
			except FileNotFoundError:
				print("[!] File deleted. Recreating trap...")
				create_trap()
				last_access = os.path.getatime(TRAP_FILENAME)
			time.sleep(CHECK_INTERVAL)
	except KeyboardInterrupt:
		print("\nStopped monitoring.")

if __name__ == "__main__":
	create_trap()
	monitor_trap()