#MilesToStuds

def System():
    #SystemStart
    MileInput = float(input("How many miles are you looking to convert? "))

    #Mathematics
    MileToMetre = 1609.344
    MetreToStud = 0.28

    #Convertion
    ConvertMileToMetre = MileInput * MileToMetre
    ConvertMetreToStud = ConvertMileToMetre / MetreToStud

    #ConvertToRobloxRealism
    RobloxRealisticScale = ConvertMetreToStud / 4

    #ReturnResult
    print("Realistic Studs: ")
    print(round(ConvertMetreToStud, 3))

    print("----")

    print("Roblox Scale Studs: ")
    print(round(RobloxRealisticScale, 3))

    #RepeatSystem
    System()

System()