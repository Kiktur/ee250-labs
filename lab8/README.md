Team Members: Victor Gutierrez (USC ID: 9841169875) Angie Vasquez (USC ID: 5537473368)

Question 1: What are the denominations of the US coins from the green, blue, and
orange distributions?
Can you think why the coins from the same denomination might show variation in
weight, although they are specified to be of the same weight?
If your vending machine had a weight sensor, how would you use the weight of a coin
that was just inserted to find the denomination?

The three distributions represent U.S coin denominations, including penny,nickel,and dime, and they each have distinct average weights. Small variations also occur due to there being manufacturing tolerances, and they have wear, which slightly alter the coin’s weight and reflectance. A vending machine with a weight sensor would measure how heavy the coin is and then compare it to the known weight ranges it learned during training to decide which coin it is(penny,nickel, or dime).

Question 2. We can shine light on the coin and measure the reflected amount of light,
which should be proportional (directly or in some non-linear way) to the size/area of the
coin. Can you guess which sensor on the Grove Pi Kit can be used for this purpose?

The grove light sensor can be used to measure the reflected light from a coin’s surface. The sensor’s analog output increases with brightness, so it can estimate how much light reflects off the coin, which correlates with the coin’s size and material. This reflectance value can then be used along with weight to improve classification accuracy.


Question 3: Which of the following datasets are linearly separable? Justify your answer.
From the plots, only Dataset A can be separated by a single line because the blue and orange points are clearly on different sides. The other datasets are not linearly separable since their points overlap, or for clusters, they would need to have multiple boundaries to be separate.


Question 4. Sometimes we need more than a simple hyperplane to separate the
datasets of the two classes. What are some other simple geometric entities other than a
simple plane/line that can be used to separate some of the data points that were not
linearly separable?

When the data can’t be separated by a straight line, we can use curved shapes such as: 
Circle → (x−h)2+(y−k)2=r2(x−h)2+(y−k)2=r2,Parabola → (y−k)2=4a(x−h)(y−k)2=4a(x−h),
Ellipse → (x−h)2a2+(y−k)2b2=1a2(x−h)2​+b2(y−k)2​=1, Hyperbola → (x−h)(y−k)=c(x−h)(y−k)=c
With these shapes they can form non linear boundaries that separate data points when a single straight line can’t. The neural networks learn these kinds of curved boundaries automatically using activation functions.


Question 5. For the example shown in the figure, what is approximately the output of the
neuron?
The bias is -2 [if anybody has any confusion]

The weighted sum is 4, and after applying the sigmoid activation function, the output is about 0.98. Since the value is very close to 1, the neuron is strongly “activated,” meaning its confident in its positive class prediction.
