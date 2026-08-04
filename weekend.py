def is_today_weekend(day):
    match day:
        case "Saturday" | "Sunday":
            return True
        case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":       
            return False
        case _:
            print("Not even a real day, so")
            return False

    
print("Yes" if is_today_weekend("Sunday") is True else "Nope")