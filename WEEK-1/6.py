##Create a program that
##converts a given number of seconds into hours, minutes, and seconds.
seconds=int(input("Enter the Seconds: "))
minutes= seconds/60
hours=minutes/60
left_seconds=seconds%60
print("Hours: ",int(hours),",Mintues: ",int(minutes),",Seconds: ",left_seconds)
print(int(hours),int(minutes),left_seconds,sep=",")


