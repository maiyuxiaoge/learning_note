[toc]
# MVC -- Model View Controller

# Variables
1. MONAD
- The most common type of variable, monads have a single part
- subject to data fundamentals discussed earlier.
- Reflect the underlying type;either intrinsic(int,float...)
- By default, monads are transient, occupying space on the stack.
```c++
int i = 10;
char value = 'a';
```
2. DYAD
- The **LHS** usually lives on the stack,and is of type(address). It contains the memory address of the RHS.
- The RHS is a monad of any type, stored on the heap.
![picture 34](images/b0612aa7a6d85c28067f9139de453a725f13ff3dbd9d148ab4eed98cde625e9c.png)  

3. REFERENCE
4. ENUMS
- c-enums
```c
enum basic {first = 10,second, third}
```
- c++ enums
```c++
class enum improved : char {first = 'a', second = 'b', third = 'c'}
```
5. AUTO
- auto isn't a type in c++, it is a mechanism by which the compiler can auto-detect the associated type.
```c++
int main(){
    auto theValue = 3.14;
}
```

# iteration
1. type1
```cpp
int theInts[] = {100,200,300,400};
const int theCount = std::size(theInts);
for (int i = 0; i < theCount; i++){ std::cout << theInts[i] << "\n";}
//more modern
for (auto theInt: theInts){ std::cout << theInt << "n";}
```
2. type2
```cpp
int theInts[] = {100,200,300,400};
const int theCount = std::size(theInts);
int i = 0;
while (i < theCount){
    std::cout << theInts[i] << "\n";
}
```
3. type3
```cpp
int theInts[] = {100,200,300,400};
const int theCount = std::size(theInts);
int i = 0;
do{
    std::cout << theInts[i] << "\n";
}while(++j < theCount);
```
4. type4
```cpp
void recurse(int aValue,int aMaxinum){
    std::cout << aValue << "\n";
    if (aValue < aMaximum) recurse(aValue + 1,aMaxinum);
}
int main(){
    recurse(0,10);
}
```
5. type5
```c++
#include<algorithm>
void printInt(int aValue){std::cout << aValue << "\n";}

int main(){
    int theInts[] = {100,200,300,400};
    const int theCount = std::size(theInts);
    std::for_each(theInts,theInts + theCount,printInt);
}
```

# making a class in cpp
- your class must provide a default constructor
- every class needs to implement the methods specified in the orthodox canonical form
```cpp
class Foo{
    public:
        Foo();
        Foo(const Foo &aCopy);
        ~Foo();
        Foo& operator=(const Foo &aCopy);
    protected:
        int value;
        std::string str;
}

Foo::Foo():value(0),str(""){};
Foo::Foo(const Foo &aCopy){*this = aCopy;}
~Foo(){};
Foo& Foo::operator=(const Foo &aCopy){
    value = aCopy.value;
    str = aCopy.str;
}
```

## orthodox canonical form
```cpp
class Foo{
    Foo();
    Foo(const Foo &aCopy);
    ~Foo();
    Foo& operator=(const Foo &aCopy);
}
```

# polymorphism
 1. compile-time
   ```c++
   int max(int arg1,int arg2){return arg1<arg2? arg2:arg1;}
   float max(float arg1,float arg2){return arg1<arg2? arg2:arg1;}
   int main(){
       float f1{3.14};
       float f2{6.28};
       float f3 = max(f1,f2);
   }
   ```
 2. run-time
 ```cpp
 struct Foo{
     virtual void doSomething(){
         cout << "i am a foo";
     }
 }
  struct Bar{
     virtual void doSomething(){
         cout << "i am a Bar";
     }
 }
 int main(){
     Foo* theFoo = new Bar;
     theFoo -> doSomething();
 }
 ```
 3. run-time with custom dispatch
 4. fully-dynamic


