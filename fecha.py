import datetime

year = int(input("Any: "))
month = int(input("Mes: "))
day = int(input("Dies: "))

avui = datetime.datetime.now()
user_date = datetime.datetime (year=year, month=month, day=day)

time_remaining = user_date - datetime.datetime.now()


print("{} dies,{} hores".format(time_remaining.days, int(time_remaining.seconds / 60 / 60)))