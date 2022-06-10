import numpy as np
import cv2

import src

# Load data
print('Load data...')
data = np.load('hw2.npy', allow_pickle = True)

verts3d = data[()]['verts3d']
faces = data[()]['faces']
vcolors = data[()]['vcolors']
c_org = data[()]['c_org']
c_lookat = data[()]['c_lookat']
c_up = data[()]['c_up']
t_1 = data[()]['t_1']
t_2 = data[()]['t_2']
u = data[()]['u']
phi = data[()]['phi']

print('Done!')

# Step 0
print('Render image 0...')
img = src.render_object(
    verts3d,
    faces,
    vcolors,
    src.IMG_HEIGHT,
    src.IMG_WIDTH,
    src.CAMERA_HEIGHT,
    src.CAMERA_WIDTH,
    src.F,
    c_org,
    c_lookat,
    c_up
)
cv2.imwrite(
    '0.jpg',
    cv2.cvtColor( (img*255).astype(np.uint8), cv2.COLOR_RGB2BGR)
)

print('Done!')

# Step a
print('Render image a...')
verts3d = src.affine_transform(verts3d, translation = t_1)
img = src.render_object(
    verts3d,
    faces,
    vcolors,
    src.IMG_HEIGHT,
    src.IMG_WIDTH,
    src.CAMERA_HEIGHT,
    src.CAMERA_WIDTH,
    src.F,
    c_org,
    c_lookat,
    c_up
)
cv2.imwrite(
    'a.jpg',
    cv2.cvtColor( (img*255).astype(np.uint8), cv2.COLOR_RGB2BGR)
)

print('Done!')

# Step b
print('Render image b...')
verts3d = src.affine_transform(verts3d, phi, u)
img = src.render_object(
    verts3d,
    faces,
    vcolors,
    src.IMG_HEIGHT,
    src.IMG_WIDTH,
    src.CAMERA_HEIGHT,
    src.CAMERA_WIDTH,
    src.F,
    c_org,
    c_lookat,
    c_up
)
cv2.imwrite(
    'b.jpg',
    cv2.cvtColor( (img*255).astype(np.uint8), cv2.COLOR_RGB2BGR)
)

print('Done!')

# Step c
print('Render image c...')
verts3d = src.affine_transform(verts3d, translation = t_2)
img = src.render_object(
    verts3d,
    faces,
    vcolors,
    src.IMG_HEIGHT,
    src.IMG_WIDTH,
    src.CAMERA_HEIGHT,
    src.CAMERA_WIDTH,
    src.F,
    c_org,
    c_lookat,
    c_up
)
cv2.imwrite(
    'c.jpg',
    cv2.cvtColor( (img*255).astype(np.uint8), cv2.COLOR_RGB2BGR)
)

print('And done!')