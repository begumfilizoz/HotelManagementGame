
import math
from graphics import Canvas
import random
import time
from playsound import playsound
button_width = 200
button_height = 60
CANVAS_WIDTH = 1500
CANVAS_HEIGHT = 800
MENU_HEIGHT = 600
MENU_WIDTH = 300
BLOCK_WIDTH = 300
BLOCK_HEIGHT = 150
initial_money = 15000
room_price = 5000
suite_price = 10000
star = 0
wait = 20
def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    canvas.set_canvas_title("Hotel Management")
    playsound('hotelmusic.mp3', block=False)
    stars = star
    restaurant = 0
    pool = 0
    suite_num = 0
    cleaner = 0
    customers = 0
    money = initial_money
    second_y = 600
    third_level = 600
    second_floors = 0
    third_y = 600 - BLOCK_HEIGHT
    y_level = 600 - BLOCK_HEIGHT
    added_rooms = 0
    title, play_button, play_text, how_to_button, how_to_text = starting_screen(canvas)
    canvas.wait_for_click()
    if 500 <= canvas.get_mouse_x() <= 500 + button_width and 500 <= canvas.get_mouse_y() <= 500 + button_height:
        canvas.delete(title)
        canvas.delete(play_button)
        canvas.delete(play_text)
        canvas.delete(how_to_button)
        canvas.delete(how_to_text)
        canvas.set_canvas_background_color('white')
    if 800 <= canvas.get_mouse_x() <= 800 + button_width and 500 <= canvas.get_mouse_y() <= 500 + button_height:
        how_to(canvas, title, play_button, play_text, how_to_button, how_to_text)

    canvas.create_image_with_size(0, 0, CANVAS_WIDTH, CANVAS_HEIGHT, 'beachbg.jpg')
    create_menu(canvas)
    canvas.create_image_with_size(100, 600, BLOCK_WIDTH, BLOCK_HEIGHT, 'reception.png')
    create_money(canvas)
    add_room_button(canvas)
    cleaner_button(canvas)
    restaurant_button(canvas)
    pool_button(canvas)
    suite_button(canvas)
    money_you_have = canvas.create_text(1280, 80, str(initial_money) + '$')
    canvas.set_font(money_you_have, 'Rockwell', 30)
    canvas.set_fill_color(money_you_have, 'dim gray')
    while True:
        messages(canvas, customers, stars)
        canvas.wait_for_click()
        if money >= 15000:
            suite_num, money, third_y, customers = add_suites(canvas, restaurant, suite_num, money, third_y, customers)
            pool, money = add_pool(canvas, suite_num, pool, money)
        if money >= 40000:
            restaurant, money = add_rest(canvas, second_floors, restaurant, money)
        if money >= 1000:
            cleaner, money = hire_a_cleaner(canvas, cleaner, money, stars)
        if money >= 5000:
            y_level, added_rooms, money, customers = add_room(canvas, y_level, added_rooms, money, second_floors,
                                                              customers, cleaner)
            second_y, second_floors, money, customers = add_room_new_x(canvas, second_y, second_floors, added_rooms,
                                                                       money, customers, cleaner)
        if added_rooms == 3:
            stars = star + 1
            money = money + 10000
            money = money - 1500
        if second_floors == 2:
            stars = stars + 1
            money = money + 10000
            money = money - 3000
        if second_floors == 5 and restaurant == 1:
            stars = stars + 1
            money = money + 10000
            money = money - 4500
            second_floors = second_floors + 1
        if suite_num == 3 and pool == 0:
            stars = stars + 1
            money = money + 10000
            money = money - 6000
            suite_num = suite_num + 1
        if pool == 1:
            stars = 5
            money = money + 10000
            money = money - 7500
            pool = pool + 1
            suite_num = suite_num - 1
            won = canvas.create_text(CANVAS_WIDTH / 2, CANVAS_HEIGHT / 2, 'You won!')
            canvas.set_font(won, 'Rockwell', 50)
            canvas.set_fill_color(won, 'maroon')
        canvas.set_text(money_you_have, str(money) + '$')
        if money < 5000:
            failed = canvas.create_text(CANVAS_WIDTH/2, CANVAS_HEIGHT/2, 'You failed!')
            canvas.set_font(failed, 'Rockwell', 50)
            canvas.set_fill_color(failed, 'white')
        canvas.update()
    canvas.update()
    canvas.mainloop()

