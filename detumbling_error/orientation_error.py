import numpy as np

# Normalize quaternions (set magnitude to 1)
def normalize(q):
    norm = np.linalg.norm(q)
    return q / norm

# Find quaternion conjugate
def conjugate(q):
    q_conjugate = np.copy(q)
    q_conjugate[1:] *= -1
    return q_conjugate

# Multiply both quaternions
def multiply(q1, q2):
    w1, x1, y1, z1 = q1
    w2, x2, y2, z2 = q2
    product = np.array([w1*w2 - x1*x2 - y1*y2 - z1*z2, w1*x2 + x1*w2 + y1*z2 - z1*y2, w1*y2 - x1*z2 + y1*w2 + z1*x2, w1*z2 + x1*y2 - y1*x2 + z1*w2])
    return product

def calculate_error(q_sat, q_field):

    # Normalize quaternions
    q_sat= normalize(q_sat)
    q_field = normalize(q_field)

    # Find difference quaternion
    q_error = multiply(conjugate(q_sat), q_field)

    # Get the angle of rotation through scalar part of difference quaternion
    theta = 2 * np.arccos(q_error[0])
    print(f"Orientation error (angle in radians): {theta}")


# Example quaternions
q_sat = np.array(1000, 2000, 3000, 4000)
q_field = np.array(5000, 6000, 7000, 8000)

if __name__ == "__main__":
    calculate_error(q_sat, q_field)
