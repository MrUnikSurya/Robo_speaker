import os
if __name__ == '__main__':
     print("Welcome to artificial speaker created by Surya")
     while True:
         x = input("Enter what you want robo to speak: ")
         if x == 'q':
             break
         semi_command = f"(New-Object -ComObject SAPI.SpVoice).Speak('{x}')"
         command = f"powershell -Command {semi_command}"
         os.system(command)


