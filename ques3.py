# You are working with a model represented as a binary texture image image. This texture is represented as an n x n grid where each 1 in the grid is a black pixel, and O is a white pixel.
# There are three transformations to apply to the model's texture in this order:
# 1. Rotation: The texture image can be rotated by 90, 180, or 270 degrees clockwise specified in the variable rotation
# 2. Vertical Flip: If verticalFlip 1, flip the image along its horizontal axis. The pixels will appear in reverse order from top to bottom,
# 3. Horizontal Flip: If horizontalFlip 1, flip the image along its vertical axis. The pixels will appear in reverse order from left to right
# Implement a function that applies the transformations and returns the final image.
# The function getFinalimage will take the following inputs:
# int image[n][n] the texture image to process
# int rotation, the rotation parameter
# int verticalFlip, the vertical flip parameter2
# int horizontal Flip the horizontal flip parameter