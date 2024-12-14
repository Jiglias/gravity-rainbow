# physics-emulation
creates a rainbow bloom effect from input monochrome images, as shown in the examples folder.

it treats the luminosity of pixels as mass and sums their effect to all other pixels using the inverse square law to create a "gravitiational field". the field is represented by a hsv image, where the hue at each point is determined by the direction, and the value is determined by gravitational acceleration.

### How to generate image
1. Put a png in the main folder, where the brighter a pixel is the denser it is.
2. change the name variable in the python folder to match the png,
3. optionally change the gravitional constant depnding on how bright the original image is
4. run python file
