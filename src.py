import numpy as np

# Conf
IMG_WIDTH = 512
IMG_HEIGHT = 512
CAMERA_WIDTH = 15
CAMERA_HEIGHT = 15
F = 70
BACKGROUND = [1., 1., 1.]



def affine_transform(point: np.ndarray, angle = 0., axis: np.ndarray = np.nan, translation = np.array([0, 0, 0])) -> np.ndarray:
    """
        Perform 3D Affine Transformation

        Arguments:
            point: Point(s) to transform.
            angle: Angle of rotation.
            axis: Axis of rotation
            translation: Translation of point(s)

        Returns:
            new point(s) coordinates
    """

    # Pass rotation if axis is not defined or angle is 0
    if axis is not np.nan or angle != 0:
        # Create rotation matrix
        rotationMatrix = _rotation_matrix(angle, axis)

        # Rotate
        # Transpose coordinates before and after rotation in case multiple points have been given
        point = np.matmul(rotationMatrix, point.transpose()).transpose()

    # Translate
    point = np.add(point, translation)

    return point



def system_transform(point: np.ndarray, angle = 0., axis: np.ndarray = np.nan, center = np.array([0, 0, 0])) -> np.ndarray:
    """
        Coordinate System Transformation

        Arguments:
            point: Point(s) to transform.
            angle: Angle of rotation.
            axis: Axis of rotation
            center: Center of new co. system

        Returns:
            point(s) coordinates in the new system
    """

    # Translate point to new center
    point = np.add(point, -center)

    # Pass rotation if axis is not defined or angle is 0
    if axis is not np.nan or angle != 0:
        # Create rotation matrix
        rotationMatrix = _rotation_matrix(-angle, axis)

        # Rotate
        # Transpose coordinates before and after rotation in case multiple points have been given
        point = np.matmul(rotationMatrix, point.transpose()).transpose()

    return point



def _rotation_matrix(angle = 0., axis: np.ndarray = np.nan) -> np.ndarray:
    """
        Create rotation matrix

        Arguments:
            angle: Angle of rotation.
            axis: Axis of rotation
        Returns:
            rotation matrix
    """

    if axis is np.nan or angle == 0:
        return np.identity(3)
    
    # Get unit vector of axis
    u = axis / np.linalg.norm(axis)

    sinA = np.sin(angle)
    cosA = np.cos(angle)

    rotationMatrix = np.array([
        [
            (u[0]**2) * (1 - cosA) + cosA,
            u[0] * u[1] * (1 - cosA) - u[2] * sinA,
            u[0] * u[2] * (1 - cosA) + u[1] * sinA
        ],
        [
            u[1] * u[0] * (1 - cosA) + u[2] * sinA,
            (u[1]**2) * (1 - cosA) + cosA,
            u[1] * u[2] * (1 - cosA) - u[0] * sinA
        ],
        [
            u[2] * u[0] * (1 - cosA) - u[1] * sinA,
            u[2] * u[1] * (1 - cosA) + u[0] * sinA,
            (u[2]**2) * (1 - cosA) + cosA
        ]
    ])

    return rotationMatrix