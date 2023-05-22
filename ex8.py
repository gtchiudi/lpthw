formatter = "{} {} {} {}" # this will allow the placement of 4 variables in a format() with spaces in between.

print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
	"try your",
	"Own text here",
	"Maybe a poem",
	"Or a song about fear"
))
