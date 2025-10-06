# jpg-wav-converter
A simple Python program that converts .jpg files into .wav files and vice versa.
## Usage
Program requires two directories called input and output. Place files you want to convert into input. Run the program and the output files will be placed into output.
## How it Works
Program converts .jpg file into 3 different arrays, one for each RGB value. Data is converted into a .wav file with the data from R being the right channel, the data from G being the left, and B being centered.
Program converts data from .wav file into a flattened array. A square .jpg image is created from data.
