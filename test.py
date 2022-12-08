print("Welcome to STRATIS Lofts Admin Portal\n4230 Main St.\nPhiladelphia, PA 19127")
fname = input("\nPlease Enter Your First Name: ")
lname = input("Please Enter Your Last Name: ")
if fname == "Ty" and lname == "Adams":
    print(f"\nWelcome, {fname} {lname}!")
elif fname == "Mackenzie" and lname == "Carroll":
    print(f"\nWelcome, {fname} {lname}!")
elif fname == "Zakiyya" and lname == "Shabazz":
    print(f"\nWelcome, {fname} {lname}!")
elif fname == "Duane" and lname == "Velasquez":
    print(f"\nWelcome, {fname} {lname}!")
elif fname == "Dorothea" and lname == "Brooke":
    print(f"\nWelcome, {fname} {lname}!")
elif fname == "Jian" and lname == "Ma":
    print(f"\nWelcome, {fname} {lname}!")
else:
    print("\nInvalid User")
    import sys
    sys.exit()

if fname == "Mackenzie" and lname == "Carroll":
    print("\nUnit: 102\nName: Mackenzie Carroll\nRole: Resident\nDevices:\n-Thermostat: Warm-Me\n-Lights: Bright Ideas\n-Locks: LockNess")
elif fname == "Duane" and lname == "Velasquez":
    print("\nUnit: 202\nName: Duane Velasquez\nRole: Resident\nDevices:\n-Thermostat: Warm-Me\n-Lights: Bright Ideas\n-Locks: SkeletonKey")
elif fname == "Dorothea" and lname == "Brooke":
    print("\nUnit: 301\nName: Dorothea Brooke\nRole: Resident\nDevices:\n-Thermostat: Warm-Me\n-Lights: Bright Ideas, Sunnee\n-Locks: LockNess")
elif fname == "Jian" and lname == "Ma":
    print("\nUnit: 301\nName: Jian Ma\nRole: Resident\nDevices:\n-Thermostat: Warm-Me\n-Lights: Bright Ideas, Sunnee\n-Locks: LockNess")
elif fname == "Ty" and lname == "Adams":
    print("\nUnit: 101\nName: Ty Adams\nRole: Admin, Resident\nDevices:\n-Thermostat: Warm-Me\n-Lights: Bright Ideas, Sunnee\n-Locks: LockNess")
elif fname == "Zakiyya" and lname == "Shabazz":
    print("\nUnit: 201\nName: Zakiyya Shabazz\nRole: Admin, Resident\nDevices:\n-Thermostat: Warm-Me\n-Lights: Bright Ideas, Sunnee\n-Locks: LockNess")
else:
    print("\nInvalid User")
    import sys
    sys.exit()


