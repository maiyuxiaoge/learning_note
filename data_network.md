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
1. of frequencies occupied by the signal travelling on 

![picture 1](images/4bb9ec79ceade8b7daf649c81aff67c5582b52cf29a317ed06a2362a91d618fe.png) 
if i sample f(t) at sampling frequency a least twice bandwidth then i can recover f(t)(T< pi/Ω>) from samples.

- To reconstruct signal from samples what we can do is a low pass filter
![picture 2](images/3a0a08929ca0cb8cee62b6031a2bd784039be21cd79315cdccdde3957b78b53e.png)  

- generate a delta-train using the sampled values
- apply low-pass of cut-off - frequency Ω
- obtain back f(t)

## Why?
- Remember that sampling in the time domain corresponds to replicating signal in frequency domain.
![picture 3](images/d4990159ba55afe7612585366092e5ae27039e22e02f9634f83f00c3798b043c.png)  

To get back f(t) from sampled signal, we can apply a filter to eliminate the replicas.

If signal has duration T0 and bandwidth Ω (means limited), we can reconstruct it using **at least**
![picture 4](images/19d4ab99d6258927c92e928bf26b62ea807c8d10a5abbb02c0bf02bc202fce10.png)  


Nyquist Number is the minimum number of samples required to reconstruct the signal in the interval.

Transmitting f(t) over time To is the same as transmitting N0 real numbers.
f(t) has a discrete representation in terms of N0 numbers.
It seems that by  sampling theorem, transmitting f(t) we achieve a rate of N0/T0 reals/time
![picture 5](images/9ffafec5e51ec9ae0e06757701212838ec2eb575d35187c816350ca182930803.png)  

## how to go to bits/time
- Question: can real numbers be arbitery or are the y constrained?

1. we can not have f(T) of arbitary energy.
![picture 8](images/d18dfc34c43054343813a7af9b950266387bd771ec60fa94404f9fbf806b7915.png)  

Noise constraint 
when points are too closed in space their coordinates are also cloes which means the reconstructed signals look very much.

And because of noise they are undistinguishable.

How many signal we can distinguish if noise has energy $\sqrt{NN0}$

number of sigals that can be distinguished from  noise balls that fit inside space without overlap.
$$M = \frac{Volume signal ball}{Volume noise ball} = \frac{P+N}{N0}$$

if we can transmit a bandlimited signal of finite energy over a noisy of noise energy(NN0) over a time interval T0,then we can have at most $M=(\sqrt{1+P / N})^{N_{0}}$ possibilities.

## how many bits does this physical possibility correspond to?
By transmitting one of the M signals at we are communicating $\log2M bits$

- bit-rate
![picture 9](images/fb6772b055ed4d11852d7e9a5ec7b3a3253cdc8178c9dde63588159296b2d42c.png)  

