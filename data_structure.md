[toc]
# Java v.s c++
## string
### java
- immutable
- s.substring(beginIndex,endIndex)
- can concatenate any type

### c++
- mutable
- can only concatenate string
- s.substr(beginIndex,length)

## compare
### java
- a.equals(b)
- a.compareTo(b)

### c++
- a == b
- a != b
- a < b
- a > b


## variable

### java
- variable initialization is checked
```java
int fast;
int furious;
int fastFurious = fast + furious; //compile error
```
- narrowing is checked
```java
int x = 40000;
short y = x; //compile error
```
- variables cannot be declared outside of a class
```java
int x = 4;
class MyClass(){

} //compile error
```
### c++
- variable initialization is not checked
``` c++
int fast;
int furious;
int fastFurious = fast + furious; // undefined error
```
- narrowing is not checked
``` c++
int x = 40000;
short y = x; //overflow
```
- variables can be declared outside of a class
```c++
int x = 4; //global variable
class MyClass(){

} //right
```

## classes,source code, headers
### java
```java
class Student{
    public static int numStudents = 0;
    private String name;
    public Student(String n){};
    public void setName(String n){}; // must implement method
    public String getName(){};
}

```

### c++
```c++
class Student{
    public:
        static int numStudents;
        Student(string);
        void setName(string n);
        string getName() const;
    private:
        string name;        
}; // just declaration
int Student::numStudents = 0;
Student::Student(string n){};
void Student:: setName(string n){};
string Student::getName() const{};
```

### c++ member Initializer list
```c++
class Point{
    private:
        int x;
        int y;
    public:
        Point(int i, int j);
};
Point::Point(int i,int j){
    x = i;
    y = j;
};

class Point{
    private:
        int x;
        int y;
    public:
        Point(int i, int j);
};
Point::Point(int i,int j): x(i),y(j){};
```

### source file vs header files
```c++
// student.h
class Student{
    public:
        static int numStudents;
        Student(string);
        void setName(string n);
        string getName() const;
    private:
        string name;        
}; 

//student.cpp
int Student::numStudents = 0;
Student::Student(string n){};
void Student:: setName(string n){};
string Student::getName() const{};
```


## c++ memory diagrams
![picture 2](images/a6ca4ef8f769da73575a4ca5a5cfe12aa4fd04fcdcef184729789c9a229603b1.png)  

### reference
![picture 3](images/bddddc1c726f133275389b1653eec727be65826b052958d5d289c26a3a7d47cf.png)  

### pointers
#### c++
![picture 4](images/efa52011526779449fe7b0b210579970276d33ebc3ddd2f82eb7cf51cc553dc9.png)  

#### java
![picture 5](images/04608229769c4b3054206f650d038e63d9f00b4948ac669d5e831f0ac892ffe1.png)  


## the const keyword
```c++
const int s = 42;
s = 32; // compile error
int const a = 42;
a = 4; // compile error


int a = 42;
const int * ptr1 = &a;
int const* ptr2 = &a;
*ptr1 = 1; // error
*ptr2 = 1; //error

int * const ptr3 = &a;
ptr3 = &b; //error

const int* const ptr4 = &a;
ptr4 = &b; // error
*ptr4 = 1; //error


int a = 42;
const int & ref1 = a;
ref1 = 20;// error
int const &ref2 = a;
ref2 = 20; //error

class Student{
    public:
        static int numStudents;
        Student(string);
        void setName(string n);
        string getName() const;  // cannot modify by object, cannot assign instance var, can only call other const function
    private:
        string name;        
}; 

//student.cpp
int Student::numStudents = 0;
Student::Student(string n){};
void Student:: setName(string n){};
string Student::getName() const{};
```

## c++ functions
```c++
int main(){}; // must be int

```

### pass by value vs pass by reference
```c++
void swap1(int a,int b){
    int temp = a;
    a = b;
    b = temp;
}
swap1(a,b);// a,b not changed
void swap2(int & a,int & b){
    int temp = a;
    a = b;
    b = temp;
}
swap2(a,b);// a,b changed
```

## c++ vectors
```c++
vector<int> a;
a.push_back(42);
a.push_back(21);
a.pop_back(33);
std::cout << a[0] << std::endl;

vector<int> b = a; // full copy of a
```

## c++ input /output

```c++
int n;
cout << "Enter a number";
cin >> n;

string message;
cout << "Enter a message";
getline(cin,message);

if (cin.fail()){
    cerr<< "Bad input!" << endl;
}
```

## c++ template
```java
class Node<Data>{
    public final Data data;
    public Node(Data d){
        data = d;
    }
}
Node<String> a = new Node<String>(s);
Node<Integer> b = new Node<Integer>(n);
```

