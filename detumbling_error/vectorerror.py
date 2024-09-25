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

        max_iterations = 1209602  # Set the limit for the number of loops


        for iteration, row in enumerate(csv_reader):
            if iteration >= max_iterations:
                break
            else:
                # Convert the x, y, z components from strings to floats and create magnetic field vector
                field_XYZ = (float(row['x_(nT)'].strip()), float(row['y_(nT)'].strip()), float(row['z_(nT)'].strip()))
                
                # Calculate the angle between satellite vector and field vector
                angle = vector_angles(sat_XYZ, field_XYZ)
               
                # Store the result in the list with iterations to measure time in seconds
                field_vectors.append(angle)
                time_count.append(iteration)

        plt.plot(time_count, field_vectors, 'ro', markersize = 0.1) # Plot error vs time

        # Label axes
        plt.ylabel('angle (rad)')
        plt.xlabel('time (seconds)')

        plt.title(f'Error of Detumbling Simulation for {max_iterations} seconds compared to [{sat_XYZ}]') # Title graph for readability
        plt.show() #Show graph
            


# Function to calculate the angle between two vectors
def vector_angles(sat_XYZ, field_XYZ):

    # Convert to vectors
    sat_vector = np.array(sat_XYZ)
    field_vector = np.array(field_XYZ)

    # Compute dot product
    dot_product = np.dot(sat_vector, field_vector)

    # Normalize magnitudes
    norm_sat = np.linalg.norm(sat_vector)
    norm_field = np.linalg.norm(field_vector)

    # Calculate angle (error) in radians
    error = math.acos(dot_product / (norm_sat * norm_field))

    return error

# Create graph
graph(file, (1, 1, 70000))