def starting_screen(canvas):
    canvas.set_canvas_background_color('RosyBrown1')
    title = canvas.create_text(CANVAS_WIDTH / 2, CANVAS_HEIGHT / 2, 'Hotel Management')
    canvas.set_font(title, 'Didot', 72)
    canvas.set_fill_color(title, 'gray')
    play_button = canvas.create_rectangle(500, 500, 500 + button_width, 500 + button_height)
    canvas.set_fill_color(play_button, 'LightSkyBlue2')
    how_to_button = canvas.create_rectangle(800, 500, 800 + button_width, 500 + button_height)
    canvas.set_fill_color(how_to_button, 'LightSkyBlue2')
    play_text = canvas.create_text(600, 530, 'Play!')
    canvas.set_font(play_text, 'Didot', 40)
    canvas.set_fill_color(play_text, 'blue4')
    how_to_text = canvas.create_text(905, 530, 'How to Play?')
    canvas.set_font(how_to_text, 'Didot', 30)
    canvas.set_fill_color(how_to_text, 'blue4')
    return title, play_button, play_text, how_to_button, how_to_text
def how_to(canvas, title, play_button, play_text, how_to_button, how_to_text):
    canvas.delete(title)
    canvas.delete(play_button)
    canvas.delete(play_text)
    canvas.delete(how_to_button)
    canvas.delete(how_to_text)
    guide = canvas.create_image_with_size(350, 50, 800, 400, 'howto1.png')
    play_button = canvas.create_rectangle(500, 500, 500 + button_width, 500 + button_height)
    canvas.set_fill_color(play_button, 'LightSkyBlue2')
    play_text = canvas.create_text(600, 530, 'Play!')
    canvas.set_font(play_text, 'Didot', 40)
    canvas.set_fill_color(play_text, 'blue4')
    canvas.wait_for_click()
    if 500 <=canvas.get_mouse_x() <= 500 + button_width and 500 <= canvas.get_mouse_y() <= 500 + button_height:
        canvas.delete(title)
        canvas.delete(play_button)
        canvas.delete(play_text)
        canvas.delete(how_to_button)
        canvas.delete(how_to_text)
        canvas.set_canvas_background_color('white')
    canvas.delete(guide)

def create_menu(canvas):
    menu = canvas.create_rectangle(CANVAS_WIDTH - MENU_WIDTH - 100, CANVAS_HEIGHT - 700,
                                   CANVAS_WIDTH - MENU_WIDTH - 100 + MENU_WIDTH, CANVAS_HEIGHT - 700 + MENU_HEIGHT)
    canvas.set_fill_color(menu, 'light salmon')
    menu_text = canvas.create_text(1250, 150, 'Menu')
    canvas.set_font(menu_text, 'Rockwell', 40)
    canvas.set_fill_color(menu_text, 'blue4')
def create_money(canvas):
    money_rect = canvas.create_rectangle(1100, 50, 1400, 100 )
    canvas.set_fill_color(money_rect, 'linen')
    money_text = canvas.create_text(1170, 80, 'Money: ')
    canvas.set_font(money_text, 'Rockwell', 30)
    canvas.set_fill_color(money_text, 'dim gray')
def add_room_button(canvas):
    room_rect = canvas.create_rectangle(1120, 200, 1380, 250)
    canvas.set_fill_color(room_rect, 'seashell3')
    add_room_text = canvas.create_text(1260, 230, 'Add Room')
    canvas.set_font(add_room_text, 'Rockwell', 30)
    canvas.set_fill_color(add_room_text, 'dim gray')

def cleaner_button(canvas):
    cleaner_rect = canvas.create_rectangle(1120,300, 1380, 350)
    canvas.set_fill_color(cleaner_rect, 'seashell3')
    cleaner_text = canvas.create_text(1260, 330, 'Hire a Cleaner')
    canvas.set_font(cleaner_text, 'Rockwell', 30)
    canvas.set_fill_color(cleaner_text, 'dim gray')
def restaurant_button(canvas):
    rest_rect = canvas.create_rectangle(1120,400, 1380, 450)
    canvas.set_fill_color(rest_rect, 'seashell3')
    rest_text = canvas.create_text(1260, 430, 'Add Restaurant')
    canvas.set_font(rest_text, 'Rockwell', 30)
    canvas.set_fill_color(rest_text, 'dim gray')

def pool_button(canvas):
    pool_rect = canvas.create_rectangle(1120,500, 1380, 550)
    canvas.set_fill_color(pool_rect, 'seashell3')
    pool_text = canvas.create_text(1260, 530, 'Add Pool')
    canvas.set_font(pool_text, 'Rockwell', 30)
    canvas.set_fill_color(pool_text, 'dim gray')

