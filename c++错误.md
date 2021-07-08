## new types may not be defined in a return type
类的定义最后没有加括号

## shared_weak_ptr
裸指针和智能指针混用，对象为栈上分配非堆上


## link error: redefinition:

Make the variables extern in the header file.

extern AClass* variable1;   // assuming AClass is declared at this point.
extern int* variable2;
Define them once and only once in any cpp file e.g. in main.cpp at namespace scope.

AClass* variable1 = NULL;   // assuming AClass is declared at this point.
int* variable2 = NULL;

## shared_ptr to set_allocated_
- oPerson.set_allocated_profile(pProfile.get()); 可能会导致segmentation fault
oPerson.mutable_profile()->CopyFrom(*pProfile);
Or equivalently:

*oPerson.mutable_profile() = *pProfile;

## c++ 开启core dump
ulimit  -c unlimited

# linux 开启交换空间
sudo dd if=/dev/zero of=/swapfile bs=64M count=16

sudo mkswap /swapfile

sudo swapon /swapfile

After compiling, you may wish to

Code:

sudo swapoff /swapfile

sudo rm /swapfile

# git error: RPC failed； result=35, HTTP code = 0 fatal: The remote end hung up unexpectedly
后来，通过设置Git的http缓存大小，解决了这个问题，在当前工程目录下运行如下命令：

git config --global http.postBuffer 20M

如果20M不行就 50M