from game.action import Action
from game.point import Point
from game import constants
class HandleCollisionsAction(Action):
    


    def execute(self, cast):

        """         paddle = cast["paddle"][0]
        ball = cast["ball"][0]
        brick = cast["brick"] """
        
        """         if paddle.get_position().is_boarder(len(paddle.get_text())):
            position = paddle.get_position()
            velocity = paddle.get_velocity()
            x1 = position.get_x()
            y1 = position.get_y()
            x2 = velocity.get_x() * -1
            y2 = velocity.get_y()
            x = 1 + (x1 + x2 - 1)
            y = 1 + (y1 + y2 - 1)
            position = Point(x,y)
            paddle.set_position(position)

        ball_hitbox = ball.get_hitbox()
        for bricks in brick:

            if  bricks.get_position().equals(ball_hitbox["upper"][0]):
                position = ball.get_position()
                velocity = ball.get_velocity()
                x = velocity.get_x() 
                y = velocity.get_y() * -1
                ball.set_velocity(Point(x,y))
             """
            
        ball = cast["ball"][0]
        paddle = cast["paddle"][0] 
        bricks = cast["brick"]
        for brick in bricks:
            if ball.get_position().equals(brick.get_position()):
                bricks.remove(brick)
                ball.set_velocity(Point.reverse_y(ball.get_velocity()))

        if ball.get_position().get_y() == paddle.get_position().get_y():
            if ball.get_position().get_x() >= paddle.get_position().get_x() and ball.get_position().get_x() <= (paddle.get_position().get_x() + 11):
                ball.set_velocity(Point.reverse_y(ball.get_velocity()))

        if ball.get_position().get_y() == 0:
            ball.set_velocity(Point.reverse_y(ball.get_velocity()))
        
        if ball.get_position().get_x() == 0 or ball.get_position().get_x() == constants.MAX_X:
            ball.set_velocity(Point.reverse_x(ball.get_velocity()))

        if ball.get_position().get_y() == constants.MAX_Y:
            quit()


