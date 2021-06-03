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
