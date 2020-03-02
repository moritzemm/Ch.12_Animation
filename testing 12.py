import arcade
SW=640
SH=480
class MyGame(arcade.Window):
    '''This is my first game class'''
    def __init__(self,width,height,title):
        super().__init__(width,height,title)
        arcade.set_background_color(arcade.color.BUBBLES)
        self.x = SW/2
        self.y = SH/2

    def on_draw(self):
        arcade.start_render()
        arcade.draw_circle_filled()

def main():
    window=MyGame(SW,SH,"Animation")
    arcade.run()





if __name__=="__main__":
    main()