def suite_button(canvas):
    suite_rect = canvas.create_rectangle(1120,600, 1380, 650)
    canvas.set_fill_color(suite_rect, 'seashell3')
    suite_text = canvas.create_text(1260, 630, 'Add Suite')
    canvas.set_font(suite_text, 'Rockwell', 30)
    canvas.set_fill_color(suite_text, 'dim gray')
def hire_a_cleaner(canvas, cleaner, money, stars):
    if 1120 <= canvas.get_mouse_x() <= 1380 and 300 <= canvas.get_mouse_y() <= 350:
        cleaner = cleaner + 1
        if stars == 0:
            money = money - 1500
    return cleaner, money


def add_room(canvas, y_level, added_rooms, money, second_floors, customers, cleaner):
    if 1120 <= canvas.get_mouse_x() <= 1380 and 200 <= canvas.get_mouse_y() <= 250:
        if added_rooms <= 4:
            canvas.create_image_with_size(100, y_level, BLOCK_WIDTH, BLOCK_HEIGHT, 'room.png')
            added_rooms = added_rooms + 1
            y_level = y_level - BLOCK_HEIGHT
            money = money - room_price
            customers = customers + (added_rooms + second_floors) * 5
        if cleaner == 0 and second_floors < 5:
            money = money + 5 * customers
        if cleaner >= 1 and second_floors < 5:
            money = money + 40 * customers
    return y_level, added_rooms, money, customers

def add_room_new_x(canvas, second_y, second_floors, added_rooms, money, customers, cleaner):
    if 1120 <= canvas.get_mouse_x() <= 1380 and 200 <= canvas.get_mouse_y() <= 250:
        if added_rooms > 4 and second_floors < 5:
            canvas.create_image_with_size(100 + BLOCK_WIDTH, second_y, BLOCK_WIDTH, BLOCK_HEIGHT, 'room.png')
            second_floors = second_floors + 1
            second_y = second_y - BLOCK_HEIGHT
            money = money - room_price
            customers = customers + (added_rooms + second_floors) * 5
        if cleaner == 0 and second_floors < 5:
            money = money + 5 * customers
        if cleaner >= 1 and second_floors < 5:
            money = money + 40 * customers
    return second_y, second_floors, money, customers

def add_rest(canvas, second_floors, restaurant, money):
    if 1120 <= canvas.get_mouse_x() <= 1380 and 400 <= canvas.get_mouse_y() <= 450:
        if second_floors == 5:
            canvas.create_image_with_size(100 + 2 * BLOCK_WIDTH, 600, BLOCK_WIDTH, BLOCK_HEIGHT, 'restaurant.png')
            restaurant = 1
            money = money - 30000
    return restaurant, money

def add_suites(canvas, restaurant, suite_num, money, third_y, customers):
    if 1120 <= canvas.get_mouse_x() <= 1380 and 600 <= canvas.get_mouse_y() <= 650:
        if restaurant == 1 and suite_num < 3:
            canvas.create_image_with_size(100 + 2 * BLOCK_WIDTH, third_y,
                                          BLOCK_WIDTH, BLOCK_HEIGHT, 'suite.png')
            third_y = third_y - BLOCK_HEIGHT
            suite_num = suite_num + 1
            money = money - 15000
            customers = customers + suite_num * 5
            money = customers * 100 + money
    return suite_num, money, third_y, customers

def add_pool(canvas, suite_num, pool, money):
    if 1120 <= canvas.get_mouse_x() <= 1380 and 500 <= canvas.get_mouse_y() <= 550:
        if suite_num >= 3 and pool == 0:
            pool = pool + 1
            canvas.create_image_with_size(100 + 2 * BLOCK_WIDTH, 0, BLOCK_WIDTH - 5, BLOCK_HEIGHT, 'hotelpool.png')
            money = money - 30000
    return pool, money









def messages(canvas, customers, stars):
    message_rect = canvas.create_rectangle(500, 700, CANVAS_WIDTH - 100, 800)
    canvas.set_fill_color(message_rect, 'linen')
    message_text = canvas.create_text(920, 720, 'Add 3 rooms to have 1 star. Do not forget, each room costs 5000$.')
    canvas.set_font(message_text, 'Rockwell', 25)
    canvas.set_fill_color(message_text, 'dim gray')
    star_text = canvas.create_text(630, 770, 'Current Stars: ' + str(stars))
    canvas.set_font(star_text, 'Rockwell', 30)
    canvas.set_fill_color(star_text, 'gold')
    customer_text = canvas.create_text(1000, 770, 'Number of Customers: ' + str(customers))
    canvas.set_font(customer_text, 'Rockwell', 30)
    canvas.set_fill_color(customer_text, 'LightBlue4')






if __name__ == '__main__':
    main()
