import man_db
import os


def main():
	if not os.path.exists("index.db"):
		print("To create an index you first have to run main.py!")
		exit(0)
	man = man_db.man()
	print("This is a db manager! Please enter your command. For Example: SELECT * from urls where Url=https://www.wikipedia.com AND Sheme=https")
	while True:
		search = input("Enter search: ")
		try:
			if search == "exit":
				exit(0)
			results = man.read(search)
			print(results)
		except:
			print("Not found")
	
	
	
if __name__ == "__main__":
	main()
