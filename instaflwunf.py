from seleniumbase import BaseCase
import time
import pyfiglet
import colorful as cf


ov3rctrl = pyfiglet.figlet_format("                       by ov3rctrl", font = "mini" ) 
banner = pyfiglet.figlet_format("\t \t \t \t \t \t  ---- \nINSTAFLWUNF", font = "starwars" )  
  
print(cf.bold_red(banner + ov3rctrl))
print(cf.bold_green("""
\t\t\tgithub.com/ov3rctrl
"""))    
time.sleep(1)
print(cf.bold_blue('######################################################################\n'))
time.sleep(1)

print(cf.bold_green("""
Choose.
"""))
time.sleep(1)
print(cf.bold_green("""
1. Follow(Suggestins)
2. Unfollow
"""))
choice = int(input("? : "))

print(cf.bold_green("""
\t \t \t
////////////////////////////###&&&&%#(////////////////////////////////
//////////////////////////#&&&######%&#///////////////////////////////
//////////////////////////&&#(((///((%@///////////////////////////////
//////////////////////////&&####((#%#(((//////////////////////////////
//////////////////////////(%#(((#(((/((///////////////////////////////
////////////////////////////%#(&&###(%(///////////////////////////////
((//////////////////////////@&&##%(#&/(///////////////////////////////
((((((////////((////////%&&@&##@@@&##((&&&(///////////////////////////
(((((((/////////////(&&&@&@&&######((#&&&&&&&(////////////////////////
(((((((((/////(((((&&&&&@&&&&&&((((&&&&&&&&&&&%(//////////////////////
(((((((((((((((((%&&&@&&@&&&&&&&&&&&&&&&&&&&&&&&%/////////////////////
(((((((((((((((%&&&&&&&@&&&&&&&&&&&&&&&&&&&@@&&&&%///((/(//((//////(//
((((((((((((((((%&&&&&@&&&&&&&&&&&&&&&&&&&&@&&&&&&(///////////////////
((((((((((((((((##(((#&@@&&&&&&&&&&&&&&&&&&@@&%(##(///////////////////
//////(////////(##(((#@@@&&&&&&&&&&&&&&&&&&@%((((##///////////////////
///////////////%#(((#%@@@&&&&&&&&&&&&&&&&&&%/###(##///////////////////
//////////////(#((##/&@@&@&&&&&&&&&&&&&&&&&(//######//////////////////
JUST DO IT DO IT DO IT DO IT DO IT DO IT DO IT DO IT DO IT DO IT DO IT 
JUST DO IT DO IT DO IT DO IT DO IT DO IT DO IT DO IT DO IT DO IT DO IT 
"""))



if (choice == 1):
    username = input("Username : ")
    passwd = input("Password : ")
    amount = int((input("How much flw/unf : ")))
    sleep_time = int((input('Sleep Time : ')))

    class flw(BaseCase):
        def test_basic(self):
            self.open("https://www.instagram.com/accounts/login")
            self.click('name=username')
            self.type(f"//input[@name='username']", username)
            self.click('name=password')
            self.type(f"//input[@name='password']", passwd)
            self.click('.sqdOP > .Igw0E')
            time.sleep(0.5)
            self.click('.s4Iyt')
            self.open("https://www.instagram.com/explore/people/suggested/")
            time.sleep(0.5)
            self.scroll_to_bottom()
            self.scroll_to_top()
            time.sleep(0.5)
            for i in range(amount):
                self.click_xpath("//button[contains(.,'Takip Et')]")
                self.press_down_arrow(selector="html", times=1)
                time.sleep(sleep_time)
            self.refresh_page()
            for i in range(amount):
                self.click_xpath("//button[contains(.,'Takip Et')]")
                self.press_down_arrow(selector="html", times=1)
                time.sleep(sleep_time)
            self.refresh_page()
            for i in range(amount):
                self.click_xpath("//button[contains(.,'Takip Et')]")
                self.press_down_arrow(selector="html", times=1)
                time.sleep(sleep_time)

if (choice == 2):
    username = input("Username : ")
    passwd = input("Password : ")
    amount = int((input("How much flw/unf : ")))
    sleep_time = int((input('Sleep Time : ')))

    class unf(BaseCase):
        def test_basic(self):
            self.open("https://www.instagram.com/accounts/login")
            self.click('name=username')
            self.type(f"//input[@name='username']", username)
            self.click('name=password')
            self.type(f"//input[@name='password']", passwd)
            self.click('.sqdOP > .Igw0E')
            time.sleep(1)
            self.click('.s4Iyt')
            self.open("https://www.instagram.com/" + username)
            time.sleep(1)
            self.click_xpath("//div[@id='react-root']/section/main/div/header/section/ul/li[3]/a")
            time.sleep(1)
            self.click("li:nth-child(1) > .Igw0E")
            time.sleep(1)
            for i in range(amount):
                self.click_xpath("//button[contains(.,'Takiptesin')]")
                self.click_xpath("//button[contains(.,'Takibi Bırak')]")
                self.press_down_arrow(selector="html", times=15)
                self.scroll_to("//button[contains(.,'Takiptesin')]")
                time.sleep(sleep_time)
else:
    time.sleep(1)
    print("\nSomething Isn't Right. Try Again.\n")
