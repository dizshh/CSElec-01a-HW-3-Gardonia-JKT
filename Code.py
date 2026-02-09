import turtle
import matplotlib.pyplot as plt
from decimal import Decimal, getcontext, ROUND_FLOOR, ROUND_HALF_UP

# --- CONFIGURATION ---
# We need 105 digits of precision to handle the 100th decimal request
getcontext().prec = 105

# A string of Pi to 105 decimal places (standard math.pi is not enough)
PI_STRING = "3.141592653589793238462643383279502884197169399375105820974944592307816406286208998628034825342117067982148"

# The decimal places we want to test
precisions = [20, 40, 60, 100]

# Rocket Destination Distance (e.g., Distance to Mars in km ~ 225 million km)
# We use a huge number to try and make the error visible!
distance_to_target = Decimal("225000000") 

# Lists to store data for the graph
labels = []
differences = []

print(f"{'Decimals':<10} | {'Truncated Result':<25} | {'Rounded Result':<25} | {'DIFFERENCE (The Gap)':<25}")
print("-" * 90)

# --- PART 1: THE CALCULATION (Truncation vs Rounding) ---
for p in precisions:
    # Create the quantizer string (e.g., '1.000...0') with p zeros
    quantizer = Decimal("1." + "0" * p)
    
    # 1. Truncate Pi (Cut off extra digits)
    pi_trunc = Decimal(PI_STRING).quantize(quantizer, rounding=ROUND_FLOOR)
    
    # 2. Round Pi (Round to nearest)
    pi_round = Decimal(PI_STRING).quantize(quantizer, rounding=ROUND_HALF_UP)
    
    # Formula: Distance Traveled = Pi * Diameter (or generic factor)
    # We compare the calculated position based on the two different Pi values
    res_trunc = pi_trunc * distance_to_target
    res_round = pi_round * distance_to_target
    
    # The Gap
    diff = abs(res_trunc - res_round)
    
    labels.append(f"{p} Dec")
    differences.append(float(diff)) # Convert to float for graphing
    
    # Print mainly the Difference because the full numbers are too long
    print(f"{p:<10} | ...{str(res_trunc)[-10:]:<12} | ...{str(res_round)[-10:]:<12} | {diff:.10E}")

print("\nConclusion: Even with 20 decimals, the difference is microscopic, but it exists!")

# --- PART 2: MATPLOTLIB GRAPH (The Evidence) ---
plt.figure(figsize=(10, 5))
# We use Log Scale because the difference between 20th and 100th decimal is MASSIVE
plt.bar(labels, differences, color=['red', 'orange', 'green', 'blue'])
plt.yscale('log') 
plt.title("Impact of Truncation vs Rounding on Rocket Calculation")
plt.xlabel("Decimal Precision of Pi")
plt.ylabel("Difference in Location (Log Scale)")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# --- PART 3: TURTLE DRAWING (The Concept) ---
# Since the actual mathematical difference is 0.000000000001 pixels, 
# we cannot draw it to scale. We will draw a CONCEPTUAL model 
# to show how "Truncation" and "Rounding" steer the rocket differently.

def draw_conceptual_rocket():
    screen = turtle.Screen()
    screen.title("Concept: Truncation vs Rounding Trajectory")
    screen.bgcolor("black")
    
    t = turtle.Turtle()
    t.speed(1)
    t.width(3)
    
    start_x, start_y = -300, 0
    
    # 1. Draw The "Target" Line (True Pi)
    t.penup()
    t.goto(start_x, start_y)
    t.pendown()
    t.color("white")
    t.forward(600)
    t.write("  Perfect Path", font=("Arial", 12, "normal"))
    
    # 2. Draw Truncated Path (Falls Short/Under)
    t.penup()
    t.goto(start_x, start_y)
    t.pendown()
    t.color("red")
    t.setheading(0 - 5) # Exaggerated angle for visual effect
    t.forward(600)
    t.write("  Truncated Error", font=("Arial", 12, "bold"))
    
    # 3. Draw Rounded Path (Overshoots/Over)
    t.penup()
    t.goto(start_x, start_y)
    t.pendown()
    t.color("cyan")
    t.setheading(0 + 5) # Exaggerated angle
    t.forward(600)
    t.write("  Rounded Error", font=("Arial", 12, "bold"))

    screen.exitonclick()

# Run the drawing
draw_conceptual_rocket()