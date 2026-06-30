a = int(input("Enter the melting temperature of your metal: "))

if a > 3000:
    print("This metal is suitable for incandescent filament")
elif a >= 1000:
    print("This metal is suitable for incandescent filament, but efficiency is undefined")
else:
    print("This metal is not suitable at all")
