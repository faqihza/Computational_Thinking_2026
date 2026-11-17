import turtle

actor = turtle.Turtle()
actor.shape("turtle")
actor.color("red")

actor.left(36)

for i in range(5):
	actor.forward(200)
	actor.left(144)

turtle.done()
