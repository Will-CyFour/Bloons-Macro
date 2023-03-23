import pyautogui as a
import time
import tower as t


def pos(n):
    for i in range(n):
        time.sleep(1)
        print(a.position())


def infernal_deflation():
    time.sleep(5)  # (loading)
    a.click(900, 500)  # OK
    time.sleep(2)

    hero_switch = False

    if hero_switch:
        a.click(1711, 228)  # select hero
        a.click(121, 655)  # place Gwen (IDK if other heroes fit here)

    # menu_down() #no need with new method

    a.click(1710, 627)  # Ninja
    a.click(825, 382)  # Ninja1 place
    a.click(825, 382)  # Ninja1 select
    upgrade_old(1, 4)
    upgrade_old(3, 2)

    a.click(1710, 627)  # Ninja
    a.click(831, 695)  # Ninja2 place
    a.click(831, 695)  # Ninja2 select
    upgrade_old(1, 4)
    upgrade_old(3, 2)

    a.click(1820, 627)  # Alch
    a.click(805, 304)  # Alch1 place
    a.click(805, 304)  # Alch1 select
    upgrade_old(1, 4)
    upgrade_old(2, 2)

    a.click(1820, 627)  # Alch
    a.click(798, 750)  # Alch2 place
    a.click(798, 750)  # Alch2 select
    upgrade_old(1, 4)
    upgrade_old(2, 2)

    a.click(925, 482)  # click middle of map

    play()
    for i in range(26):  # can be 26 i think
        time.sleep(13)
        a.click(925, 482)  # click middle of map
        time.sleep(1)
        a.click(925, 482)  # click middle of map

        time.sleep(1)


def end_screen():
    a.click(950, 900)  # next
    time.sleep(2)
    a.click(1222, 888)  # freeplay
    time.sleep(1)
    a.click(1222, 888)  # ok (anywhere)
    time.sleep(2)
    a.keyDown("esc")
    a.keyUp("esc")
    a.click(1075, 843)  # restart
    time.sleep(0.5)
    a.click(1123, 725)  # restart
    time.sleep(1)


def grind_infernal():
    warlock_count = 0
    while True:
        infernal_deflation()

        end_screen()

        warlock_count += 1
        money = str(warlock_count * 66)
        print(warlock_count)
        print("$" + money + " made")


def menu_up():
    a.moveTo(1824, 613)
    for i in range(13):
        a.scroll(1)


def menu_down():
    a.moveTo(1824, 613)
    for i in range(13):
        a.scroll(-1)


def use_ability(num):
    a.click(100 + 100 * num, 1020)


def use_ability_target(num, x, y):
    use_ability(num)
    time.sleep(0.5)
    a.click(x, y)


def use_chinook(num, x, y, right):
    distance = 100
    use_ability(num)
    time.sleep(0.5)
    a.click(x, y)
    time.sleep(0.5)
    if right:
        a.move(distance, 0, 0.25)
    else:
        a.move(-1 * distance, 0, 0.25)
    time.sleep(0.5)
    a.click()
    time.sleep(0.5)


def play():
    a.click(1794, 974)
    a.click(1794, 974)


def upgrade_old(path, tier):  # left side gui
    for i in range(tier):
        if path == 1:
            y = 500
        elif path == 2:
            y = 600
        elif path == 3:
            y = 775
        else:
            y = 0
        a.click(1500, y)


def upgrade_left(path, tier):  # left side gui
    for i in range(tier):
        if path == 1:
            y = 500
        elif path == 2:
            y = 600
        elif path == 3:
            y = 775
        else:
            y = 0
        a.click(350, y)


def upgrade(p1, p2, p3):
    upgrade_old(1, p1)
    upgrade_old(2, p2)
    upgrade_old(3, p3)


