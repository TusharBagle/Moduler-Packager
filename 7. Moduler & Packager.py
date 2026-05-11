print("=" * 70)
print("\t\tWelcome to Multi-Utility Toolkit")
print("=" * 70)


from datetime import datetime
import time
import math
import random
import uuid
import string



class Datetime_and_Time_Operation :


    def Display_Current_date_and_time (self) :

        Current_date_and_time = datetime.now().strftime('%d-%m-%y %H:%M:%S')
        print('\n\n ' , Current_date_and_time)


    def Calculate_difference_between_two_dates_time (self) :

        First_Date = input("\n\n\t\tEnter the First Date : ")
        First_Date_Calculation = datetime.strptime(First_Date , '%d-%m-%y')

        Second_Date = input("\n\t\tEnter the Second Date : ")
        Second_Date_Calculation = datetime.strptime(Second_Date , '%d-%m-%y')

        Difference_between_two_dates = ( Second_Date_Calculation - First_Date_Calculation ).days
        print(f"\n\n The difference between {Second_Date} and {First_Date} is : {Difference_between_two_dates}")


    def Format_date_into_custom_format (self) :

        pass


    def Stopwatch (self) :

        Stopwatch_Seconds = int(input("\n\n\t\tEnter the seconds to Stopwatch : "))

        print()
        for i in range (1 , Stopwatch_Seconds + 1) :
            time.sleep(i)
            print('' , i)
        print('\n Time Up !...')


    def Countdown (self) :

        Countdown = int(input("\n\n\t\tEnter the seconds to Countdown : "))

        print()
        for i in range ( Countdown , 0 , -1 ) :
            time.sleep(i)
            print('' , i)
        print('\n Time Up !...')



    def menu_Datetime_and_Time_Operation (self) :

        while True :

            try :

                menu = int(input("""\n\n\tDatetime and Time Operations :   \n
                1. Display Current date and time
                2. Calculate difference between two dates/time 
                3. Format date into custom format 
                4. Stopwatch
                5. Countdown 
                6. Back to Main menu  \n
                Enter your choice : """))

                if ( menu == 1 ) :
                    self.Display_Current_date_and_time()
                    print("\n\n" , "*" * 100)
                elif ( menu == 2 ) :
                    self.Calculate_difference_between_two_dates_time()
                    print("\n\n" , "*" * 100)
                elif ( menu == 3 ) :
                    self.Format_date_into_custom_format()
                    print("\n\n" , "*" * 100)
                elif ( menu == 4 ) :
                    self.Stopwatch()
                    print("\n\n" , "*" * 100)
                elif ( menu == 5 ) :
                    self.Countdown()
                    print("\n\n" , "*" * 100)
                elif ( menu == 6 ) :
                    break
                else :
                    print("\n\n Please enter the valid input !...")

            except Exception :
                print("\n\n Invalid input \n Please enter the valid input !...")