```c++
template<typename Data>
class Node{
    public:
        Data const data;
        Node(const Data &d): data(d) {};
};
Node<string> a(s);
Node<int> b(n);
```

# c++ iterators
## motivation for iterators
```c++
for (string name:names){
    cout << name << endl;
}
```

## iterators over arrays
![picture 6](images/adf5525748e6934ece93120365b569524a71786d88194b705b0511138022a8d7.png)  


## using iterators
![picture 7](images/ba31fd6b12340c7af8b36071064d834e12862841950a004c653745f643fe8a8d.png)  

## creating an iterator class
### operators in the iterator class
- == true if iterators are pointing to the same item
- != false
- * return a reference to the current data value
- ++(pre) and --(post) move current iterator to the next item

### functions in the data structure classes:
- begin() returns iterator to **the first** element
- end()  returns iterator to **just after** the last element

# time complexity
## notation of complexity

- big-O: upper bound
- big Ω: lower bound
- big θ: both upper bound and lower bound


## finding big-o time complexity
1. determine f(n)
2. drop all lower terms of n
3. drop constant coefficient

## common big-o time complexity
### polynomial
- o(1) - constant
- o(logn) -- logarithmic
- o(n) -- linear
- o(nlogn)
- o(n2) -- quadratic
- o(n3) -- cubic

### bad
- o(k^n) exponential
- o(n!) Factorial

# space complexity


# Trees
## what are trees
- no undirected cycles
- connected
  
## special cases of trees
- empty (null)
  - 0 nodes
  - 0 edges
- single node tree
  - 1 node 
  - 0 edges

- rooted trees
  - only one root node(no parent)

- unrooted trees

- leaves : 1 neighbor
- internal nodes: multiple neighbors
- root: no parent

## tree traversal
### dfs
- preorder:visit,left,right
- inorder:left,visit,right
- postorder: left,right,visit

### bfs
- levelorder: 1st level(left to right), 2en level

## properties of a binary search tree(BST)
1. rooted binary tree
2. every node is larger than all nodes in its left subtree
3. every node is smaller than all nodes in its right subtree

## bst find algorithm
1. start at the root
2. if query == current: success
3. otherwise, traverse the left/right
4. no such child: fail

## bst insert algorithm
1. perform find algorithm
2. if find: duplicate
3. insert the new element at the site of failure

## bst successor: next largest node
1) if the node has a right child,traverse right once, then all the way left
2) other wise, traverse up the tree. The first time the current node is its parent's left child ,the parent is our successor

## bst remove algorithm
- no children: just delete the node
- one child: direct my child to my parent
- thw children: replace my value with my successor,and remove me.

## bst time complexity
- height of a node: the longest distance from node to a leaf
- height of a tree: Height of  the root of the tree 
- depth of a node: number of nodes in the path from that node to the root
## tree balance
### best vs worst vs average case
- best: query is the root O(1)
- worst perfectly unbalanced,query not found O(n)
- average case:
  - Theoretical expected value over all  trees and queries
  - all n elements are equally likely to be searched for.
  - all n! possible insertion orders are equally likely 


# treaps tree + heap
- bst properties wrt keys
  - larger than all keys in the left subtree
  - smaller than all keys in right subtree
- heap property wrt priorities
  - larger than all priorities below

![picture 1](images/7622651ed0b02e8769359279726d057f12cf980ca19d291be6dfabe58585461e.png)  

# AVL rotations
![picture 2](images/c51cb41fc098546cc29fb71274f449d5246327c20298f65ef1a215335064da6d.png)  


# treap insertion
1. insert via BST insert algorithm
2. use AVL rotation to bubble up to fix Heap wrt priorities


Randomized search tree
- user elements as keys (maintain bst)
- random generate priorities (maintain heap property)

# AVL trees
- balance factor BF: height of right subtree - height of left subtree
- avl tree: in which every node has BF of -1,0,or 1

# AVL tree insertion
1. regular BST insertion
2. update balance factor
3. fix broken balance factor using AVL rotation


# red-black trees
1. all nodes must be red or black
2. the root must be black
3. if a node is red,all of its children must be black.
4. for every node u, every possible path from u to a null reference must have the same munber of black nodes
5. null reference are black

# red-black tree vs avl tree
- red-black tree is not necessarily an avl tree

# the set adt
- set: store multiple elements
- find,insert,remove

# the map adt
- map: store multiple pairs
- get,put,remove

# implementing the set and map adts
- unsorted linked list
- sorted linked list
- unsorted arraylist
- sorted arraylist
- slef-balancing BST:
- Hash table


