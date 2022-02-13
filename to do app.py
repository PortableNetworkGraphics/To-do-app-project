from datetime import date
import sys

# Opening and reading the file

f = open('events.txt','r',encoding="utf-8")
read = f.readlines()
f.close()
task_list = []
for task in read:
    data = task.replace("\n", "").split(";")
    date_object = data[2].split("-")
    task_list.append({
    "name":data[0],
    "des":data[1],
    "date": date(int(date_object[0]), int(date_object[1]), int(date_object[2]))
})

# Console commands
print("To add a task press 1.")
print("In order to see the latest tasks press 2.")
print("To close the program press 3.")


while True:
    pyk = input()
    if pyk == "1":              # Adding a new task
        task_list.append({
        "name": input("Name: "),
        "des": input("Description: "),
        "date": date(int(input("Year: ")), int(input("Month: ")), int(input("Day: ")))
        })
        print("Task added.")
    elif pyk == "2":            # Showing 5 most recent tasks
         task_list.sort(key=lambda item: item.get("date"))
         print("Here are your 5 most recent tasks:\n")
         print("1. " + str(task_list[0].get("name")) + " -- " + str(task_list[0].get("des")) + " -- " + str(task_list[0].get("date")))
         print("2. " + str(task_list[1].get("name")) + " -- " + str(task_list[1].get("des")) + " -- " + str(task_list[1].get("date")))
         print("3. " + str(task_list[2].get("name")) + " -- " + str(task_list[2].get("des")) + " -- " + str(task_list[2].get("date")))
         print("4. " + str(task_list[3].get("name")) + " -- " + str(task_list[3].get("des")) + " -- " + str(task_list[3].get("date")))
         print("5. " + str(task_list[4].get("name")) + " -- " + str(task_list[4].get("des")) + " -- " + str(task_list[4].get("date")) + "\n")
    elif pyk == "3":            # Saving the changes and closing the program
        with open('events.txt', "w") as myfile:
            string1 = ""
            for elements in task_list:
                 string1 = string1 + str(elements.get("name")) + ";" + str(elements.get("des")) + ";" + str(elements.get("date")) + "\n"
            myfile.write(str(string1))
            print("FILE SAVED :)")
            f.close()
            sys.exit("")





