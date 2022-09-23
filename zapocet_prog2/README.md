# Demonstration of Discrete Fourier Transform
 
Running the application does not require any special setup, besides installing libraries mentioned in *requirements.txt*
 
The application can be in 3 different states: *idle*, *recording trace*, *running*. User can iterate forward with SPACE and rest the STATE to *idle* with R key. If the trace is taken from a svg file the application directly skipps to stage *running*
 
#### Comandline arguments
* *set screen resolution:* -r width height
* *input file:* -i image will scaled to screen
* *number of approximation functions:* -n
* *sampling rate for tracing mouse cursor:* -s
* *point density in svg file per path:* -d
* *window update rate:* -u
 
#### GUI (mentioned in the welcome screen)
* *quitting the app:* ESC
* *toggling elements form view*
 * traced points: P
 * vector lines: L
 * circle on which the vector revolves: C
* *zooming* (can speed up by holding the key)
 * zoom-in: ↑
 * zoom-out: ↓
* *#vectors*
  * increase: → 
  * decrease: ←
   
## Documentation
The application is all inside one module and has a standard pygame structure with infinite loop. The functionality relies on two classes.
 
#### Window
Is responsible for the graphic interface. Presents the welcome screen as well as draws a grid in the beginning and contains all information about the "canvas".
 
#### Fourier Transform
Does all the calculation. The two main functions are:
* *calculate_coefficienet*: takes the traced points and calculates appropriate coefficient $c_k$ for each function
* *calculate_point*: is called in every iteration of t, it calculates the resulting point which is drawn by the tip of the last vector. It simultaneously draws the vectores and circle on which they rotate
 
## The idea behind it
The application tries to demonstrate that an arbitrary curve could be generated as a sum of infinite functions. Since it is not possible to perform infinite calculation we can just show that by raising the number of functions we can get a pretty close approximation of the former curve. First we will look at the formal infinite definition and then discretize it.
 
The computation happens in a complex plane and all of the rotations are described by expression $c \cdot e^{freq \cdot time \cdot 2\pi i}$, where the coefficient $c$ determines initial angle and magnitude of the rotating vector. Our goal is to be able to express approximation of an arbitrary curve in form of function:
 
$$ f(t) = c_{-n} e^{-n \cdot t2\pi i} + ... + c_{-1} e^{-1 \cdot t2\pi i} + c_{0} e^{0} + c_{1} e^{1 \cdot t2\pi i} + ... + c_{n} e^{n \cdot t2\pi i}$$
 
Therefore we need to be able to calculate coefficients $c$. The easiest to find is the constant $c_0$, since the vector is not rotating the value of $c_0$ is equal to the average of all traced points. With finer distribution of points we will get the term $c_0$ in the limit. This infinite sum can be described as the integral $\int_0^1{f(t)dt}$. To get the average we would normally divide the sum by length of the input range, but that is equal to 1.
 
$$\int_0^1{f(t)dt} = \int_0^1{c_{-n} e^{-n \cdot t2\pi i}} + ... + \int_0^1{c_{0} e^{0 \cdot t2\pi i}} + ... + \int_0^1{c_{n} e^{n \cdot t2\pi i}}$$
 
We are able to split the integral and look at each term separately as the $t$ goes from zero to one. Every vector except the one with $c_0$ will make a whole number of rotations around the center, therefore their averages would be 0. Since $e^{0 \cdot t2\pi i}$ stays static the value $c_0$ would just be the position on which the vector has started. Now we can see that $\int_0^1{f(t)dt}$ in fact equals $c_0$.
 
This neat trick can be further generalized to calculate any arbitrary coefficient $k$. The idea is to multiply the whole function by the expression which would stabilize the vector $k$. So, to *"kill"* the exponent in $c_k e^{k \cdot t2\pi i}$ needs to be multiplied by $e^{-k \cdot t2\pi i}$. We can be certain that there would not be any other static vector. The rotating frequencies for a  $\{-n, -n+1, ..., 0, ... n-1, n\}$ after applying $e^{-k \cdot t2\pi i}$ the set would shift and there would remain just one vector with the zero frequency. Finally we get formula:
 
$$c_k = \int_0^1{f(t)e^{-k \cdot t2\pi i}}$$
 
However, we will need to implement a discrete fourier transform. If we consider $p$ as the set of traced points then the coefficients could be computed like this:
 
$$c_k = \frac{1}{n} \sum_{t=0}^{n-1}p_t \cdot e^{-k \cdot \frac{t}{n} 2\pi i}$$
 
Why  bother with moving this into a complex plane? The computation is just cleaner in comparison to:
$$c_k = \frac{1}{n} \sum_{t=0}^{n-1} p_t (\cos(k \cdot \frac{t}{n} 2\pi i) - i\sin(k \cdot \frac{t}{n} 2\pi i))$$
 
 
## Sources and Libraries
I got inspiration for this project from wonderful youtube [video by 3b1b](https://www.youtube.com/watch?v=r6sGWTCMz2k&t=1298s). Calculations of the curve approximation were performed as explained in the video.
 
Two non-standard libraries were used in this project. *Pygame* for graphical interface and *svgpathtools* for parsing .svg file, besides that all code was written by me.
