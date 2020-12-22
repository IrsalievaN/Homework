import csv

def csv_write(data, path):
	with open(path, "w") as csv_file:
		csv_write = csv.writer(csv_file, delimiter=",")
		for line in data:
			csv_write.writerow(line)

data = ["id,username,email,ip_address".split(","),
		"1,root,root@example.com,192.168.0.1".split(","), 
		"2,admin,admin@example.com,192.168.0.2".split(","),
		"3,test_user,test_user@example.com,192.168.0".split(","),
		"4,second_user,second_user@exampom,192.168.0.4".split(",")]


def csv_read(file, delimiter=","):
	reader = csv.DictReader(file, delimiter=delimiter)
	for line in reader:
		print('id:' + line['id'])
		print('username:' + line['username'])
		print('email:' + line['email'])
		print('ip_address:' + line['ip_address'])

path = "data.csv"
csv_write(data, path)
with open(path, "r") as file:
	csv_read(file)