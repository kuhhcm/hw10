import datetime
import calendar
import os
import shutil
## Задание 1

# def get_week_number(year, month, day):
#     date = datetime.date(year, month, day)
#     week_number = date.isocalendar()[1]
#     return week_number

# year = 2015
# month = 6
# day = 16

# week_number = get_week_number(year, month, day)
# print(f"Номер недели  {day}.{month}.{year}: {week_number}")



# # Задание 2

# def get_first_monday(year, week):
#     first_day = datetime.date(year, 1, 1)
#     starting_weekday = first_day.weekday()
#     days_to_add = 0 if starting_weekday == 0 else 7 - starting_weekday
#     get_first_monday = first_day + datetime.timedelta(days=days_to_add)
#     target_date = get_first_monday + datetime.timedelta(weeks=week-1)
#     return target_date

# year = int(input("Введите год: "))
# week = int(input("Введите номер недели: "))
# result = get_first_monday(year, week)

# print(f"Дата первого понедельника {week} недели {year} года: {result}")



# # Задание 3
# def get_all_sundays(year):
#     sundays = []
#     date = datetime.date(year, 1, 1)
#     while date.year == year:
#         if date.weekday() == 6:
#             sundays.append(date)
#         date += datetime.timedelta(days=1)
#     return sundays

# year = int(input('Введите год: '))
# sundays = get_all_sundays(year)

# for sunday in sundays:
#     print(sunday.strftime("%Y-%m-%d"))

# # Задание 4
# date_string = input("Введите исходную дату (в формате дд.мм.гггг): ")
# date = datetime.strptime(date_string, "%d.%m.%Y")

# years = int(input("Введите количество лет для добавления: "))
# new_date = date + timedelta(days=years*365)

# print("Новая дата:", new_date.strftime("%d.%m.%Y"))


# # Задание 5
# gmt_time = datetime.now(timezone.utc)
# local_time = datetime.now()

# print(f"Время по Гринвичу: {gmt_time.strftime('%H:%M')}")
# print(f"Местное время: {local_time.strftime('%H:%M')}")



# # Задание 6
# date1 = date(2019, 6, 9)
# date2 = date(2020, 12, 31)

# delta = date2 - date1
# print("Количество дней:", delta.days)



# # Задание 7
# diff1 = datetime.timedelta(days=10, hours=3, minutes=30, seconds=15)
# diff2 = datetime.timedelta(days=3, hours=5, minutes=10, seconds=35)

# total_diff = diff1 + diff2    

# days = total_diff.days
# hours, remainder = divmod(total_diff.seconds, 3600)
# minutes, seconds = divmod(remainder, 60)

# print("Дни:", days)
# print("Часы:", hours)
# print("Минуты:", minutes)
# print("Секунды:", seconds)



# # Задание 8
# year = int(input("Введите год: "))
# month = int(input("Введите месяц: "))

# cal = calendar.HTMLCalendar()
# html = cal.formatmonth(year, month)

# with open("calendar.html", "w") as file:
#     file.write(html)
#     print("HTML-календарь создан.")




# # Задание 9
# def remove_unacceptable_words(text_file, unacceptable_file):
#     with open(text_file, 'r') as f:
#         content = f.read()
    
#     with open(unacceptable_file, 'r') as f:
#         unacceptable_words = f.read().splitlines()
    
#     for word in unacceptable_words:
#         content = content.replace(word, '')
    
#     with open('new_text.txt', 'w') as f:
#         f.write(content)



# # Задание 10
# os.mkdir("watch_me")

# video_files = os.listdir("video")
# for file in video_files:
#     source = os.path.join("video", file)
#     destination = os.path.join("watch_me", file)
#     shutil.move(source, destination)

# sub_files = os.listdir("sub")
# for file in sub_files:
#     source = os.path.join("sub", file)
#     destination = os.path.join("watch_me", file)
#     shutil.move(source, destination)




# # Задание 11
# files = os.listdir()
# for file in files:
#     if file.endswith(".jpg"):
#         first_name, last_name = file.split("_")
#         new_name = f"{last_name}_{first_name}"
#         os.rename(file, new_name)





# # Задание 12
# os.mkdir("list")
# with open("list.tsv", "r") as f:
#     file_names = f.read().splitlines()

# for file_name in file_names:
#     source = os.path.join(".", file_name)
#     destination = os.path.join("list", file_name)
#     shutil.move(source, destination)




# # Задание 13
# with open("input.txt", "r") as f:
#     lines = f.readlines()

# edited_lines = lines[:-1]

# with open("output.txt", "w") as f:
#     f.writelines(edited_lines)