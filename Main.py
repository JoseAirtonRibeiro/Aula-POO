from Class Contact import *
from Class Schedule import *

schedule_obj = Schedule()
schedule_obj.save_contact()
schedule_obj.list_cont_all()





...
white = '#ffffff'
dark_bl = '#00357b'
bl = '#0F0F10'
#_______________________
Menu_1 = tk()

Menu_1.resizable(False, False)
Menu_1.title('Schedule')


frame_fav = Frame(Menu_1)  #Frame 1 AKA f1
frame_main = Frame(Menu_1) #Frame 2 AKA f2


lb_f1 = Frame(Menu)
...