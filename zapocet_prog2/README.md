# Fast Fourier Transform

Running the application does not require any special setup, besides installing libraries mentioned in *requirements.txt*

The application can be in 3 different states: *idle*, *recording trace*, *running*. User can itterate forward with SPACE and rest the STATE to *idle* with R key. If the trace is taken from a svg file the application directly skipps to stage *running* 

#### Comandline arguments
* **set screen resoluition:** -r width height
* **input file:** -i image will scaled to screen
* **number of approximation functions:** -n
* **sampling rate for tracing mouse cursor:** -s
* **point density in svg file per path:** -d
* **window update rate:** -u

#### GUI (mentioned in the welcome screen)
* **quitting the app:** ESC
* **toggling elements form view**
  * traced points: P
  * vector lines: L
  * circle on which the vector revolves: C
* **zooming** (can speed up by holding the key)
  * zoom-in: Z
  * zoom-out: X

## Documentation
The application is all inside one module and has a standard pygame structure with infinite loop. The funcitonality relies on two classes.

#### Window
Is responsible for the graphic interface. Creates the welcome screen as well draws grid in the begining. Nothing interesting.

#### FouriesSeries
Does all the calculation. The two main functions are:
* *calculate_coefficienet*: takes the traced points and calculates appropriate coefficient $c_k$ for each function
* *calculate_point*: is called in every itteration of t, it calculates the resulting point which is drawn by the tip of the last vector. It simultaneously draws the vectores and circle on which they rotate

## How does it work
The application tries to demonstrate that an arbitrary curve could be generated as a sum of infinite functions. Since it is not possible to perform infinite calcuilation we can just the show, that by rasing the number of function we can get a pretty close approximaion of the former curve. 

The computation happen on complex plane and all of the rotation are described by expression $c \cdot e^{2\pi i t}$, where the coeficient $c$ determines initial angle and magnitude of the rotating vector. $t$ represents time in rotation

$$ c_n e^{freq \cdot time \cdot 2\pi i}$$

Our goal is to be able to express approximation of an arbitrary curve in form of function:
$$ f(t) = c_{-n} e^{-n \cdot t2\pi i} + ... + c_{0} e^{0} + ... + c_{n} e^{n \cdot t2\pi i}$$

Therefore we need to be able to calculate coeficients $c$.

$$c_k = \int_0^1{f(t)e^{-k \cdot t2\pi i}}$$

Or in the discrete form:

$$c_k = \frac{1}{n} \sum_{l=0}^{n-1}c_l \cdot e^{-k \cdot 2\pi i}$$


need to get the average point with really fine sum, that is basically an intrgral

## Sources and Libraries
I got inspiration for this project from wonderful youtube [video by 3b1b](https://www.youtube.com/watch?v=r6sGWTCMz2k&t=1298s). Calculations of the curve approximation were performed as explained in the video. 

Two non-standar libraries were used in this project. *Pygame* for graphical interface and *svgpathtools* for parsing .svg file, besides that all code was written by me.
