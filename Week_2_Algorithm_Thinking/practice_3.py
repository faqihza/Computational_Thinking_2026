import turtle

actor = turtle.Turtle()
actor.shape("turtle")
actor.color("red")

for i in range(3):
	actor.forward(20)
	actor.left(90)
	actor.forward(20)
	actor.right(90)

for i in range(3):
	actor.forward(20)
	actor.right(90)

	for j in range(3):
		actor.forward(20)
		actor.left(90)
		actor.forward(20)
		actor.right(90)


turtle.done()