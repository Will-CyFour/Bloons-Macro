import pyautogui as a
import time

def play():
   a.click(1794, 974)
   a.click(1794, 974)

def pause():
   a.keyDown("esc")
   a.keyUp("esc")

def freeplay():
   a.click(950, 900)  # next
   time.sleep(2)
   a.click(1222, 888)  # freeplay
   time.sleep(1)
   a.click(1222, 888)  # ok (anywhere)
   time.sleep(1)

def restart():
   pause()
   a.click(1075, 843)  # restart
   time.sleep(0.5)
   a.click(1123, 725)  # restart
   time.sleep(0.5)

def defeat_restart():
   a.click(950, 800) #center restart
   time.sleep(0.5)
   a.click(1123, 725)  # restart
   time.sleep(0.5)

def menu_up(ignore_state:bool = False):
   if Tower.menu_pos != "up" or ignore_state:
       menu_move(1)
   Tower.menu_pos = "up"


def menu_down(ignore_state:bool = False):
   if Tower.menu_pos != "down" or ignore_state:
       menu_move(-1)
   Tower.menu_pos = "down"


def menu_move(direction:int):
   a.PAUSE = 0
   a.moveTo(1824, 613)
   for i in range(13):
       a.scroll(direction)
   a.PAUSE = 0.1
   time.sleep(0.5)


class Tower:
   """Class for all towers, adding as needed"""

   menu_pos = "up"

   farms = False

   def __init__(self, tower_type: str, x:int, y:int, ):
       self.x = x
       self.y = y
       self.tower_type = tower_type
       self.right_side_menu = x < 835
       self.state = [0, 0, 0] #current upgrades

       #get tower number
       towers = ['hero', 'dart', 'boomerang','bomb','tack','ice','glue','sniper', 'sub', 'boat',
                 'ace', 'heli', 'mortar','dartling','wizard','super','ninja','alch','druid']
       if Tower.farms:
           towers.extend(['farm'])
       towers.extend(['spactory', 'village','engi'])

       self.tower_number = towers.index(tower_type) #0 indexed btw
       self.targeting = "first"
       ###
       self.place()
       time.sleep(0.5)

   def select(self):
       time.sleep(0.8)
       a.click(self.x, self.y)

   def place(self):
       tower_number = self.tower_number
       #even -> tower on left (1700)
       #odd -> tower on right (1800)
       if tower_number % 2 == 0:
           icon_x = 1700
       else:
           icon_x = 1800
       if tower_number >= 12:#11 is heli, the last tower on up
           menu_down()
           if not Tower.farms:
               tower_number -= 10
           else:
               tower_number -= 12
       else:
           menu_up()
       #                       make even
       icon_y = 230 + 130 * (tower_number // 2)

       a.click(icon_x,icon_y)
       self.select() #place
       time.sleep(0.1)

   def upgrade(self, top:int = 0, middle:int = 0, bottom:int = 0):
       self.select() #select
       upgrades = top, middle, bottom
       if self.right_side_menu:
           upgrade_x = 1500
       else:
           upgrade_x = 350

       for i in range(3):
           while self.state[i] < upgrades[i]:
               upgrade_y = 500 + i * 150 #500,650,800
               a.click(upgrade_x, upgrade_y)
               self.state[i] += 1
       time.sleep(0.2)
       self.select()  #de-select

   def sell(self):
       self.select()
       if self.right_side_menu: #right side menu
           a.click(1550,900) #SELL
       else:
           a.click(350,900) #SELL

####


if __name__ == '__main__':
   pass