# tries
- trie: Tree structure in wich elements are represented by  paths
- a four path trie
![picture 1](images/9769ec850f0ee9003373fa1768d3accc555f3b5bce7e47171864b5a8202d9888.png)  

# multiway tries
- trie in which nodes can have more than 2 children

## mwt time complexity
- n : number of words
- k : length of longest word
- O(n*k)


## mwt space complexity
- ![picture 2](images/f654c20cbf35405c5eaf5fbaeebc033ba80a9e9415e5ce7b327a1b2803494b96.png)  

- $\Sigma$ = alphabet
- $|\Sigma|$ = length of alphabet
- O($n^k$)


# ternary search trees (TSTs)
-  BST:O(klogn),memory efficient
-  MWT:O(k), memory inefficient
-  TST: somewhere in between
![picture 3](images/bd837f80f2168f8b3dbcb2b70f500f2affbb24b39e6d116032d31016e26f7e41.png)  
![picture 4](images/dcb3fd26d4d66297d3d2823ed19ca4bac89b56a3b2753ad7aca6802f621d51b7.png)  


## tst time complexity
- worst O(n)
- average O(logn)

# hash function
- input : an object x
- output: an integer representation of x
- property of equality: if x is equal ot y,h(x) must be the same
- property of inequality: if x is not equal to y, it would be nice if h(x) is not equal to h(y)

## examples:
```python
def h(s): //valid not good
    return 0
def h(s): //valid
    out = 0
    for c in s:
    out += ascii value of c
    return out

def h(s): //invalid
    return a random integer

def h(s): //valid,best
    out = 0
    for c in s:
        out *= 31
        out += ascii value of c
    return out
def h(s): // invalid
    return current time
```

$P_{N, M}(\geq 1 collision) =
1-P_{N, m}(0$ collisions $) = 
1- 1 \cdot \frac{m-1}{m} \cdot \frac{m-2}{m} \cdot \cdots \frac{m-N+1}{m}
$

## load factor
expected total number of collisions:$\sum_{i=1}^{N-1} \frac{i}{n}=\frac{N(N-1)}{2 m} = 1$  
-> $N=\sqrt{2 m}$

$M=O\left(N^{2}\right)$

expected total number of collisions $=\frac{1}{2}\left(1+\frac{1}{1-\alpha}\right)$

# collision resolution strategies
## open addressing(linear probing)
![picture 1](images/7699ce77b6201366261a901694a0931e605f8ac4daab05570de227dd16af3cad.png)  

## double hashing
![picture 2](images/79fc8de4dd1f78707dc3d337eb1d2719a1e919c714b21ffcffaa7d3ae45b6d27.png)  


## closed addressing(separate chaining)
![picture 4](images/2b9671fc7d1663cc016e1af368b7b9a43e9fe5ddf24ce7a81800a10b6dad7233.png)  


# bloom filters and count-min sketches
## bloom filters
![picture 3](images/7ec10c39f37ff0e7f5cc47c0d8591e96c97df5f5963871231f2e64bd13396b52.png)  


## designing an optimal bloom filter
1. each hash function uniformly distributed
2. each insertion is independent

![picture 5](images/8178e01e0b5e2f0a59ddc984919055d7ece00be9289df227f8ffd884afc48e66.png)  
![picture 6](images/800ce960bb8eed0ef60cd031084ea0ca16352f3330bcd6c5975be30ef24d0d28.png)  


## count-min sketches
- probabilistic data
- memory-efficient
- provides upper-bound on counts

![picture 7](images/37ba10709cc2312e97b5d002d41563b8948bd342290a29a1b6b7b32d7ad15c6e.png)  

## design an optimal count-min sketch
![picture 8](images/87c6a78f43bb85d909b9a35afd1e0960b90c34bc47963d4d681bd679ec466536.png)  

# Aho-Corasick Automaton
## matching a database of many short strings to a long query string
![picture 2](images/4dd524ac7d27f20ef4e8aa5f0778e37ff7b14a510a082cc8d3cd0f9b03a005a7.png)  

## aho-corasick automaton
![picture 3](images/69d3c441c7902114e8078be9a92b344641b967ee4225e07d0d1f8f72de0c446a.png)  

## dictionary link
![picture 4](images/14c4ed1589017c4bd19b4e7fe9c33727ec4eb15def2f385be21dfd3e343ba23c.png)  

# suffix arrays and burrows-wheeler transform(BWT)
## suffix arrays
![picture 5](images/29132374d4d7a408b1aa9d1525e79e49939e8d5dfdbfe530645eba0c6a6dd0cb.png)  


