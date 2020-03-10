'''
SNOWFALL
--------
Try to create the snowfall animation by meeting
the following requirements:

1.) Create a 600 x 600 window with black background*
2.) Window title equals "Snowfall"*
3.) Crossbars 10 px wide. Snow must be outside!
4.) Make snowflake radius random between 1-3
5.) Randomly start snowflakes anywhere in the window.
6.) Random downward speed of -4 to -1
7.) Start snowflakes again at random x from 0-600 and random y from 600-700
8.) Generate 300 snowflakes
9.) Color snowflake #1 red just for fun.
10.) All other snowflakes should be white.


'''
import arcade
import random
SW=600
SH=600
SF=300
class Snow:
    def __init__(self,pos_x,pos_y,dy,radius,color):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.dy = dy
        self.radius = radius
        self.color = color

    def draw_snow(self):
        arcade.draw_circle_filled(self.pos_x,self.pos_y,self.radius,self.color)

    def update_snow(self):
        self.pos_y+=self.dy

        #bouncing the snow off the edges direct tv style
        if self.pos_y<0:
            self.pos_x=random.randint(0,SW)
            self.pos_y=random.randint(SH,SH+100)


class MyGame(arcade.Window):
    '''This is my first game class'''
    def __init__(self,width,height,title):
        super().__init__(width,height,title)
        arcade.set_background_color(arcade.color.BLACK)
        self.snow_list=[]
        for i in range(SF):
            dy = random.randint(-4, -1)
            rad=random.randint(1,3)
            x = random.randint(0,SW)
            y = random.randint(0,SH)
            if i == 0:
                color=arcade.color.RED
            else:
                color=arcade.color.WHITE

            snow=Snow(x,y,dy,rad,color)
            self.snow_list.append(snow)

    def on_draw(self):
        arcade.start_render()
        for snow in self.snow_list:
            snow.draw_snow()
        arcade.draw_rectangle_filled(SW/2,SH/2,10,SH,arcade.color.OTTER_BROWN)
        arcade.draw_rectangle_filled(SW/2,SH/2,SW,10, arcade.color.OTTER_BROWN)

    def on_update(self,dt):
        for snow in self.snow_list:
            snow.update_snow()

def main():
    window=MyGame(SW,SH,"SnowFall")
    arcade.run()



if __name__=="__main__":
    main()