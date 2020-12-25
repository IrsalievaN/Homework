import json
import datetime


data = [
	{
	"id": "1",
	"username": "admin",
	"email": "admin@example.com",
	"registered_at": str(datetime.datetime.now())
	},
	{
	"id": "2",
	"username": "first_user",
	"email": "first_user@example.com",
	"registered_at": str(datetime.datetime.now())
	},
	{
	"id": "3",
	"username": "second_user",
	"email": "second_user@example.com",
	"registered_at": str(datetime.datetime.now())
	}
]

with open("data.json", "w") as file:
	json.dump(data, file)

with open("data.json") as file:
	print(json.load(file))
