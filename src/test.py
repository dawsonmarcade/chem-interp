import numpy as np


coords = []
 
for i in range (0, 200):
    coords.append((np.random.rand(1,2) * 10))

def main():
    print(coords)

if __name__ == "__main__":
    main()