def lategame():
    # Blood Sacrifice lasts 20 seconds (1 min)
    # 12|9.6: Ultra (10 seconds on tier 5), therefore 100+% uptime with energizer`
    # 15|12: arm clock home/call (home lasts 20/3 = 6.6 seconds)
    # 20|16: ball g-sabotage (10 seconds)
    t = -5
    while True:
        time.sleep(5)
        t += 5

        use_ability(1)  # ?
        use_ability(3)  # ?
        use_ability(5)  # ?
        use_ability(6)  # ?
        use_ability(7)  # ?
        use_ability(9)  # ?
        use_ability(10)  # ?

        if t % 10 == 0:
            pass  # techbot
            # use_ability_target(4, 1027, 417)  # ultra
            # a.click(1027, 700)  # deselect
        if t % 20 == 0:
            time.sleep(1)
            a.click(1824, 378)  # select super
            a.click(90, 850)  # place sacrifice
            time.sleep(1)
            a.click(90, 850)  # select sacrifice
            time.sleep(1)
            upgrade(2, 0, 2)  # make sure
            use_ability_target(2, 90, 850)  # blood sacrifice


def off_the_coast_easy():
    t.Tower.farms = True

    sauda = t.Tower('hero', 291, 509)
    dart = t.Tower('dart', 103, 530)
    sniper = t.Tower('sniper', 777, 680)
    t.play()
    time.sleep(2 * 60 + 34)
    sniper.upgrade(2, 0, 2)
    time.sleep(32)
    sniper.upgrade(2, 0, 3)
    time.sleep(1 * 60 + 12)
    sniper.upgrade(2, 0, 4)
    time.sleep(58)


def another_brick_easy():
    menu_up()
    a.click(1711, 228)  # select hero
    a.click(577, 340)  # place hero (Sauda)
    play()
    menu_down()
    time.sleep(3 * 60)  # wait until about round 27
    a.click(1835, 486)  # Alch
    a.click(677, 230)
    a.click(677, 230)
    upgrade(4, 0, 1)
    a.click(1710, 486)  # Ninja
    a.click(677, 340)  # Ninja1 place
    time.sleep(1 * 60)
    a.click(677, 340)  # Ninja1 select
    upgrade(4, 0, 1)
    time.sleep(1 * 60 + 5)

    end_screen()


def cubisim_deflation():
    t.Tower.farms = False
    churchill = t.Tower('hero', 583, 339)

    boats = t.Tower('boat', 1118, 299), t.Tower('boat', 1206, 296)
    for b in boats:
        b.upgrade(3, 2, 0)
    darts = t.Tower('dart', 690, 348), t.Tower('dart', x=771, y=346)
    for d in darts:
        d.upgrade(0, 2, 3)
    darts[0].upgrade(0, 2, 4)
    boomer = t.Tower('boomerang', x=1590, y=508)
    boomer.upgrade(4, 0, 2)
    t.play()
    timer = 5 * 60 + 15 + 10
    while timer > 0:
        time.sleep(2)
        timer -= 2
        a.click(900, 450)
        time.sleep(3)
        timer -= 3


if __name__ == '__main__':
    a.hotkey('alt', 'tab')
    # t.menu_up(True)  # start each loop at the top
    t.restart()
    grind_infernal()

    """
        a.hotkey('alt', 'tab')  # to switch windows
    time.sleep(1)
    key = 'esc'
    a.keyDown(key)
    time.sleep(0.5)
    a.keyUp(key)
    Coords:
    Victory Screen:
        Next Button: 950, 900
        Home: 700, 850
    Main Menu:
        Play: 800,900
 
    Map Select:
        Advanced: 1080, 950
        Expert: 1350, 950
            Map 4: 500, 600
 
    Difficulty Select:
        Easy: 600, 460
            Deflation: 1300, 400
 
    OK: 900,500 (anywhere is fine i think
 
    Towers:
        Dart(1828, 228)
        Bomb(1825, 356)
        Ice(1826, 498)
        Sniper(1824, 613)
        Boat(1818, 755)
        Heli(1819, 883)
 
        Point(x=1711, y=204)
        Mortar:(1709, 357)
        Point(x=1712, y=478)
        Point(x=1710, y=627)
        Point(x=1713, y=754)
        Point(x=1713, y=887)
 
    """

