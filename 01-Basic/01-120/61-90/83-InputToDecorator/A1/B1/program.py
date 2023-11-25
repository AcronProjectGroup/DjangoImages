from Decorators import OutLayerDecorator

@OutLayerDecorator(2)
def RepeaterTwice():
    print("First Function")

@OutLayerDecorator(3)
def RepeaterThreeTimes():
    print("Second Function")


RepeaterTwice()
RepeaterThreeTimes()
# Output:
    # First Function
    # First Function
    # Second Function
    # Second Function
    # Second Function
