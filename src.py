import numpy as np

# Conf
IMG_WIDTH = 512
IMG_HEIGHT = 512
CAMERA_WIDTH = 15
CAMERA_HEIGHT = 15
F = 70
BACKGROUND = [1., 1., 1.]

def affine_transform(point: np.array, angle: float, axis: np.array, displacement: np.array) -> np.array:
    """
        Perform 3D Affine Transformation

        Arguments:
            point: Point to transform.
            angle: Angle of rotation.
            axis: Axis of rotation
            displacement: Displacement of point

        Returns:
            new point
    """

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