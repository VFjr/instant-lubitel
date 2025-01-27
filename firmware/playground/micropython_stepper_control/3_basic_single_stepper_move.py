from machine import Pin
import time

# Pin Definitions - Adjust these to match your wiring
STEP_PIN = 5  # GPIO pin connected to STEP pin of A4988
DIR_PIN = 6   # GPIO pin connected to DIR pin of A4988

# Motor Configuration
STEPS_PER_SECOND = 100  # Adjust this to change speed
DIRECTION = 1          # 1 for clockwise, 0 for counterclockwise

# Setup pins as outputs
step_pin = Pin(STEP_PIN, Pin.OUT)
dir_pin = Pin(DIR_PIN, Pin.OUT)

# Set initial direction
dir_pin.value(DIRECTION)

# Calculate delay in nanoseconds (1 second = 1_000_000_000 nanoseconds)
# Factor of 2 because we need two delays per step
step_delay_ns = 1_000_000 // (2 * STEPS_PER_SECOND)

def move_stepper():
    try:
        while True:
            # Generate one step
            step_pin.value(1)
            time.sleep_us(step_delay_ns)
            step_pin.value(0)
            time.sleep_us(step_delay_ns)
            
    except KeyboardInterrupt:
        print("\nStopping motor...")

print(f"Moving stepper at {STEPS_PER_SECOND} steps per second")
print("Press Ctrl+C to stop")
move_stepper()
