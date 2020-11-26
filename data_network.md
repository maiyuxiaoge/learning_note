[toc]
# What is a network

- a system of links that interconnect nodes in order to exchange information
- two type of nodes:
- 
  - hosts: sources and sinks of information
  - Router: relay nodes that simply forward information

# packet vs circuits

- Internet is a packet switching network.

# ip: the glue of the internet
- hosts and routers are tied together by ip(internet protocol),a single common interface between users and the network and between networks.

# hierarchical addressing
- DNS is a distributed directory system that translates names into ip address.

# osi system interconnection(OSI)
![picture 1](images/bb1bf6412c91f428913996cef642eca0a144cc85bd7d5dd382bb88110b9d58ac.png)  
![picture 2](images/d60fe913cf511cdb0b6e4e559609347c588229bf57136306b9b186f71e532e73.png)  

# router forward packets
- routers determine the next hop for a packet based on the destination ip address.
- routing algorithms ensure packets follow the shortest path

# properties of links

- capacity: width of the link


# example of commication media
![picture 7](images/11beea0a980cb7928cbb82eb25f7674dc053ec0656fb69f4842c29c35f486fcb.png)  

# examples of capacity-delay
![picture 8](images/68da8ca08022cf5b6e7fc2cf474b77b91473af9120f8b817631f0d786c55a82c.png)  


- packet delay = Transmission delay + propagation delay

![picture 9](images/f043a3f7854821a6c39df00e7fbfef1a5274c47914fae3040c96853b9f6d60b4.png)  

# circuit switching
- time division
  each circuit allocated certain time slots
- frequency division


# circuit switching
- pros
  - guaranteed performance
  - fast transfer (once connection is established)

- cons
  - waste capacity if it is busy
  - connection setup time is overhead
  - when have failures, have to establish connection from scratch.

# packet switching 
- data is sent as chunks of formatted bits(packets)
- packets consist of a header and payload
- switch forward packets based on their headers.
- each packet travels independently
- no link resources are reserved in advance

# statical multiplexing
- pipe view
![picture 10](images/7979568cb17aa3998773317e42cd8405dcd506f144a92b83b6afa61cc92d838f.png)  

- we need some control protocol to ensure queues are stable: TCp


# queues introduce queuing delays
- with queues: queuing delay = rx delay + prop delay + queuing delay
- made worse at high load

packet switching: pros and cons
- cons:
  - guaranteed performance
  - header overhead per packet
  - queues and queuing delays
- pro:
- efficient use of capacity
- no overhead dur to connection setup
- resilient - can route around trouble

# ECE view on bandwidth
1. range of frequencies occupied by the signal travelling on the link

![picture 1](images/4bb9ec79ceade8b7daf649c81aff67c5582b52cf29a317ed06a2362a91d618fe.png) 
if i sample f(t) at sampling frequency a least twice bandwidth then i can recover f(t)(T< pi/Ω) from samples.

- To reconstruct signal from samples what we can do is a low pass filter
![picture 2](images/3a0a08929ca0cb8cee62b6031a2bd784039be21cd79315cdccdde3957b78b53e.png)  

- generate a $\delta$-train using the sampled values
- apply low-pass of cut-off - frequency Ω
- obtain back $f(t)$

## Why?
- Remember that sampling in the time domain corresponds to replicating signal in frequency domain.
![picture 3](images/d4990159ba55afe7612585366092e5ae27039e22e02f9634f83f00c3798b043c.png)  

To get back f(t) from sampled signal, we can apply a filter to eliminate the replicas.

If signal has duration $T_0$ and bandwidth $\Omega$ (means limited), we can reconstruct it using **at least**
![picture 15](images/a784d29e493e77f295951f9026007de350fe8ba5267ce572f84deaa9d533ead8.png)  



Nyquist Number is the minimum number of samples required to reconstruct the signal in the interval.

Transmitting $f(t)$ over time $T_o$ is the same as transmitting $N_0$ real numbers.(samples).
$f(t)$ has a discrete representation in terms of N0 numbers.
It seems that by sampling theorem, transmitting $f(t)$ we achieve a rate of $N_0$/$T_0$ reals/time
![picture 16](images/f3fa7db9a8bfa92d209c86ab3a666189b5456b6d2e2db0577362fdd600fed00a.png)  


## how to go to bits/time
- Question: can real numbers(samples) be arbitrary or are they constrained?