if fname == "Ty" or fname == "Zakiyya" or lname == "Adams" or lname == "Shabazz":
    search = input("\nSearch for First Name & Last Name or The Unit Number: ")

    if search == "101":
        tname = ("Ty Adams")
        listat = ("Off")
        lostat =("Locked")
        print(f"\nUnit: {search}\nName: {tname}\nRole: Admin, Resident\nDevices:\n-Thermostat: Warm-Me\n-Lights: Bright Ideas, Sunnee ({listat})\nLocks: SkeletonKey ({lostat})")
        access = input("\nType 1 to Change Tenant\nType 2 to Control Sunnee Lights\nType 3 to lock/unlock the unit\nType 4 to exit\n\nEnter Option: ")
        if access == "1":
            tname = input("\nEnter name of the new tenant: ")
            print(f"\n**Changes has been saved.**\n\nUnit: {search}\nName: {tname}\nRole: Admin, Resident\nDevices:\n-Thermostat: Warm-Me\n-Lights: Bright Ideas, Sunnee ({listat})\n-Locks: SkeletonKey ({lostat})")
            access = input("\nType 1 to Exit\n\nEnter Option: ")
            if access == "1":
                import sys
                sys.exit()
            else:
                print("Invalid option, forcing to exit...")
                import sys
                sys.exit()
        if access == "2":
            listat = input("\nType 1 to turn off the Sunnee Lights\nType 2 to turn on the Sunnee lights\n\nEnter Option: ")
            if listat == "1":
                listat = ("Off")
                print(f"\n**Changes has been saved.**\n\nUnit: {search}\nName: {tname}\nRole: Admin, Resident\nDevices:\n-Thermostat: Warm-Me\n-Lights: Bright Ideas, Sunnee ({listat})\n-Locks: SkeletonKey ({lostat})")
                access = input("\nType 1 to Exit\n\nEnter Option: ")
                if access == "1":
                    import sys
                    sys.exit()
                else:
                    print("Invalid option, forcing to exit...")
                    import sys
                    sys.exit()
            elif listat == "2":
                listat = ("On")
                print(f"\n**Changes has been saved.**\n\nUnit: {search}\nName: {tname}\nRole: Admin, Resident\nDevices:\n-Thermostat: Warm-Me\n-Lights: Bright Ideas, Sunnee ({listat})\n-Locks: SkeletonKey ({lostat})")
                access = input("\nType 1 to Exit\n\nEnter Option: ")
                if access == "1":
                    import sys
                    sys.exit()
                else:
                    print("Invalid option, forcing to exit...")
                    import sys
                    sys.exit()
            else:
                print("Invalid Option, exiting...")
                import sys
                sys.exit()
        if access == "3":
            lostat = input("\nType 1 to lock the unit\nType 2 to unlock the unit\n\nEnter Option: ")
            if lostat == "1":
                lostat = ("Locked")
                print(f"\n**Changes has been saved.**\n\nUnit: {search}\nName: {tname}\nRole: Admin, Resident\nDevices:\n-Thermostat: Warm-Me\n-Lights: Bright Ideas, Sunnee ({listat})\n-Locks: SkeletonKey ({lostat})")
                access = input("\nType 1 to Exit\n\nEnter Option: ")
                if access == "1":
                    import sys
                    sys.exit()
                else:
                    print("Invalid option, forcing to exit...")
                    import sys
                    sys.exit()
            elif lostat == ("2"):
                lostat = ("Unlocked")
                print(f"\n**Changes has been saved.**\n\nUnit: {search}\nName: {tname}\nRole: Admin, Resident\nDevices:\n-Thermostat: Warm-Me\n-Lights: Bright Ideas, Sunnee ({listat})\n-Locks: SkeletonKey ({lostat})")
                access = input("\nType 1 to Exit\n\nEnter Option: ")
                if access == "1":
                    import sys
                    sys.exit()
                else:
                    print("Invalid option, forcing to exit...")
                    import sys
                    sys.exit()
            else:
                print("Invalid Option, forcing to exit...")
                import sys
                sys.exit()


        if access == "4":
            import sys
            sys.exit()

    elif search == "Ty Adams":
        unit = ("101")
        listat = ("Off")
        lostat =("Locked")
        print(f"\nUnit: {unit}\nName: {search}\nRole: Admin, Resident\nDevices:\n-Thermostat: Warm-Me\n-Lights: Bright Ideas, Sunnee ({listat})\nLocks: SkeletonKey ({lostat})")
        access = input("\nType 1 to Change Tenant\nType 2 to Control Sunnee Lights\nType 3 to lock/unlock the unit\nType 4 to exit\n\nEnter Option: ")
        if access == "1":
            search = input("\nEnter name of the new tenant: ")
            print(f"\n**Changes has been saved.**\n\nUnit: {unit}\nName: {search}\nRole: Admin, Resident\nDevices:\n-Thermostat: Warm-Me\n-Lights: Bright Ideas, Sunnee ({listat})\n-Locks: SkeletonKey ({lostat})")
            access = input("\nType 1 to Exit\n\nEnter Option: ")
            if access == "1":
                import sys
                sys.exit()
            else:
                print("Invalid option, forcing to exit...")
                import sys
                sys.exit()
        if access == "2":
            listat = input("\nType 1 to turn off the Sunnee Lights\nType 2 to turn on the Sunnee lights\n\nEnter Option: ")
            if listat == "1":
                listat = ("Off")
                print(f"\n**Changes has been saved.**\n\nUnit: {unit}\nName: {search}\nRole: Admin, Resident\nDevices:\n-Thermostat: Warm-Me\n-Lights: Bright Ideas, Sunnee ({listat})\n-Locks: SkeletonKey ({lostat})")
                access = input("\nType 1 to Exit\n\nEnter Option: ")
                if access == "1":
                    import sys
                    sys.exit()
                else:
                    print("Invalid option, forcing to exit...")
                    import sys
                    sys.exit()
            elif listat == "2":
                listat = ("On")
                print(f"\n**Changes has been saved.**\n\nUnit: {unit}\nName: {search}\nRole: Admin, Resident\nDevices:\n-Thermostat: Warm-Me\n-Lights: Bright Ideas, Sunnee ({listat})\n-Locks: SkeletonKey ({lostat})")
                access = input("\nType 1 to Exit\n\nEnter Option: ")
                if access == "1":
                    import sys
                    sys.exit()
                else:
                    print("Invalid option, forcing to exit...")
                    import sys
                    sys.exit()
            else:
                print("Invalid Option, exiting...")
                import sys
                sys.exit()
        if access == "3":
            lostat = input("\nType 1 to lock the unit\nType 2 to unlock the unit\n\nEnter Option: ")
            if lostat == "1":
                lostat = ("Locked")
                print(f"\n**Changes has been saved.**\n\nUnit: {unit}\nName: {search}\nRole: Admin, Resident\nDevices:\n-Thermostat: Warm-Me\n-Lights: Bright Ideas, Sunnee ({listat})\n-Locks: SkeletonKey ({lostat})")
                access = input("\nType 1 to Exit\n\nEnter Option: ")
                if access == "1":
                    import sys
                    sys.exit()
                else:
                    print("Invalid option, forcing to exit...")
                    import sys
                    sys.exit()
            elif lostat == ("2"):
                lostat = ("Unlocked")
                print(f"\n**Changes has been saved.**\n\nUnit: {unit}\nName: {search}\nRole: Admin, Resident\nDevices:\n-Thermostat: Warm-Me\n-Lights: Bright Ideas, Sunnee ({listat})\n-Locks: SkeletonKey ({lostat})")
                access = input("\nType 1 to Exit\n\nEnter Option: ")
                if access == "1":
                    import sys
                    sys.exit()
                else:
                    print("Invalid option, forcing to exit...")
                    import sys
                    sys.exit()
            else:
                print("Invalid Option, forcing to exit...")
                import sys
                sys.exit()


        if access == "4":
            import sys
            sys.exit()

    elif search == "Mackenzie Carroll":
        unit = ("102")
        lostat =("Locked")
        print(f"\nUnit: {unit}\nName: {search}\nRole: Resident\nDevices:\n-Thermostat: Warm-Me\n-Lights: Bright Ideas\n-Locks: SkeletonKey ({lostat})")
        access = input("\nType 1 to Change Tenant\nType 2 to lock/unlock the unit\nType 3 to exit\n\nEnter Option: ")
        if access == "1":
            search = input("\nEnter name of the new tenant: ")
            print(f"\n**Changes has been saved.**\n\nUnit: {unit}\nName: {search}\nRole: Resident\nDevices:\n-Thermostat: Warm-Me\n-Lights: Bright Ideas\n-Locks: LockNess ({lostat})")
            access = input("\nType 1 to Exit\n\nEnter Option: ")
            if access == "1":
                import sys
                sys.exit()
            else:
                print("Invalid option, forcing to exit...")
                import sys
                sys.exit()
        if access == "2":
            lostat = input("\nType 1 to lock the unit\nType 2 to unlock the unit\n\nEnter Option: ")
            if lostat == "1":
                lostat = ("Locked")
                print(f"\n**Changes has been saved.**\n\nUnit: {unit}\nName: {search}\nRole: Resident\nDevices:\n-Thermostat: Warm-Me\n-Lights: Bright Ideas\n-Locks: LockNess ({lostat})")
                access = input("\nType 1 to Exit\n\nEnter Option: ")
                if access == "1":
                    import sys
                    sys.exit()
                else:
                    print("Invalid option, forcing to exit...")
                    import sys
                    sys.exit()
            elif lostat == ("2"):
                lostat = ("Unlocked")
                print(f"\n**Changes has been saved.**\n\nUnit: {unit}\nName: {search}\nRole: Resident\nDevices:\n-Thermostat: Warm-Me\n-Lights: Bright Ideas\n-Locks: LockNess ({lostat})")
                access = input("\nType 1 to Exit\n\nEnter Option: ")
                if access == "1":
                    import sys
                    sys.exit()
                else:
                    print("Invalid option, forcing to exit...")
                    import sys
                    sys.exit()
            else:
                print("Invalid Option, forcing to exit...")
                import sys
                sys.exit()
        if access == "3":
            import sys
            sys.exit()

    elif search == "102":
        tname = ("Mackenzie Carroll")
        lostat =("Locked")
        print(f"\nUnit: {search}\nName: {tname}\nRole: Resident\nDevices:\n-Thermostat: Warm-Me\n-Lights: Bright Ideas\n-Locks: SkeletonKey ({lostat})")
        access = input("\nType 1 to Change Tenant\nType 2 to lock/unlock the unit\nType 3 to exit\n\nEnter Option: ")
        if access == "1":
            tname = input("\nEnter name of the new tenant: ")
            print(f"\n**Changes has been saved.**\n\nUnit: {search}\nName: {tname}\nRole: Resident\nDevices:\n-Thermostat: Warm-Me\n-Lights: Bright Ideas\n-Locks: LockNess ({lostat})")
            access = input("\nType 1 to Exit\n\nEnter Option: ")
            if access == "1":
                import sys
                sys.exit()
            else:
                print("Invalid option, forcing to exit...")
                import sys
                sys.exit()
        if access == "2":
            lostat = input("\nType 1 to lock the unit\nType 2 to unlock the unit\n\nEnter Option: ")
            if lostat == "1":
                lostat = ("Locked")
                print(f"\n**Changes has been saved.**\n\nUnit: {search}\nName: {tname}\nRole: Resident\nDevices:\n-Thermostat: Warm-Me\n-Lights: Bright Ideas\n-Locks: LockNess ({lostat})")
                access = input("\nType 1 to Exit\n\nEnter Option: ")
                if access == "1":
                    import sys
                    sys.exit()
                else:
                    print("Invalid option, forcing to exit...")
                    import sys
                    sys.exit()
            elif lostat == ("2"):
                lostat = ("Unlocked")
                print(f"\n**Changes has been saved.**\n\nUnit: {search}\nName: {tname}\nRole: Resident\nDevices:\n-Thermostat: Warm-Me\n-Lights: Bright Ideas\n-Locks: LockNess ({lostat})")
                access = input("\nType 1 to Exit\n\nEnter Option: ")
                if access == "1":
                    import sys
                    sys.exit()
                else:
                    print("Invalid option, forcing to exit...")
                    import sys
                    sys.exit()
            else:
                print("Invalid Option, forcing to exit...")
                import sys
                sys.exit()
        if access == "3":
            import sys
            sys.exit()

    elif search == "Zakiyya Shabazz":
        unit = ("201")
        listat = ("Off")
        lostat =("Locked")
        print(f"\nUnit: {unit}\nName: {search}\nRole: Admin, Resident\nDevices:\n-Thermostat: Warm-Me\n-Lights: Bright Ideas, Sunnee ({listat})\nLocks: LockNess ({lostat})")
        access = input("\nType 1 to Change Tenant\nType 2 to Control Sunnee Lights\nType 3 to lock/unlock the unit\nType 4 to exit\n\nEnter Option: ")
        if access == "1":
            search = input("\nEnter name of the new tenant: ")
            print(f"\n**Changes has been saved.**\n\nUnit: {unit}\nName: {search}\nRole: Admin, Resident\nDevices:\n-Thermostat: Warm-Me\n-Lights: Bright Ideas, Sunnee ({listat})\n-Locks: LockNess ({lostat})")
            access = input("\nType 1 to Exit\n\nEnter Option: ")
            if access == "1":
                import sys
                sys.exit()
            else:
                print("Invalid option, forcing to exit...")
                import sys
                sys.exit()
        if access == "2":
            listat = input("\nType 1 to turn off the Sunnee Lights\nType 2 to turn on the Sunnee lights\n\nEnter Option: ")
            if listat == "1":
                listat = ("Off")
                print(f"\n**Changes has been saved.**\n\nUnit: {unit}\nName: {search}\nRole: Admin, Resident\nDevices:\n-Thermostat: Warm-Me\n-Lights: Bright Ideas, Sunnee ({listat})\n-Locks: SkeletonKey ({lostat})")
                access = input("\nType 1 to Exit\n\nEnter Option: ")
                if access == "1":
                    import sys
                    sys.exit()
                else:
                    print("Invalid option, forcing to exit...")
                    import sys
                    sys.exit()
            elif listat == "2":
                listat = ("On")
                print(f"\n**Changes has been saved.**\n\nUnit: {unit}\nName: {search}\nRole: Admin, Resident\nDevices:\n-Thermostat: Warm-Me\n-Lights: Bright Ideas, Sunnee ({listat})\n-Locks: SkeletonKey ({lostat})")
                access = input("\nType 1 to Exit\n\nEnter Option: ")
                if access == "1":
                    import sys
                    sys.exit()
                else:
                    print("Invalid option, forcing to exit...")
                    import sys
                    sys.exit()
            else:
                print("Invalid Option, exiting...")
                import sys
                sys.exit()
        if access == "3":
            lostat = input("\nType 1 to lock the unit\nType 2 to unlock the unit\n\nEnter Option: ")
            if lostat == "1":
                lostat = ("Locked")
                print(f"\n**Changes has been saved.**\n\nUnit: {unit}\nName: {search}\nRole: Admin, Resident\nDevices:\n-Thermostat: Warm-Me\n-Lights: Bright Ideas, Sunnee ({listat})\n-Locks: SkeletonKey ({lostat})")
                access = input("\nType 1 to Exit\n\nEnter Option: ")
                if access == "1":
                    import sys
                    sys.exit()
                else:
                    print("Invalid option, forcing to exit...")
                    import sys
                    sys.exit()
            elif lostat == ("2"):
                lostat = ("Unlocked")
                print(f"\n**Changes has been saved.**\n\nUnit: {unit}\nName: {search}\nRole: Admin, Resident\nDevices:\n-Thermostat: Warm-Me\n-Lights: Bright Ideas, Sunnee ({listat})\n-Locks: SkeletonKey ({lostat})")
                access = input("\nType 1 to Exit\n\nEnter Option: ")
                if access == "1":
                    import sys
                    sys.exit()
                else:
                    print("Invalid option, forcing to exit...")
                    import sys
                    sys.exit()
            else:
                print("Invalid Option, forcing to exit...")
                import sys
                sys.exit()
        if access == "4":
            import sys
            sys.exit()

    elif search == "201":
        tname = ("Zakiyya Shabazz")
        listat = ("Off")
        lostat =("Locked")
        print(f"\nUnit: {search}\nName: {tname}\nRole: Admin, Resident\nDevices:\n-Thermostat: Warm-Me\n-Lights: Bright Ideas, Sunnee ({listat})\nLocks: LockNess ({lostat})")
        access = input("\nType 1 to Change Tenant\nType 2 to Control Sunnee Lights\nType 3 to lock/unlock the unit\nType 4 to exit\n\nEnter Option: ")
        if access == "1":
            tname = input("\nEnter name of the new tenant: ")
            print(f"\n**Changes has been saved.**\n\nUnit: {search}\nName: {tname}\nRole: Admin, Resident\nDevices:\n-Thermostat: Warm-Me\n-Lights: Bright Ideas, Sunnee ({listat})\n-Locks: LockNess ({lostat})")
            access = input("\nType 1 to Exit\n\nEnter Option: ")
            if access == "1":
                import sys
                sys.exit()
            else:
                print("Invalid option, forcing to exit...")
                import sys
                sys.exit()
        if access == "2":
            listat = input("\nType 1 to turn off the Sunnee Lights\nType 2 to turn on the Sunnee lights\n\nEnter Option: ")
            if listat == "1":
                listat = ("Off")
                print(f"\n**Changes has been saved.**\n\nUnit: {search}\nName: {tname}\nRole: Admin, Resident\nDevices:\n-Thermostat: Warm-Me\n-Lights: Bright Ideas, Sunnee ({listat})\n-Locks: SkeletonKey ({lostat})")
                access = input("\nType 1 to Exit\n\nEnter Option: ")
                if access == "1":
                    import sys
                    sys.exit()
                else:
                    print("Invalid option, forcing to exit...")
                    import sys
                    sys.exit()
            elif listat == "2":
                listat = ("On")
                print(f"\n**Changes has been saved.**\n\nUnit: {search}\nName: {tname}\nRole: Admin, Resident\nDevices:\n-Thermostat: Warm-Me\n-Lights: Bright Ideas, Sunnee ({listat})\n-Locks: SkeletonKey ({lostat})")
                access = input("\nType 1 to Exit\n\nEnter Option: ")
                if access == "1":
                    import sys
                    sys.exit()
                else:
                    print("Invalid option, forcing to exit...")
                    import sys
                    sys.exit()
            else:
                print("Invalid Option, exiting...")
                import sys
                sys.exit()
        if access == "3":
            lostat = input("\nType 1 to lock the unit\nType 2 to unlock the unit\n\nEnter Option: ")
            if lostat == "1":
                lostat = ("Locked")
                print(f"\n**Changes has been saved.**\n\nUnit: {search}\nName: {tname}\nRole: Admin, Resident\nDevices:\n-Thermostat: Warm-Me\n-Lights: Bright Ideas, Sunnee ({listat})\n-Locks: SkeletonKey ({lostat})")
                access = input("\nType 1 to Exit\n\nEnter Option: ")
                if access == "1":
                    import sys
                    sys.exit()
                else:
                    print("Invalid option, forcing to exit...")
                    import sys
                    sys.exit()
            elif lostat == ("2"):
                lostat = ("Unlocked")
                print(f"\n**Changes has been saved.**\n\nUnit: {search}\nName: {tname}\nRole: Admin, Resident\nDevices:\n-Thermostat: Warm-Me\n-Lights: Bright Ideas, Sunnee ({listat})\n-Locks: SkeletonKey ({lostat})")
                access = input("\nType 1 to Exit\n\nEnter Option: ")
                if access == "1":
                    import sys
                    sys.exit()
                else:
                    print("Invalid option, forcing to exit...")
                    import sys
                    sys.exit()
            else:
                print("Invalid Option, forcing to exit...")
                import sys
                sys.exit()
        if access == "4":
            import sys
            sys.exit()

    elif search == "Duane Velasquez":
        unit = ("202")
        lostat =("Locked")
        print(f"\nUnit: {unit}\nName: {search}\nRole: Resident\nDevices:\n-Thermostat: Warm-Me\n-Lights: Bright Ideas\n-Locks: SkeletonKey ({lostat})")
        access = input("\nType 1 to Change Tenant\nType 2 to lock/unlock the unit\nType 3 to exit\n\nEnter Option: ")
        if access == "1":
            search = input("\nEnter name of the new tenant: ")
            print(f"\n**Changes has been saved.**\n\nUnit: {unit}\nName: {search}\nRole: Resident\nDevices:\n-Thermostat: Warm-Me\n-Lights: Bright Ideas\n-Locks: SkeletonKey ({lostat})")
            access = input("\nType 1 to Exit\n\nEnter Option: ")
            if access == "1":
                import sys
                sys.exit()
            else:
                print("Invalid option, forcing to exit...")
                import sys
                sys.exit()
        if access == "2":
            lostat = input("\nType 1 to lock the unit\nType 2 to unlock the unit\n\nEnter Option: ")
            if lostat == "1":
                lostat = ("Locked")
                print(f"\n**Changes has been saved.**\n\nUnit: {unit}\nName: {search}\nRole: Resident\nDevices:\n-Thermostat: Warm-Me\n-Lights: Bright Ideas\n-Locks: SkeletonKey ({lostat})")
                access = input("\nType 1 to Exit\n\nEnter Option: ")
                if access == "1":
                    import sys
                    sys.exit()
                else:
                    print("Invalid option, forcing to exit...")
                    import sys
                    sys.exit()
            elif lostat == ("2"):
                lostat = ("Unlocked")
                print(f"\n**Changes has been saved.**\n\nUnit: {unit}\nName: {search}\nRole: Resident\nDevices:\n-Thermostat: Warm-Me\n-Lights: Bright Ideas\n-Locks: SkeletonKey ({lostat})")
                access = input("\nType 1 to Exit\n\nEnter Option: ")
                if access == "1":
                    import sys
                    sys.exit()
                else:
                    print("Invalid option, forcing to exit...")
                    import sys
                    sys.exit()
            else:
                print("Invalid Option, forcing to exit...")
                import sys
                sys.exit()
        if access == "3":
            import sys
            sys.exit()

    elif search == "202":
        tname = ("Duane Velasquez")
        lostat =("Locked")
        print(f"\nUnit: {search}\nName: {tname}\nRole: Resident\nDevices:\n-Thermostat: Warm-Me\n-Lights: Bright Ideas\n-Locks: SkeletonKey ({lostat})")
        access = input("\nType 1 to Change Tenant\nType 2 to lock/unlock the unit\nType 3 to exit\n\nEnter Option: ")
        if access == "1":
            tname = input("\nEnter name of the new tenant: ")
            print(f"\n**Changes has been saved.**\n\nUnit: {search}\nName: {tname}\nRole: Resident\nDevices:\n-Thermostat: Warm-Me\n-Lights: Bright Ideas\n-Locks: SkeletonKey ({lostat})")
            access = input("\nType 1 to Exit\n\nEnter Option: ")
            if access == "1":
                import sys
                sys.exit()
            else:
                print("Invalid option, forcing to exit...")
                import sys
                sys.exit()
        if access == "2":
            lostat = input("\nType 1 to lock the unit\nType 2 to unlock the unit\n\nEnter Option: ")
            if lostat == "1":
                lostat = ("Locked")
                print(f"\n**Changes has been saved.**\n\nUnit: {search}\nName: {tname}\nRole: Resident\nDevices:\n-Thermostat: Warm-Me\n-Lights: Bright Ideas\n-Locks: SkeletonKey ({lostat})")
                access = input("\nType 1 to Exit\n\nEnter Option: ")
                if access == "1":
                    import sys
                    sys.exit()
                else:
                    print("Invalid option, forcing to exit...")
                    import sys
                    sys.exit()
            elif lostat == ("2"):
                lostat = ("Unlocked")
                print(f"\n**Changes has been saved.**\n\nUnit: {search}\nName: {tname}\nRole: Resident\nDevices:\n-Thermostat: Warm-Me\n-Lights: Bright Ideas\n-Locks: SkeletonKey ({lostat})")
                access = input("\nType 1 to Exit\n\nEnter Option: ")
                if access == "1":
                    import sys
                    sys.exit()
                else:
                    print("Invalid option, forcing to exit...")
                    import sys
                    sys.exit()
            else:
                print("Invalid Option, forcing to exit...")
                import sys
                sys.exit()
        if access == "3":
            import sys
            sys.exit()

    elif search == "Dorothea Brooke":
        unit = ("301")
        listat = ("Off")
        lostat =("Locked")
        print(f"\nUnit: {unit}\nName: {tname} / Jian Ma\nRole: Resident\nDevices:\n-Thermostat: Warm-Me\n-Lights: Bright Ideas, Sunnee ({listat})\nLocks: LockNess ({lostat})")
        access = input("\nType 1 to Change Tenant\nType 2 to Control Sunnee Lights\nType 3 to lock/unlock the unit\nType 4 to exit\n\nEnter Option: ")
        if access == "1":
            search = input("\nEnter name of the new tenant: ")
            print(f"\n**Changes has been saved.**\n\nUnit: {unit}\nName: {search} / Jian Ma\nRole: Resident\nDevices:\n-Thermostat: Warm-Me\n-Lights: Bright Ideas, Sunnee ({listat})\n-Locks: LockNess ({lostat})")
            access = input("\nType 1 to Exit\n\nEnter Option: ")
            if access == "1":
                import sys
                sys.exit()
            else:
                print("Invalid option, forcing to exit...")
                import sys
                sys.exit()
        if access == "2":
            listat = input("\nType 1 to turn off the Sunnee Lights\nType 2 to turn on the Sunnee lights\n\nEnter Option: ")
            if listat == "1":
                listat = ("Off")
                print(f"\n**Changes has been saved.**\n\nUnit: {unit}\nName: {search} / Jian Ma\nRole: Resident\nDevices:\n-Thermostat: Warm-Me\n-Lights: Bright Ideas, Sunnee ({listat})\n-Locks: LockNess ({lostat})")
                access = input("\nType 1 to Exit\n\nEnter Option: ")
                if access == "1":
                    import sys
                    sys.exit()
                else:
                    print("Invalid option, forcing to exit...")
                    import sys
                    sys.exit()
            elif listat == "2":
                listat = ("On")
                print(f"\n**Changes has been saved.**\n\nUnit: {unit}\nName: {search} / Jian Ma\nRole: Resident\nDevices:\n-Thermostat: Warm-Me\n-Lights: Bright Ideas, Sunnee ({listat})\n-Locks: LockNess ({lostat})")
                access = input("\nType 1 to Exit\n\nEnter Option: ")
                if access == "1":
                    import sys
                    sys.exit()
                else:
                    print("Invalid option, forcing to exit...")
                    import sys
                    sys.exit()
            else:
                print("Invalid Option, exiting...")
                import sys
                sys.exit()
        if access == "3":
            lostat = input("\nType 1 to lock the unit\nType 2 to unlock the unit\n\nEnter Option: ")
            if lostat == "1":
                lostat = ("Locked")
                print(f"\n**Changes has been saved.**\n\nUnit: {unit}\nName: {search} / Jian Ma\nRole: Resident\nDevices:\n-Thermostat: Warm-Me\n-Lights: Bright Ideas, Sunnee ({listat})\n-Locks: LockNess ({lostat})")
                access = input("\nType 1 to Exit\n\nEnter Option: ")
                if access == "1":
                    import sys
                    sys.exit()
                else:
                    print("Invalid option, forcing to exit...")
                    import sys
                    sys.exit()
            elif lostat == ("2"):
                lostat = ("Unlocked")
                print(f"\n**Changes has been saved.**\n\nUnit: {unit}\nName: {search} / Jian Ma\nRole: Resident\nDevices:\n-Thermostat: Warm-Me\n-Lights: Bright Ideas, Sunnee ({listat})\n-Locks: LockNess ({lostat})")
                access = input("\nType 1 to Exit\n\nEnter Option: ")
                if access == "1":
                    import sys
                    sys.exit()
                else:
                    print("Invalid option, forcing to exit...")
                    import sys
                    sys.exit()
            else:
                print("Invalid Option, forcing to exit...")
                import sys
                sys.exit()
        if access == "4":
            import sys
            sys.exit()

    elif search == "301":
        tname = ("Dorothea Brooke / Jian Ma")
        listat = ("Off")
        lostat =("Locked")
        print(f"\nUnit: {search}\nName: {tname}\nRole: Resident\nDevices:\n-Thermostat: Warm-Me\n-Lights: Bright Ideas, Sunnee ({listat})\nLocks: LockNess ({lostat})")
        access = input("\nType 1 to Change Tenant\nType 2 to Control Sunnee Lights\nType 3 to lock/unlock the unit\nType 4 to exit\n\nEnter Option: ")
        if access == "1":
            tname = input("\nEnter name of the new tenant: ")
            print(f"\n**Changes has been saved.**\n\nUnit: {search}\nName: {tname}\nRole: Admin, Resident\nDevices:\n-Thermostat: Warm-Me\n-Lights: Bright Ideas, Sunnee ({listat})\n-Locks: LockNess ({lostat})")
            access = input("\nType 1 to Exit\n\nEnter Option: ")
            if access == "1":
                import sys
                sys.exit()
            else:
                print("Invalid option, forcing to exit...")
                import sys
                sys.exit()
        if access == "2":
            listat = input("\nType 1 to turn off the Sunnee Lights\nType 2 to turn on the Sunnee lights\n\nEnter Option: ")
            if listat == "1":
                listat = ("Off")
                print(f"\n**Changes has been saved.**\n\nUnit: {search}\nName: {tname}\nRole: Admin, Resident\nDevices:\n-Thermostat: Warm-Me\n-Lights: Bright Ideas, Sunnee ({listat})\n-Locks: LockNess ({lostat})")
                access = input("\nType 1 to Exit\n\nEnter Option: ")
                if access == "1":
                    import sys
                    sys.exit()
                else:
                    print("Invalid option, forcing to exit...")
                    import sys
                    sys.exit()
            elif listat == "2":
                listat = ("On")
                print(f"\n**Changes has been saved.**\n\nUnit: {search}\nName: {tname}\nRole: Admin, Resident\nDevices:\n-Thermostat: Warm-Me\n-Lights: Bright Ideas, Sunnee ({listat})\n-Locks: LockNess ({lostat})")
                access = input("\nType 1 to Exit\n\nEnter Option: ")
                if access == "1":
                    import sys
                    sys.exit()
                else:
                    print("Invalid option, forcing to exit...")
                    import sys
                    sys.exit()
            else:
                print("Invalid Option, exiting...")
                import sys
                sys.exit()
        if access == "3":
            lostat = input("\nType 1 to lock the unit\nType 2 to unlock the unit\n\nEnter Option: ")
            if lostat == "1":
                lostat = ("Locked")
                print(f"\n**Changes has been saved.**\n\nUnit: {search}\nName: {tname}\nRole: Admin, Resident\nDevices:\n-Thermostat: Warm-Me\n-Lights: Bright Ideas, Sunnee ({listat})\n-Locks: LockNess ({lostat})")
                access = input("\nType 1 to Exit\n\nEnter Option: ")
                if access == "1":
                    import sys
                    sys.exit()
                else:
                    print("Invalid option, forcing to exit...")
                    import sys
                    sys.exit()
            elif lostat == ("2"):
                lostat = ("Unlocked")
                print(f"\n**Changes has been saved.**\n\nUnit: {search}\nName: {tname}\nRole: Admin, Resident\nDevices:\n-Thermostat: Warm-Me\n-Lights: Bright Ideas, Sunnee ({listat})\n-Locks: LockNess ({lostat})")
                access = input("\nType 1 to Exit\n\nEnter Option: ")
                if access == "1":
                    import sys
                    sys.exit()
                else:
                    print("Invalid option, forcing to exit...")
                    import sys
                    sys.exit()
            else:
                print("Invalid Option, forcing to exit...")
                import sys
                sys.exit()


        if access == "4":
            import sys
            sys.exit()

    elif search == "Jian Ma":
        unit = ("301")
        listat = ("Off")
        lostat =("Locked")
        print(f"\nUnit: {unit}\nName: Dorothy Brooke / {search}\nRole: Resident\nDevices:\n-Thermostat: Warm-Me\n-Lights: Bright Ideas, Sunnee ({listat})\nLocks: LockNess ({lostat})")
        access = input("\nType 1 to Change Tenant\nType 2 to Control Sunnee Lights\nType 3 to lock/unlock the unit\nType 4 to exit\n\nEnter Option: ")
        if access == "1":
            search = input("\nEnter name of the new tenant: ")
            print(f"\n**Changes has been saved.**\n\nUnit: {unit}\nName: Dorothy Brooke / {search}\nRole: Resident\nDevices:\n-Thermostat: Warm-Me\n-Lights: Bright Ideas, Sunnee ({listat})\n-Locks: LockNess ({lostat})")
            access = input("\nType 1 to Exit\n\nEnter Option: ")
            if access == "1":
                import sys
                sys.exit()
            else:
                print("Invalid option, forcing to exit...")
                import sys
                sys.exit()
        if access == "2":
            listat = input("\nType 1 to turn off the Sunnee Lights\nType 2 to turn on the Sunnee lights\n\nEnter Option: ")
            if listat == "1":
                listat = ("Off")
                print(f"\n**Changes has been saved.**\n\nUnit: {unit}\nName: Dorothy Brooke / {search}\nRole: Resident\nDevices:\n-Thermostat: Warm-Me\n-Lights: Bright Ideas, Sunnee ({listat})\n-Locks: LockNess ({lostat})")
                access = input("\nType 1 to Exit\n\nEnter Option: ")
                if access == "1":
                    import sys
                    sys.exit()
                else:
                    print("Invalid option, forcing to exit...")
                    import sys
                    sys.exit()
            elif listat == "2":
                listat = ("On")
                print(f"\n**Changes has been saved.**\n\nUnit: {unit}\nName: Dorothy Brooke / {search}\nRole: Resident\nDevices:\n-Thermostat: Warm-Me\n-Lights: Bright Ideas, Sunnee ({listat})\n-Locks: LockNess ({lostat})")
                access = input("\nType 1 to Exit\n\nEnter Option: ")
                if access == "1":
                    import sys
                    sys.exit()
                else:
                    print("Invalid option, forcing to exit...")
                    import sys
                    sys.exit()
            else:
                print("Invalid Option, exiting...")
                import sys
                sys.exit()
        if access == "3":
            lostat = input("\nType 1 to lock the unit\nType 2 to unlock the unit\n\nEnter Option: ")
            if lostat == "1":
                lostat = ("Locked")
                print(f"\n**Changes has been saved.**\n\nUnit: {unit}\nName: Dorothy Brooke / {search}\nRole: Resident\nDevices:\n-Thermostat: Warm-Me\n-Lights: Bright Ideas, Sunnee ({listat})\n-Locks: LockNess ({lostat})")
                access = input("\nType 1 to Exit\n\nEnter Option: ")
                if access == "1":
                    import sys
                    sys.exit()
                else:
                    print("Invalid option, forcing to exit...")
                    import sys
                    sys.exit()
            elif lostat == ("2"):
                lostat = ("Unlocked")
                print(f"\n**Changes has been saved.**\n\nUnit: {unit}\nName: Dorothy Brooke / {search}\nRole: Resident\nDevices:\n-Thermostat: Warm-Me\n-Lights: Bright Ideas, Sunnee ({listat})\n-Locks: LockNess ({lostat})")
                access = input("\nType 1 to Exit\n\nEnter Option: ")
                if access == "1":
                    import sys
                    sys.exit()
                else:
                    print("Invalid option, forcing to exit...")
                    import sys
                    sys.exit()
            else:
                print("Invalid Option, forcing to exit...")
                import sys
                sys.exit()
        if access == "4":
            import sys
            sys.exit()
    else:
        print("\nInvalid First Name/Last Name/Unit Number.")
        import sys
        sys.exit()
