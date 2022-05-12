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

    # Pass rotation if axis is not defined
    if axis is not np.nan:
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

        # Rotate
        # Transpose coordinates before and after rotation in case multiple points have been given
        point = np.matmul(rotationMatrix, point.transpose()).transpose()

    # Translate
    point = np.add(point, translation)

    return point



def system_transform(point: np.array, angle: float, axis: np.array, center: np.array) -> np.array:
    """
        Coordinate System Transformation

        Arguments:
            point: Point to transform.
            angle: Angle of rotation.
            axis: Axis of rotation
            center: Center of new co. system

        Returns:
            point in the new system
    """

    return point