1. we can not have f(T) of arbitrary energy.
![picture 8](images/d18dfc34c43054343813a7af9b950266387bd771ec60fa94404f9fbf806b7915.png)  
![picture 17](images/2be622db42ee985f53b083c8b98cdf1fc8fcd71091f2b35022950ed4f2b64f0a.png)  

Every signal f(t) can be seen as a point (x1,x2,xN0) in a space of $N_o$ dimensions and this point must be inside a ball of radius $PN_0$

1. f(t) can be seen as a point( by sampling theorem)
2. The point must be inside a ball (by energy constraint)

### How many different signals bandlimited and if a given energy I can have?

Noise constraint 
when points are too closed in space their coordinates are also close which means the reconstructed signals look very much.

And because of noise they are undistinguishable.

How many signal we can distinguish if noise has energy $\sqrt{NN_0}$
![picture 18](images/8c7daaee20bba49f3bf49a228b7f83ea01111b9fca61126db3ecf3f2e75b124b.png)  

number of signals that can be distinguished from  noise balls that fit inside space without overlap.
$$M = \frac{Volume \ signal \ ball}{Volume \  noise \ ball} = \frac{P+N}{N_0}$$

if we can transmit a bandlimited signal of finite energy over a noisy of noise energy(NN0) over a time interval T0,then we can have at most $M=(\sqrt{1+P / N})^{N_{0}}$ possibilities.

## how many bits does this physical possibility correspond to?
By transmitting one of the M signals at we are communicating $\log_2M \ bits$

- bit-rate
![picture 9](images/fb6772b055ed4d11852d7e9a5ec7b3a3253cdc8178c9dde63588159296b2d42c.png)  

SNR signal to noise ratio that is average power of received signal / avg power of the noise
$$C=W \log (1+SNR) \frac{bits}{rec}$$
How many distinct signals can I send?
![picture 25](images/4541c2156f8de465e93277e0b84e7e09c1d9958836c376c722e07f7558f6576b.png)  

Transmitting one signal out of the M possible ones corresponds to transmitting
![picture 26](images/556f36deb4ca7177df2652ea96c99367f62bdcc2879e305bca55842d31f860b3.png)  

- Example
![picture 27](images/ba1c04b9f2de5390a167e578468a4da0337fdb5e8060dfadfb35b1936997bace.png)  

assume we send this email over a connection line
7 bits/sec == 1 character per second
![picture 28](images/5d785ce3a65280a2e78a24d59006d33b461c1f1eb8ff2bf6efdca4c345853134.png)  

signal must have enough Frequency band and average power to satisfy condition for a given noise

If instead we want to send 1M characters per second


# queueing delay

- single link : packet delay = tx delay + pro delay
- network packet delay = tx delay + prop delay + queueing delay

## queueing theory
- network we have random packet arrival at intermediate nodes.
- random amount of traffic - **model**

- To design protocols efficiently, we should have an idea of things like
  - How long is a packet queued at intermediate nodes?
  - How large are the queues?

### random arrival process for packets entering the queue

- random service process for packets exiting the queue
- model the arrivals as a poisson process
  - P(n arrivals in interval of time of size T) = $\frac{(\lambda T)^{n}}{n !} e^{-\lambda T}$
  - $\lambda$ = intensity of p.p is a parameter
  - number of arrivals n1,n2 in disjoint intervals of time are independent random variables.

#### why poisson
- it can be shown that poisson formula arises whenever the probability of arrival in a very small interval is proportioned to the site of that interval. 
- How can we simulate an arrival process?
  1. draw a random number n ~ poisson
  2. place them uniformly at random in the inter-arrival time t2-t1 ~ Wxpo($\lambda$)

![picture 29](images/7dc6d64d13dc65d88fa7073c05e67f0e259dfb207fd99a430137ae23d9e5eb4f.png)  

![picture 30](images/d0065ff80256421762d8fb024e1ed8f4f3dbcb9a281a541d4ea6332b18716040.png)  

### properties that are useful in the problems
- merging property

![picture 31](images/84dd2719cd2107a8b2f00c449f48ac56dd3059b4f3094cca7efce09a295c573b.png)  

- splitting  property
![picture 34](images/630db2b77836219c60e8496921bbfb4ea821c3d81f2ae0e6887a4b3a82af4d35.png)  


