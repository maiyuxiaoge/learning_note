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