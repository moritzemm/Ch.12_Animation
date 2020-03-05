import arcade
SW=640
SH=480
class Ball:
    def __init__(self,pos_x,pos_y,dx,dy,radius,color):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.dx = dx
        self.dy = dy
        self.radius = radius
        self.color = color

    def draw_ball(self):
        arcade.draw_circle_filled(self.pos_x,self.pos_y,self.radius,self.color)

    def update_ball(self):
        self.pos_x+=self.dx
        self.pos_y+=self.dy

        #bouncing the ball off the edges
        if self.pos_x<self.radius or self.pos_x>SW-self.radius:
            self.dx*=-1
        if self.pos_y<self.radius or self.pos_y>SH-self.radius:
            self.dy*=-1

class MyGame(arcade.Window):
    '''This is my first game class'''
    def __init__(self,width,height,title):
        super().__init__(width,height,title)
        arcade.set_background_color(arcade.color.BUBBLES)
        self.ball=Ball(SW/2,SH/2,3,-2,15,arcade.color.AFRICAN_VIOLET)

    def on_draw(self):
        arcade.start_render()
        self.ball.draw_ball()

    def on_update(self,dt):
        self.ball.update_ball()

def main():
    window=MyGame(SW,SH,"Animation")
    arcade.run()



if __name__=="__main__":
    main()