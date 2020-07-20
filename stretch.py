your_limb = input("💬 What would you like to stretch? -> ")
your_direction = input("💬 Which direction would you like to stretch it? -> ")

def stretch(limb, direction):
    print("💬 Your "+ limb.lower() + " is gently stretched " + direction.lower())

stretch(your_limb, your_direction)
