
def isValid(user_input):

    if user_input.isalpha() or user_input == "0":
        
        return False 

    elif int(user_input) <= 0 : 
        
        return False

    else:

        return True
    
        

def doCalc(user_input):
    user_input = int(user_input)
    second = int(user_input/1000)
    minute = int(second/60) 
    hour = int(minute/60)
    second = second -minute*60
    minute = minute -hour*60
    
    if second > 0:
        sec_text = "{} second/s".format(second)
    
    elif minute == 0 and hour == 0: 
        
        sec_text = "just {} milisecond/s".format(user_input)

    else:
        sec_text = ""
    
    if minute > 0 : 
        min_text = "{} minute/s".format(minute)
    
    else:
        min_text = ""
    
    if hour > 0 : 
        hour_text = "{} hour/s".format(hour)
    else:
        hour_text = ""
    
    return f'{hour_text}' + f' {min_text}' + f' {sec_text}'