import numpy as np
import csv
import math
import matplotlib.pyplot as plt

file = "detumble_csv.csv"

def graph(file, sat_XYZ):
   field_vectors = []
   time_count = []
   with open(file, 'r') as file:
        csv_reader = csv.DictReader(file)

        max_iterations = 300  # Set the limit for the number of loops


        for iteration, row in enumerate(csv_reader):
            max_iterations = 1048576
            # Stopping iterations at a certain maximum
            if iteration >= max_iterations:
                break
            else:
                # Convert the x, y, z components from strings to floats
                field_XYZ = (float(row['x_(nT)'].strip()), float(row['y_(nT)'].strip()), float(row['z_(nT)'].strip()))
                
                # Calculate the angle between satellite vector and field vector
                angle = vector_angles(sat_XYZ, field_XYZ)  # Assuming sat_XYZ is (0, 0, 0) to get angle of magnetic field

                # Store the result in the list with iterations to measure time in seconds
                field_vectors.append(angle)
                time_count.append(iteration)

        plt.plot(time_count, field_vectors, 'ro', markersize = 0.1)
        plt.ylabel('angle (rad)')
        plt.xlabel('time (seconds)')
        plt.title(f'Error of Detumbling Simulation for {max_iterations} seconds compared to [{sat_XYZ}]')
        plt.show()
            


# Function to calculate the angle between two vectors
def vector_angles(sat_XYZ, field_XYZ):
    sat_vector = np.array(sat_XYZ)
    field_vector = np.array(field_XYZ)

    # Compute dot product
    dot_product = np.dot(sat_vector, field_vector)

    # Compute magnitudes
    sat_magnitude = np.linalg.norm(sat_vector)
    field_magnitude = np.linalg.norm(field_vector)

    # Calculate angle (error) in radians
    error = math.acos(dot_product / (sat_magnitude * field_magnitude))

    return error

# Create graph
graph(file, (1, 1, 70000))