## suffix array search
![picture 6](images/33e8ea918ed45b1d118826f1a32260bafa5517d7b07d541db5965db1a8ddeb66.png)  

- O(klogn)

## burrows wheeler tranform
![picture 7](images/0794cea7cce83939e79853725fa54e5df276d4389cb42537c1abab14920b83a2.png)  

## inverting the bwt
![picture 8](images/ff0c66d12f7fe56b2367b830ab424234f8ce5e8a100e7d98d80cb7916ed5ee0f.png)  


## pattern matching usring the BWT
![picture 10](images/8dbb5de9f24f77d1837e76eb169e3ead3d9db088de07602ea8e9cb6caa015120.png)  


# Message encoding
## Coding Tree
![picture 1](images/87fc9f5eeebdc9cce4c477aa5f7d4430affd6ad7687dadea1735df7c32db9862.png)  

## information vs. data
- information: content of some message
  - tells us details about some system
- data: raw unit of information
  - representation of information

## entropy
- entropy: measure of disorder(non-uniformity) of a system
- Shannon entropy: expected value(average) of the information contained in some data


## data uniformity and information
- uniformity: lack of variation among symbols in a message

- more uniform -> less entropy -> less information

# Huffman coding
## prefix code
- an encoding in which no symbol is represented by a code that is a prefix of the code representing another symbol

![picture 1](images/7aaef0606bb635407ca5128294e4c33df89384ab0e138673cfb9d211ba201bbc.png)  

## a lower bound on data compression
$$\sum_{x} P_{x} \log _{2}\left(\frac{1}{x}\right)$$

![picture 2](images/af1ddeb26cb24af8220dea5612d18aa3cb2086c6729b80aa8522dedf84ab6d25.png)  

## huffman tree construction
1. compute frequencies of symbols in message
2. start with a forest of single-node trees(symbol w/frequency)
3. while there is more than one tree in the forest
   1. remove 2 trees with lowest frequency from forest
   2. create new node with frequency = t1's frequency + t2' frequency to be their parent
   3. insert this new node into the forest

## huffman encoding& decoding
![picture 3](images/612764aa8ef8680011153cebc29a39c060fb34b0cb4f31fc908adaca0c728406.png)  

# bitwise input/output(I/O)
## bytewise(I/O)
![picture 4](images/1937be58e58cfaad342820b388ef6dd60f0d709d65a6e881fafc9055d6bd38b5.png)  
## bitwise I/O
![picture 5](images/4c27fe9f4b8b2965874b73747e5242cb757d0a4487c8cddb1ac939cec36ebdf4.png)  

## reading from a bitwise buffer
![picture 6](images/1d726a9539906f5c1617308e6d15a9da58dffddf9d6bd8169d6762dd6c54d346.png)  


## writing to a bitwise buffer
![picture 7](images/121aa3f4fd4305a17665b3b81c85e18bc45d93fce26ad20c6802b7f8744a4804.png)  

# graphs
## directed vs undirected
- directed: an edge(u,v) is from u to v, not v to u
- undirected: an edge(u,v) is from u to v and v to u
## weighted vs unweighted

## cycles
- a valid path starting and ending at the same node
  
## classes of graphs
- structured: a disconnected collection of nodes
- sequential: an ordered collection of connected nodes
- hierarchical: a ranked collection of connected nodes
- structured: a collection of both connected and disconnected nodes

## multigraphs
- multigraphs: graph in which a pair of nodes may have multiple distinct edges


# graph representation
## adjacency matrix
![picture 1](images/7cca38e0da41ede6b3f90e5f903501080ce02cebd045f9f6c5a3c77993ff569d.png)  

## adjecency list
![picture 2](images/79d6feb9187c5669d31fbf067b69172db916bffff3603611868ecd32ac63c17d.png)  


# breadth first search(BFS)
![picture 3](images/b4bfa0e7ec46b63d37a8c8be876622546266e338127a4164b04d5f9f9a8c4369.png)  


# depth first search(DFS)
![picture 4](images/6cacba97059eedf6be7e1effda09dc1175c2c8440203585307457534caff75d9.png)  

# bfs and dfs time complexity
![picture 5](images/bbc7c1b2f7eb491bd290da023813312b1f72a932daf1d016f27bb0dbfdc369ee.png)  


# dijkstra's algorithm
![picture 6](images/5f7152f1da7e34fb37f174ebbeaa0911e67fa5d1a4d288bc545b4368a08f08f4.png)  

# dijkstra's algorithm time complexity
![picture 7](images/4e21139e165f0e454448303a1c5ce4eb52dff96b8c5d52bd501e34543ae5a8b5.png)  


#