import turtle

MOVE_SPEED = 20

class Snake:
    def __init__(self):
        """Initialize the Snake class with an empty list of segments."""
        self.segments = []
        self.create_snake()

    def create_segment(self):
        """Creates a single segment of the snake."""
        segment = turtle.Turtle()
        segment.shape("square")
        segment.color((192, 190, 190))
        segment.penup()
        self.segments.append(segment)

    def create_snake(self):
        """Creates the head and initial segments of the snake."""
        # Create the head of the snake
        self.head = turtle.Turtle()
        self.head.shape("square")
        self.head.color("white")
        self.head.penup()
        self.segments.append(self.head)

        # Create body segments
        for _ in range(5):
            self.create_segment()

        # Position the segments in a line
        back_pace = 20
        for segment in self.segments:
            segment.backward(back_pace)
            back_pace += 20

    def move(self):
        """Move the snake by updating the positions of the segments."""
        # Move each segment to the position of the segment in front of it
        for i in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[i - 1].xcor()
            new_y = self.segments[i - 1].ycor()
            self.segments[i].goto(new_x, new_y)

        # Move the head forward
        self.head.forward(MOVE_SPEED)