class Mathematical_Operation (Datetime_and_Time_Operation) :


    def Calculate_Factorial (self) :

        Factorial = int(input("\n\n\t\tEnter the number to Calculate it's Factorial : "))
        Calculate_Factorial = math.factorial(Factorial)
        print(f'\n\n The Factorial of {Factorial}! : ' , Calculate_Factorial)


    def Solve_Compound_Interest (self) :

        Principle_Amount = int(input("\n\n\t\tEnter the Principle Amount : "))
        Rate = int(input("\n\t\tEnter the rate of Interest (in %) : "))
        Time = int(input("\n\t\tEnter the Duration time (in year) : "))

        Compound_Interest = Principle_Amount * ( 1 + Rate / 100 ) ** Time
        print(f"\n\n The Compound Interest : {Compound_Interest}")



    def Degree_to_Sin (self) :
        Sin = int(input("\n\n\t\t\tEnter the Degree to Convert it into Sin's Value : "))
        Convert = math.sin(Sin)
        print('\n\n Sin Value :' , Convert)


    def Degree_to_Cos (self) :
        Cos = int(input("\n\n\t\t\tEnter the Degree to Convert it into Cos's Value : "))
        Convert = math.cos(Cos)
        print('\n\n Cos Value :' , Convert)


    def Degree_to_Tan (self) :
        Tan = int(input("\n\n\t\t\tEnter the Degree to Convert it into Tan's Value : "))
        Convert = math.tan(Tan)
        print('\n\n Tan Value :' , Convert)


    def Degree_to_Radian (self) :
        Radian = int(input("\n\n\t\t\tEnter the Degree to Convert it into Radian's Value : "))
        Convert = math.radians(Radian)
        print('\n\n Degree Value :' , Convert)


    def Radian_to_Degree (self) :
        Degree = int(input("\n\n\t\t\tEnter the Radian to Convert it into Degree's Value : "))
        Convert = math.degrees(Degree)
        print('\n\n Radian Value :' , Convert)



    def menu_Trigonometric_Calculation (self) :

        while True :

            try :

                menu = int(input("""\n\n\t\tMathematical Operations :   \n
                        1. Degree to Sin
                        2. Degree to Cos
                        3. Degree to Tan
                        4. Degree to Radian
                        5. Radian to Degree   
                        6. Exit    \n
                        Enter the your choice : """))

                if ( menu == 1 ) :
                    self.Degree_to_Sin()
                    print("\n\n" , "*" * 100)
                elif ( menu == 2 ) :
                    self.Degree_to_Cos()
                    print("\n\n" , "*" * 100)
                elif ( menu == 3 ) :
                    self.Degree_to_Tan()
                    print("\n\n" , "*" * 100)
                elif ( menu == 4 ) :
                    self.Degree_to_Radian()
                    print("\n\n" , "*" * 100)
                elif ( menu == 5 ) :
                    self.Radian_to_Degree()
                    print("\n\n" , "*" * 100)
                elif ( menu == 6 ) :
                    break
                else :
                    print("\n\n Please enter the valid input !...")

            except Exception :
                print("\n\n Invalid input \n Please enter the valid input !...")



    def Circle_Angle (self) :

        Circle_Angle = int(input("\n\n\t\t\tEnter the Radius to calculate the Area of Circle : "))
        Circle_Angle_Calculation = math.pi * Circle_Angle * Circle_Angle
        print('\n\n Area of Circle :' , Circle_Angle_Calculation)


    def Rectangle_Angle (self) :

        Rectangle_Angle_Length = int(input("\n\n\t\t\tEnter the Length to calculate the Area of Rectangle : "))
        Rectangle_Angle_Breadth = int(input("\n\t\t\tEnter the Breadth to calculate the Area of Rectangle : "))
        Rectangle_Angle_Calculation = Rectangle_Angle_Length * Rectangle_Angle_Breadth
        print('\n\n Area of Rectangle :' , Rectangle_Angle_Calculation)


    def Square_Angle (self) :

        Square_Angle_Side = int(input("\n\n\t\t\tEnter the Side to calculate the Area of Square : "))
        Square_Angle_Calculation = Square_Angle_Side * Square_Angle_Side
        print('\n\n Area of Square :' , Square_Angle_Calculation)


    def Triangle_Angle (self) :

        Triangle_Angle_Base = int(input("\n\n\t\t\tEnter the Base to calculate the Area of Triangle : "))
        Triangle_Angle_Height = int(input("\n\t\t\tEnter the Height to calculate the Area of Triangle : "))
        Triangle_Angle_Calculation = 0.5 * Triangle_Angle_Base * Triangle_Angle_Height
        print('\n\n Area of Triangle :' , Triangle_Angle_Calculation)



    def menu_Area_of_Geometric_Shapes (self) :

        while True :

            try :

                menu = int(input("""\n\n\t\tMathematical Operations :   \n
                        1. Circle Angle
                        2. Rectangle Angle
                        3. Square Angle
                        4. Triangle Angle 
                        5. Exit    \n
                        Enter the your choice : """))

                if ( menu == 1 ) :
                    self.Circle_Angle()
                    print("\n\n" , "*" * 100)
                elif ( menu == 2 ) :
                    self.Rectangle_Angle()
                    print("\n\n" , "*" * 100)
                elif ( menu == 3 ) :
                    self.Square_Angle()
                    print("\n\n" , "*" * 100)
                elif ( menu == 4 ) :
                    self.Triangle_Angle()
                    print("\n\n" , "*" * 100)
                elif ( menu == 5 ) :
                    break
                else :
                    print("\n\n Please enter the valid input !...")

            except Exception :
                print("\n\n Invalid input \n Please enter the valid input !...")




    def menu_Mathematical_Operation (self) :

        while True :

            try :

                menu = int(input("""\n\n\tMathematical Operations :   \n
                1. Calculate factorial
                2. Solve Compound Interest 
                3. Trigonometric Calculation
                4. Area of Geometric Shapes 
                5. Back to Main menu  \n
                Enter your choice : """))

                if ( menu == 1 ) :
                    self.Calculate_Factorial()
                    print("\n\n" , "*" * 100)
                elif ( menu == 2 ) :
                    self.Solve_Compound_Interest()
                    print("\n\n" , "*" * 100)
                elif ( menu == 3 ) :
                    self.menu_Trigonometric_Calculation()
                    print("\n\n" , "*" * 100)
                elif ( menu == 4 ) :
                    self.menu_Area_of_Geometric_Shapes()
                    print("\n\n" , "*" * 100)
                elif ( menu == 5 ) :
                    break
                else :
                    print("\n\n Please enter the valid input !...")

            except Exception :
                print("\n\n Invalid input \n Please enter the valid input !...")