# operator overloading
1. Arithmetic $\left(+,,{ }^{\star}, l, \% \ldots\right)$
2. Comparison $(<,>,==, \ldots$
3. Logical (!, $\& \&, \| \ldots)$
4. Bitwise $(!, \&, \mid,<<,>>)$
5. Assignment $\left(=,+=,-=,{ }^{\star}=, /=\ldots\right)$
6. Member and pointer $\left(^{\star}, \rightarrow, \&\right)$
7. Index of $\square$
8. Function call ()
9. Memory management (new, delete...)
10. Type conversion operators

## conversion operators
- a conversion operator works in an opposite manner from a conversion constructor. The goal of conversion operators is to allow an object of class A to convert itself to another type

```cpp
class Foo{};
class Bar{
    public:
        Bar();
        Bar(const Bar &aCopy);
        ~Bar();

        operator Foo(){
            return Foo();
        }
};
```

# memory management
- C: alloc,malloc,realloc,free
- C++: new,delete
```cpp
char *theBuffer = new char[100]{0};
delete [] theBuffer;
struct Foo{};
Foo* theFoo = new Foo;
delete theFoo;
```

# type - casts
## in C
- problem: the comiler will blindly try to do what you are asking,even if it does't make sense.
```c
int main(){
    int theValue{12345};
    float theFloat = (float)theValue;
    const char* theString = (char*) theFloat;
}
```
## in cpp
- static_cast: a type-safe version of type-casting
```cpp
struct A{};
struct B{};
struct C: public A{};
int main(){
    A* theA = new A;
    B* theB = new B;
    C* theC = new C;
    theA = static_cast<A*>(theC); // ok
    theA = static_cast<B*>(theB);//will not compile
}

```

- const_cast is used to remove the const-ness of a variable.

```cpp
int main(){
    char theBuffer[1000] = {'h','e','l','l','o','\n'};
    const char* thePtr = &theBuffer; // prevent change to buffer(const char*)
    char* thePtr2 = const_cast<char*>(thePtr);
    stycpy(thePtr2,"what's up");
}
```

# templates
- allow us to write code that is type-independent
## template functions
```cpp
template<typename T>
void swap(T &arg1,T &arg2){
    T temp = arg1;
    arg1 = arg2;
    arg2 = temp;
}

int main(){
    swap<int>(theInt1,theInt2);
}
```

## template methods
```cpp
class Foo{
    Foo(){};
    void swap(T &arg1, T &arg2){};
};
int main(){
    Foo theFoo;
    theFool.swap(theInt1,theInt2);
}
```
## template class

# functor
- without functor
```cpp
int value = 0;
int add(int i){
    value += i;
}
int main(){
    int theInts[10] = {1,2,3,4,5,6,7,8,9,0};
    for (int theInt: theInts){
        add(theInt);
        cout << value << endl;
    }
}
```
- using functor
```cpp
struct Functor{
    Functor(int aValue):value(aValue){};
    Functor(const Functor &aCopy){};
    Functor& operator=();

    int operate()(int aDelta){
        value += aDelta;
        return value;
    }
    int getValue(){return value};
protected:
    int value;
}

int main(){
    Functor theFunctor;
    int theInts[10] = {1,2,3,4,5,6,7,8,9,0};
    for (int theInt: theInts){
        theFunctor(theInt);
    }
    cout << theFunctor.getValue() << endl;
}
```
# RAII
- resource acquisition is initialization
- 利用c++构造的对象最终会被销毁的原则
- RAII的做法是使用一个对象，在其构造时获取对应的资源，在对象生命期内控制对资源的访问，使之始终保持有效，最后在对象析构的时候，释放构造时获取的资源
- 理解： 在destructor 中释放资源 如 fd.close(), delete p

```cpp
class BufferManager{
public:
    BufferManager(size_t aPreSize = 0){
        if (aPreSize) buffer = new char[aPreSize];

    }
    ~BufferManager(){delete buffer;}
}
```

# efficiency
1. time efficiency
2. space efficiency
3. cognitive efficiency
4. testing efficiency

# partial template specialization
- 部分模板特化
## 问题提出：
- 实现json的写入

## 解决方法一：
```cpp
class Foo{
    Foo& toJSON(std:stream &anOutput){
        anOutput << "id" << "\"" << ":" << id << "\n";
        anOutput << "amount" << "\"" << ":" << amount << "\n";
        anOutput << "name" << "\"" << ":" << name << "\n";
    }
}

```

## 解决方法二：
```cpp
class JSONWriter{
    public:
    JSONWriter& writeInt(const int &aValue);
    JSONWriter& writeFloat(const float &aValue);
    JSONWriter& writeBool(const bool &aValue);
    JSONWriter& writeString(const std::string &aValue);
}
```

## 解决方法三：
```cpp
class JSONWriter{
    public:
    JSONWriter& writeKeyValue(const std::string &aValue,aKey,const int &aValue);
    JSONWriter& writeKeyValue(const std::string &aValue,aKey,const float &aValue);
    JSONWriter& writeKeyValue(const std::string &aValue,aKey,const bool &aValue);
    JSONWriter& writeKeyValue(const std::string &aValue,aKey,const std::string &aValue);
}
```

## 解决方法四：
```cpp
class JSONWriter{
    public:
    template<typename T>
    JSONWriter& writeKeyValue(const std::string &aValue,aKey,const T &aValue);

    template<>
    JSONWriter& writeKeyValue(const std::string &aValue,aKey,const bool &aValue);

    template<>
    JSONWriter& writeKeyValue(const std::string &aValue,aKey,const std::string &aValue);
    private:
    std::stream &output;
}
```

#  friend
- 友元函数和友元类
- 友元函数内部可以访问该类对象的私有成员
```cpp
class CCar;  
class CDriver
{
public:
    void ModifyCar(CCar* pCar);  //改装汽车
};
class CCar
{
private:
    int price;
    friend int MostExpensiveCar(CCar cars[], int total);  
    friend void CDriver::ModifyCar(CCar* pCar);  
};
```

- 友元类的所有成员函数都可以访问对方对象的私有成员
```cpp
class CCar
{
private:
    int price;
    friend class CDriver;  
};
class CDriver
{
public:
    CCar myCar;
    void ModifyCar()  
    {
        myCar.price += 1000;  
    }
};

```

# CRTP (奇异的递归模板模式)
1. 继承自模板类。
2. 派生类将自身作为参数传给模板类

```cpp
template <typename T>
class Base
{
public:
    void doSomething()
    {
        T& derived = static_cast<T&>(*this);
    }
};

class Derived : public Base<Derived>
{
public:
    void doSomething()
    {
         std::cout << " Derived class " << std::endl;
    }  
};
```

- 作用： 
  - 通过static_cast 把基类转化为派生类，实现基类对象对派生对象的访问
  - 多态是个很好的特性，但是动态绑定比较慢，因为要查虚函数表。而使用 CRTP，完全消除了动态绑定，降低了继承带来的虚函数表查询开销。
  - 具体应用： https://zhuanlan.zhihu.com/p/137879448

# mixin
- Template Parameters as Base Classes
## 问题提出
```
class DerivePrint1 : public BasePrint
{
public :
    virtual void myprint() {
        cout<<"Hello World 1!"<<endl;
    }
    virtual void print() {
        myprint();
    }
};

class DerivePrint2 : public BasePrint
{
public :
    virtual void myprint() {
        cout<<"Hello World 2!"<<endl;
    }
    virtual void print() {
        myprint();
    }
};

class myClass:public DerivePrint1,public DerivePrint2{
};

int main()
{
    myClass my;
    // error，触发了多重继承的问题
    my.print();
}
```
- print 定义不清晰

## mixin解决方法
```
template <typename T>
class DerivePrint1 : public T
{
public :
    void print() {
        cout<<"Hello World 1!"<<endl;
        T::print();
    }
};

template <typename T>
class DerivePrint2 : public T
{
public :
    void print() {
        cout<<"Hello World 2!"<<endl;
        T::print();
    }
};

class myClass{
public:
    void print(){
        cout<<"myClass"<<endl;
    }
};

```
# code smell
1. Bloaters: over-engineering
   1. overly long method
   2. excessively long argument lists
   3. over-engineered primitives
2. oop abuse
   1. unnecessary switch statements
   2. poorly factored methods
   3. temporary fields
   4. poor inheritance design
   5. class alternatives with varying interfaces
3. ice-age
   1. change preventers are practices is make changing code more difficult,time-consuming or expense.
4. dispensables
   1. lazy classes
   2. duplicate code
   3. dead code
5. anti-social network
   1. unnecessary coupling or dependencies
   2. middle man
   3. message chains
   4. overly dependent hierarchies


- 参考资料： https://refactoring.guru/refactoring/smells