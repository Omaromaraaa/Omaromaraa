import time
print("⌛ Welcome to Pomodoro Timer! ")

# نطلب من المستخدم يدخل الوقت بالدقايق
mins = int(input("Enter time in minutes : "))

# نحسب اجمالي عدد الثواني
total_seconds = mins*60

# نبدأ بالعد التنازلي
while total_seconds>0:

    # نحسب الدقايق المتبقية
    mins=total_seconds//60
    # نحسب الثواني المتبقية 
    secs=total_seconds%60

    clock = f"{mins:02d}:{secs:02d}"
    print(f"\rTime Remaining : {clock}",end="")

    time.sleep(1)
    total_seconds-=1
print("\ntime's UP , take a break")