class Random_Data_Generation (Mathematical_Operation) :


    def Generate_Random_number (self) :

        Generate_Random_number = random.randint(1 , 1000) 
        print('\n\n Random number :' , Generate_Random_number)


    def Generate_Random_List (self) :

        Generate_Random_List = [ random.randint(1 , 1000) for i in range (5)]
        print('\n\n Random List :' , Generate_Random_List)


    def Create_Random_Password (self) :

        Create_Random_Password = string.ascii_letters + string.ascii_lowercase + string.ascii_uppercase + string.digits

        a =  ''.join(random.choice(Create_Random_Password) for i in range (8))
        print('\n\n Random Password :' , a)


    def Generate_Random_OTP (self) :

        Generate_Random_OTP = random.randint(1000 , 9999) 
        print('\n\n Random OTP :' , Generate_Random_OTP)


    def menu_Random_Data_Generation (self) :

        while True :

            try :

                menu = int(input("""\n\n\tMathematical Operations :   \n
                1. Generate Random number
                2. Generate Random List  
                3. Creat Randomn Password
                4. Generate Random OTP   
                5. Back to Main menu  \n
                Enter your choice : """))

                if ( menu == 1 ) :
                    self.Generate_Random_number()
                    print("\n\n" , "*" * 100)
                elif ( menu == 2 ) :
                    self.Generate_Random_List()
                    print("\n\n" , "*" * 100)
                elif ( menu == 3 ) :
                    self.Create_Random_Password()
                    print("\n\n" , "*" * 100)
                elif ( menu == 4 ) :
                    self.Generate_Random_OTP()
                    print("\n\n" , "*" * 100)
                elif ( menu == 5 ) :
                    break
                else :
                    print("\n\n Please enter the valid input !...")

            except Exception :
                print("\n\n Invalid input \n Please enter the valid input !...")




class Generate_Unique_Identifier_UUID (Random_Data_Generation) :


    def Generate_Unique_Identifier_UUID (self) :

        a = uuid.uuid4()
        print('\n\n ' , a)




class File_Operation_Custom_Module (Generate_Unique_Identifier_UUID) :


    def Create_a_new_file (self) :

        Create_a_new_file = input("\n\n\t\tEnter the File name to Create it : ")
        print('\n\n The file is successfully Created !...')


    def Write_to_a_file (self) :

        Create_a_new_file = input("\n\n\t\tEnter the File name : ")
        Data = input("\n\t\tEnter Data to write : ")

        with open (Create_a_new_file , 'w') as b :
            b.write(Data)
            print('\n\n The data is successfully Written !...')


    def Read_to_a_file (self) :

        Read_a_new_file = input("\n\n\t\tEnter the File name : ")

        with open (Read_a_new_file , 'r') as c :
            print('\n\n The File Content : ')
            e = c.read()
            print('\n ' , e)


    def Append_to_a_file (self) :

        Append_a_new_file = input("\n\n\t\tEnter the File name : ")
        Data = input("\n\t\tEnter Data to Append : ")

        with open (Append_a_new_file , 'a') as d :
            d.write(Data)
            print('\n\n The data is successfully Written !...')



    def menu_File_Operation_Custom_Module (self) :

        while True :

            try :

                menu = int(input("""\n\n\tMathematical Operations :   \n
                1. Create a new file
                2. Write to a file  
                3. Read to a file 
                4. Append to a file   
                5. Back to Main menu  \n
                Enter your choice : """))

                if ( menu == 1 ) :
                    self.Create_a_new_file()
                    print("\n\n" , "*" * 100)
                elif ( menu == 2 ) :
                    self.Write_to_a_file()
                    print("\n\n" , "*" * 100)
                elif ( menu == 3 ) :
                    self.Read_to_a_file()
                    print("\n\n" , "*" * 100)
                elif ( menu == 4 ) :
                    self.Append_to_a_file()
                    print("\n\n" , "*" * 100)
                elif ( menu == 5 ) :
                    break
                else :
                    print("\n\n Please enter the valid input !...")

            except Exception :
                print("\n\n Invalid input \n Please enter the valid input !...")




class Explore_Module_Attributes_dir (File_Operation_Custom_Module) :


    def Explore_Module_Attributes_dir (self) :

        y = dir(math)
        print('\n\n ' , y)




class Call (Explore_Module_Attributes_dir) :

    def main_menu (self) :

        while True :

            try :

                menu = int(input("""\n\n Choose an option :   \n
        1. Datetime and Time Operation
        2. Mathematical Operation
        3. Random Data Generation
        4. Generate Unique Identifier (UUID)
        5. File Operation (Custom Module)
        6. Explore Module Attributes (dir())
        7. Exit  \n
        Enter your choice : """))

                if ( menu == 1 ) :
                    self.menu_Datetime_and_Time_Operation()
                    print("\n\n" , "*" * 100)
                elif ( menu == 2 ) :
                    self.menu_Mathematical_Operation()
                    print("\n\n" , "*" * 100)
                elif ( menu == 3 ) :
                    self.menu_Random_Data_Generation()
                    print("\n\n" , "*" * 100)
                elif ( menu == 4 ) :
                    self.Generate_Unique_Identifier_UUID()
                    print("\n\n" , "*" * 100)
                elif ( menu == 5 ) :
                    self.menu_File_Operation_Custom_Module()
                    print("\n\n" , "*" * 100)
                elif ( menu == 6 ) :
                    self.Explore_Module_Attributes_dir()
                    print("\n\n" , "*" * 100)
                elif ( menu == 7 ) :
                    break
                else :
                    print("\n\n Please enter the valid input !...")

            except Exception :
                print("\n\n Invalid input \n Please enter the valid input !...")


z = Call()
z.main_menu()