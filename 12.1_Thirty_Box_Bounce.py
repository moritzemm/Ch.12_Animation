'''
30 BOX BOUNCE PROGRAM
--------------------
You will want to incorporate lists to modify the
Ball Bounce Program to create the following:

1.) Screen size 600 x 600
2.) Draw four 30px wide side rails on all four sides of the window
3.) Make each side rail a different color.
4.) Draw 30 black boxes(squares) of random size from 10-50 pixels
5.) Animate them starting at random speeds from -300 to +300 pixels/second. 
6.) All boxes must be moving.
7.) Start all boxes in random positions between the rails.
8.) Bounce boxes off of the side rails when the box edge hits the side rail.
9.) When the box bounces change its color to the rail it just hit.
10.)Title the window 30 Boxes

Helpful Hints:
1.) When you initialize the MyGame class create an empty list called self.boxlist=[] to hold all of your boxes.
2.) Then use a for i in range(30): list to instantiate boxes and append them to the list.
3.) In the on_draw section use: for box in self.boxlist: box.draw_box()
4.) Also in the on_draw section draw the side rails.
5.) In the on_update section use: for box in self.boxlist: box.update_box()
'''
import arcade
import random
SW=600
SH=600
Box_Num=30
class Box:
    def __init__(self,pos_x,pos_y,dx,dy,side,color):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.dx = dx
        self.dy = dy
        self.side = side
        self.color = color

    def draw_box(self):
        arcade.draw_rectangle_filled(self.pos_x,self.pos_y,self.side,self.side,self.color)

    def update_box(self):
        self.pos_y+=self.dy
        self.pos_x+=self.dx

        #bouncing off the sides and changing the color
        if self.pos_x<30+self.side/2:#left side
            self.dx*=-1
            self.color=arcade.color.RED
        if self.pos_x>SW-30-self.side/2:#right side
            self.dx*=-1
            self.color=arcade.color.YELLOW
        if self.pos_y<30+self.side/2:#bottom
            self.dy*=-1
            self.color=arcade.color.BLUE
        if self.pos_y>SH-30-self.side/2:#top
            self.dy*=-1
            self.color=arcade.color.GREEN



class MyGame(arcade.Window):
    '''This is my first game class'''
    def __init__(self,width,height,title):
        super().__init__(width,height,title)
        arcade.set_background_color(arcade.color.WHITE)
        self.box_list=[]
        for i in range(Box_Num):
            dy = random.randint(-5, 5)
            dx = random.randint(-5, 5)
            side =random.randint(10,50)
            x = random.randint(30+int(side/2),SW-30-int(side/2))
            y = random.randint(30+int(side/2),SH-30-int(side/2))
            color=arcade.color.BLACK
            if dx == 0 and dy == 0:
                dx=100
                dy=100

            box=Box(x,y,dx,dy,side,color)
            self.box_list.append(box)

    def on_draw(self):
        arcade.start_render()
        for box in self.box_list:
            box.draw_box()
        arcade.draw_rectangle_filled(15,SH/2,30,SH-60,arcade.color.RED)
        arcade.draw_rectangle_filled(SW-15, SH / 2, 30, SH - 60, arcade.color.YELLOW)
        arcade.draw_rectangle_filled(SW/2, SH-15, SW - 60,30, arcade.color.GREEN)
        arcade.draw_rectangle_filled(SW/2, 15, SW - 60, 30, arcade.color.BLUE)


    def on_update(self,dt):
        for box in self.box_list:
            box.update_box()

def main():
    window=MyGame(SW,SH,"Box_Bounce")
    arcade.run()



if __name__=="__main__":
    main()