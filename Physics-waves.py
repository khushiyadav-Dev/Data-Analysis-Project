import math
import time

def wave_pattern():
    print("--- Khushi's Python Wave ---")
    for i in range(0, 100):
        # Sine function ka use karke spaces calculate karna
        # 10 is amplitude, 15 is offset
        spaces = int(10 * math.sin(i / 5.0) + 15)
        
        # Har line mein wave print karna
        print(' ' * spaces + '*')
        
        # Thoda sa delay taaki animation dikhe
        time.sleep(0.05)

if __name__ == "__main__":
    wave_pattern()
