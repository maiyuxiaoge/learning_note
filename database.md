# application view of  a relational database 

- persistent data structure
  - large volume of data
  - independent from processes using the data

- Transaction management(ACID)
  - Atomicity: all or none happens,despite failure,errors
  - concurrency
  - isolation: one at a time
  - durability: recovery from failures and errors

# data  structure: relation model
- relational databases
- scheme
  - collection of tables
  - each table has a set of attributes
  - no repeating relation names, no repeating attributes in one table
- data
  - set of tuples
  - tuples have one value for each attribute of the table they belong

# primary keys and foreign keys
- primary key:unique

# programming interface
- jdbc/odbc

# SQL language
- selection $\sigma$: select tuples that satisfy the condition
- projection $\pi$ : return a table that only has the attribute
  - set version: no duplicate tuples
  - bag version: allow duplicates
- cartesian product $x$: the schema of the result has all attributes of both R and S

## duplicates and nulls
- Duplicate eliminationmust be explicitly requested (distinct)
- nulls:all aggregation operations, except count, ignore NULL values


# hardware & physical organization
![picture 1](images/5a046a181c3f393886607bed18958933d4a9b111b538decfd269a0e4e69ab641.png)  

# memory hierarchy
- cache hierarchy
- ran
- disk
- tertiary storage

# volatile vs non-volatile
- persistence important for transaction atomicity and durability

# peculiarities of storage mediums affect algorithm choice

- block-based access
- how many blocks were accessed not how many objects
- Flash is different on reading Vs writing
- Accessing consecutive blocks costs less

- moore 's law:
- all improves, but at different speed
- dis transfer rate improves a lot
- disk access time improves less

# 2-phase merge sort: an algorithm tuned for blocks
- when considering block based storage,  algorithm we have learned may not always be the best.

![picture 1](images/d510e6b6e1d94a8fc6c527cd996a76e3b3b481dd85e9fc63f60a43d6e601a3ca.png)  

![picture 2](images/9312554501ec6d37e87659bb22352c4f6a320889e2bd3ebd3a9176f3c99c3fa9.png)  

![picture 3](images/f8ff19ea30813220be9cca7b8ddf413f4065aa8da65748bab1b0b8e944d94dc9.png)  

# 2- phase merge sort : most files can be sorted in just two passes.
![picture 4](images/1b10415f3e20bd421e97123c0296a9de0ed9dacfe14be65fc7a3ef835622f7e3.png)  

# the records are packed row-oriented 
- pack each block with maximum number of records
- do not reclaim deleted records:
  - when delete one record, just leave the space marked blank, not moving every record behind to the front
- utilize overflow blocks for insertion with out of order primary key
- ![picture 5](images/fe4bedc7b2594507f25df77996a5873a3bb8d45a9baddce7a8c0e265030d5ebb.png) 
  - ![picture 6](images/78ee770bdd819bdacf561e2108981e77c862dc28a16255cce244921716c4702d.png)  
- a novel generation of databases features column storage
  - benefits when we only need to focus on a few columns of the records

# indexing 
## definition
- Data structure used for quickly locating tuples that meet a specific type fo condition

## evaluation
- access time
- insertion time
- deletion time
- disk space needed

# conventional index
## terms and distinctions
- primary index
  -  the index on the attribute that determines the sequencing of the table
-  secondary index
   -  index on any other attribute
-  dense index
   -  every value of the indexed attribute appears in the index
-  sparse index
   -  many values do not appear

## dense and sparse primary indexes
![picture 10](images/c07b39347fd00fcb689045749cdff49a6888b07fafb80250c581874591e2a44a.png)  

## sparse vs dense tradeoff
- sparse: Less index space per record can keep more of index in memory,better for insertions
- dense: Can tell if any record exists without accessing file,needed for secondary indexes

## multi-level indexes
- treat the index as a file and build an index on it
- two levels are usually sufficient.More than three levels are rare.
- Can we build a dense second level index for a dense index?

## a note on pointers
- record pointers consist of block pointer and position of record in the block
- Using the block pointer only, saves space at no extra disk accesses cost
- But a block pointer cannot serve as record identifier



## representation of duplicate values in primary indexes.
![picture 19](images/4543f3b5bf334b4881d029cd3749d1c9569e7beb2dbc244af1ca83e91e89e785.png)  
## deletion from dense index
- deletion from dense primary index file with no duplicate values is handled in the same way with deletion from a sequential file
![picture 20](images/1e6d3b3df4e6424d7f2cc888699fc210f31ba088a370ed6b67a5e3eb40bf479c.png)  

## deletion from sparse index
- if the deleted entry does not appear in the index do nothing.
![picture 21](images/e5d0106976e61288f9d042f62280a36a52444db209a30b924305b9a763bcc83a.png)  

- if the deleted entry appears in the index replace it with the next search-key value

![picture 22](images/ead5b3b49ae41b57a124fd879f3fccf770556669a670a5457e3d045fc9ec4e44.png)  

- unless the next search key value has its own index entry. In this case delete the entry
![picture 1](images/b7a05254f5cbda1fc4dd4be4070fda1eae851fd5447a1c7b1b386775c6f2c48c.png)  

## insertion in sparse index
- if no new block is created then do nothing
![picture 23](images/0c1cb660ec920ac3adfae3decd06f99dfe02ec23872842bf0f9e392c0ee97f6f.png)  
- else create overflow record
![picture 24](images/167136310a536fc2aeb15a15a232d42664a0ad9eccd32f6b56be03c5e69504c5.png)  

## secondary indexes
- file not sorted on secondary search key
- First level has to be dense,
next levels are sparse (as usual)
![picture 2](images/aefb5816ab4617c3cdf9bfe34559fbc80bfe4d442cb9f438f5fe89dc0e498873.png)  

## duplicate values & secondary indexes
- one option
![picture 3](images/093f8528c6579b2484470ef0623ec39023cf5d9ec56bfab3768afccee935d2d3.png)  

- another option: lists of pointers
![picture 4](images/a743cbf7faef206322d17c4671919e4d70380bffd70bf670dcee0d1305a55b37.png)  

- yet another idea: chain records with same key
![picture 5](images/371af8a857586353fa8df10e43e95a87a89b1b130cd97927d33edc21571193b9.png)  

## why bucket + record pointers is useful
- enables the processing of queries working with pointers only
- very common technique in information retrieval

## advantage of buckets: processing queries using pointers only
![picture 12](images/711d469c709f65d412a622caae8c9c28f3bd74aadc3e366ffaa3f018af5f96f8.png)  

## summary of conventional index
- Advantages
  - simple algorithms
  - index is sequential file
- Disadvantages
  - eventually sequentiality is lost because of overflows, reorganizations are needed

# b+ tree - another kind of index
![picture 13](images/4e104373c0e02a5eb0d6b0d500a0c5ae230e6ed76d12dfe42906386100b544df.png)  

- sample of non-leaf node

![picture 14](images/0021a23743b571f54c918ac765b23ed57735c6a9c63d0f7cacd356192cf15b42.png)  
- sample of leaf node

![picture 6](images/bfb7c933ea32b334ddb98c619cca28373b0db425f9ee08603fbeee0b0bd29739.png)  

- another kind of notation

![picture 7](images/c289d1175b8df4571e9f20625feba69851a2830b28073417c0d27981efb35f45.png)  

### size of nodes:
-  n+1 pointers
-  n keys

### b+ tree rules
1. all leaves at same lowest level (balanced)
2. Non-root nodes have to be at least half-full
   1. Non-leaf: ceil[(n+1)/2]pointers
   2. Leaf: floor[(n+1)/2] pointers to data
3. Pointers in leaves point to records except for “sequence pointer”


## B+ tree deletions in practice
- often, coalescing is not implemented
  - To hard and not worth it

- LRU is not a gool policy for b+tree buffers 
  - should try to keep root in memory at all times

# hashing schemes
## hashing
- hashing function h returns the address of bucket
- if the keys for a specific hash value do not fit into one page the bucket is a linked list of pages
![picture 8](images/eef51ec03d74b49c247ff72ad0f018af4916721a9cf9b48fe853f20a7988c8cf.png)  


- Example hash function
![picture 35](images/b0cae3e682432928c9f9d717bdfbbbd22d97a79114e0ca773b0e26e558d542b8.png)  

- good hash function L: expected number of keys is the same for all buckets

- within a bucket:
  -  do we keep keys sorted?
  - Yes, if CPU time critical & Inserts/Deletes not too frequent

![picture 36](images/ccfeea2615944910ffce9f2068917f13291992161a84c065bc076acedef53e3f.png)  
![picture 37](images/b18f83f75682503fdf3b08b5266b1513f80c948da5a292942da393c4abc352e9.png)  

- Rule of thumb
- Try to keep space utilization between 50% and 80%
- if > 80, overflows significant depends on how good hash function on # keys

- how do we cope with growth
  - overflows and reorganizations
  - dynamic hashing
    - extensible
    - linear

Extensible hashing: two ideas
1. use i of b bits output by hash function
![picture 38](images/cf03485929e7821982f1620d73d5ff74494a6758a70f09a233e0d65570511239.png)  

2. use directory

![picture 39](images/49916680fad94d72e507854fb473cbb2c8d06b6f88fd6925effc9d9761e41e48.png)  
![picture 40](images/b3644c3d739a27ad1548ed2441b38b1469619a0778fc379acb56cb7492b0cdd7.png)  
![picture 9](images/06a516370142d702fd49b56895158ce9d866b7586a843bda27ecfe688ec92c70.png)  

![picture 41](images/3bd6902acc07a7942183632d6c68e1661c25cc82ffa5bedb25089addc6f1ce4b.png)  

Extensible hashing :deletion
1. no merging of blocks
2. merge blocks and cut directory if possible(reverse insert procedure)

## summery Extensible hashing
- can handle growing files
  - with less wasted space
  - with no full reorganization
- indirection
- directory doubles in size


## linear hashing
- another dynamic hashing scheme

### Two ideas
1. usr i **low** order bits of hash
2. file grows linearly


![picture 11](images/ccf0eb5e2c373397dbb19b8676f55b6901f173af2640cc14dcc47658a05b2899.png)  

![picture 12](images/607c66cfc9f8b9ffdaaf032300f21e35ff21050d40b155715ef3a04055bb6044.png)  

![picture 13](images/316390684bfbf28f1a803e10d0c4d577187c799804c99f0ca2034084e939296e.png)  

When do we expand file 
- keep track of $\frac{number \ of \  used \ slots}{total \ slots \ in \ primary \ buckets} = U$
- if U > threshold then increase M (and i,when m reaches 2**i)


## summery linear hashing
- can handle growing files
  - with less wasted space
  - with no full reorganization
- not indirection like extensible hashing
- can still have overflow chains

![picture 42](images/e7b67c04593c54141feaecf8d38d26ab1996b14abdf27b2b4016e2abaee12896.png)  

## index vs hashing
- hashing good for probes given key
  - e.g select * from R where R.A = 5
- indexing good for range searches
  - e.g select* from R where R.A >5


# index
## note 
- CANNOT SPECIFY TYPE OF INDEX (e.g. B-tree, Hashing, …) OR PARAMETERS (e.g. Load Factor, Size of Hash,...)
- ATTRIBUTE LIST -> MULTIKEY INDEX

## multi-key index
- e.g find records where DEPTE = "TOY" AND SALARY > 50K
### Strategy I:
- Use one index, say Dept.
- Get all Dept = “Toy” records and check their salary
### Strategy II:
- Use 2 Indexes; Manipulate Pointers

![picture 14](images/2f76ef1d1180f02179f3ab66fe8f898cd280e8ff6178a68b4a708458f1a18784.png)  

### Strategy III:
- Multiple Key Index
![picture 16](images/bcd5d0a4f6974e5d0de85d43113579d98e75c617f1b23ef358b7d46997ea7b7b.png)  
![picture 17](images/8a8752bc8ac60fb797f3a8f6f10f3a799c436429be41dc882dd237ffc85a4bcc.png)  

#### Interesting application
![picture 18](images/b47857b433e48ea852cec99d4dd58f60dc815657d13a6767549abeeee67dcf19.png)  
![picture 19](images/898297828e798b8cdb68a4a79cc3a14adb199285990f0a57e1508760930daa26.png)  


# Bit map indices: alternate structure,heavily used in OLAP

![picture 2](images/a4fff09b597db1dc09df2a3e3426cb5579068844ef5783963d993c85bc2693ac.png)  


## 2nlogm compression
- naive solution needs mn bits,where m is number of distinct values and n is number of tuples.
- but there is just n 1's.
- bit encoding of sequence of runs
- 10 here means 1 one, 110 means 2 one
![picture 3](images/ca774e382632e0447b69dd7a52daf5013b866b47c171d1afd48e0d66331dcd19.png)  
![picture 4](images/51292f559324c997c569395a41bf60c2937dad5987c6926b01fb150043d8fb1a.png)  

## insertion and deletion and miscellaneous engineering
- assume tuples are inserted in order
- deletion : do nothing
- insertion : in tuple t with value v is inserted,add one run in v's sequence( compact bitmap)

# query processing
- The query processor turns user queries and data modification commands into a query plan -a sequence of operations (or algorithm) on the database
  - from high level queries to low level commands

## relational algebra
- e.g. 

Select B,D
From R,S
Where R.A = “c” AND S.E = 2 AND R.C=S.C
![picture 20](images/c7eafb02baaf819e901d7dea706129d6e63ea12f7f8111d48bdc93d1ef8ef202.png)  

![picture 21](images/34de7d49e0633fd67198d67d78258df6225e43fb2b6678389e6f6910f1304e1c.png)  

![picture 22](images/716a5c3c498257ce7c0b6d19f2fe95326c0b69a2f17a8fb0c5855d23770e4fa9.png)  
![picture 23](images/5a6343de4815d19ea32cdb7bb535f762d09672c97972f7077f99c3ae3a1abe0e.png)  

### natural join
- SELECT t1.id,t2.id,desc1,desc2,desc3,desc4 FROM t1 INNER JOIN t2 ON t1.id = t2.id;
- equals
- SELECT t1.id,t2.id,desc1,desc2,desc3,desc4 FROM t1 NATURAL JOIN t2;
## from query to optimal plan
![picture 1](images/3f3b36face7e1915a58e14e87670a6a8f95ae1ea3501bdce309d0eebabc1cdb9.png)  

- Example: The Journey of a Query
![picture 24](images/c31f3a651ffdbbcb7fccccb4fe367f736ac03ea2d5806f89d4dab7df0e919d88.png)  

![picture 25](images/ab411ab5a437e5640271898b866e8c0eb16c4de682e03dd9e28ee62d1cc25793.png)  

## Algebraic Operators: A Bag version
- Union of R and S: a tuple t is in the result as many times as the sum of the number of times it is in R plus the times it is in S
- Intersection of R and S: a tuple t is in the result the minimum of the number of times it is in R and S
- Difference of R and S: a tuple t is in the result the number of times it is in R minus the number of times it is in S
- $\delta(R)$ converts the bag R into a set
- example
![picture 27](images/15121833dc772abd84684d4602b5597b4b8f9f259b60517cb3a3b63599036cc3.png)  
R union S = {a,a,b,b,b,c,c}
R - S = {B}
## extended projection
![picture 26](images/f74baa45f9410d353b812bfc66beb42d192c41c66302e493cd1644d8cf028d27.png)  
SELECT 2*A AS D, B, C AS CPRIME FROM T
$\pi_{2*A -> D, B, C -> CPRIME} T$

## Cartesian Products => Joins
- Product of R and S (R$\times$S):
  - If an attribute named a is found in both schemas then
rename one column into R.a and the other into S.a
  - If a tuple r is found n times in R and a tuple s is found m
times in S then the product contains nm instances of the
tuple rs
- Joins
  - Natural Join R S = pA sC(RS) where
    - C is a condition that equates all common attributes
    - A is the concatenated list of attributes of R and S with no
duplicates
    - you may view tha above as a rewriting rule
  - Theta Join
      - arbitrary condition involving multiple attributes
      - $R \theta_{condition} S = \sigma_{condition} (R \times S)$

1. Equi JOIN
    1. NATURAL
    2. USING(a,b)
    3. =
    ...
2. Theta JOIN
    1. &gt;=
    2. &lt;=
    3. &gt;
    4. ...

R(A, B, C),S(A, B, D)

$R \bowtie S = \pi_{R.A -> A, R.B-> B, C, D} \sigma_{R.A=S.A AND R.B = S.B}{R \times S}$ 

## Grouping and Aggregation
![picture 28](images/e263634527984e30530205bb0209eb18423dd4af646bf82fa43404af11cc1e74.png)  

## Grouping and Aggregation: An Alternate approach 
![picture 29](images/a34780b1276493b053d083b5004bee59e85de155cd92c10b3ac4f05a690584be.png)  

SELECT Dept, AVG(Salary) AS AvgSal FROM EmployeeGROUP BY DeptHAVING , SUM(Salary) >100
$\pi_{Dept, AvgSal} \sigma_{SumSal > 100}\gamma_{Dept; ,AVG(Salary) --> AvgSal, SUM(Salary) -->SumSal} ( Employee)$
## Sorting and Lists
- lists:ordered
- bags: not ordered
![picture 30](images/562ed8c5c4328f3c52e2cdbfdf9fb1382bdd7511ac608d0f12c36a3310b8334a.png)  

# Relational algebra optimization
## Algebraic Rewritings: Commutativity and Associativity
![picture 31](images/e971e593b0e5e463ee268322d6f2a86235f140129a975dc7316a6ee96508a0bf.png)  
![picture 32](images/675f2a43a9fdf3ccfb667d00d4969a67a56ae0877548ab8c65f70bdc2abf4340.png)  

## Algebraic Rewritings for Selection: Decomposition of Logical Connectives
![picture 33](images/b083584b066df77930a0c1046e41175fa1b3a04b4154fdc9e41b439c836157bd.png)  
No
## Pushing the Selection Thru Binary Operators: Union and Difference
![picture 34](images/7102114bed8d31ebe0b9300ad29e77828293a4b572d703813dbd708676d7fa63.png)  
## Pushing Selection thru Cartesian Product and Join
![picture 35](images/6d892b79752812fad1a286ac90ffc3bf1ac2cf13f818c4c9a4d0b6247531bd8c.png)  

## Pushing Simple Projections Thru Binary Operators
![picture 36](images/1c45bef73fb70827b265a619f2475325e9d52fb2f9549a3edb84fec2a9e6bc3f.png)  

## Pushing Simple Projections Thru Binary Operators: Join and Cartesian Product
![picture 37](images/eb1b41c74b749295c37abd797ab763a9c797e764e7a72e12f89eec5cd251644f.png)  

## Notes
- No transformation is always good at the l.q.p level
- Usually good:
  - early selections
  - elimination of cartesian products
  - elimination of redundant subexpressions
- Many transformations lead to “promising” plans
  - Commuting/rearranging joins
  - In practice too “combinatorially explosive” to be handled as rewriting of l.q.p.

# Algorithms for Relational Algebra Operators
- Three primary techniques
  - Sorting
  - Hashing
  - Indexing
- Three degrees of difficulty
  - data small enough to fit in memory
  - too large to fit in main memory but small enough to be handled by a “two-pass" algorithm
  - so large that “two-pass” methods have to be generalized to “multi-pass” method (quite unlikely nowadays)

## The dominant cost of operators running on disk:
- Count # of disk blocks that must be read (or written) to execute query plan

- additional parameters:
![picture 38](images/28d86d1b06c981a1a8e4c3d8c38cc33d5abc074261c5dba1bfde5d1dcf5afddb.png)  

- Clustering index

![picture 39](images/129fd5da724b6c20414d46d774b7d8bc6416830147cff808e97bcbe55b1139a9.png)  


# Pipelining 
![picture 40](images/8e03145e62e8b95b75c62407896bef890d9457e379929ad748ecb6dc2794f945.png)  


## Example
- $R1 \bowtie R2$
- Iteration join (conceptually – without
  taking into account disk block issues)
![picture 41](images/8541902c06fd0973d7e111fa5cdb78f9f9796c77a83fb28a0cc3343d0cb29a01.png)  

- Merge join (conceptually)
![-  1](images/fcdbad60460f12db46cf8a41012ea27e85bbf1220612cbe2058fc4c75b1ff18b.png)  

- Procedure Output-Tuples(Deal with duplicate values)

![picture 43](images/fea0b50d6931f9a69e22104312e832248a21bf806b8706285c9f9a0c733cf4b7.png)  

Join with index (Conceptually) 
![picture 44](images/b8f80c7eeab1482d1c5b7f69484566f76d88d857ba3eaf32d4c7eb09dff51eb2.png)  

- Hash join

![picture 45](images/2cc34b9585e97e692b40360f340cfad35e9ef91b351a38e15b4b31fc9e170105.png)  

# Disk-oriented Computation Model
![picture 46](images/9dacb2ab40b6e7588d1e8d122fa24cc0d92faa5c3307cfc0c63d82dbf90f4ded.png)  

## notation
![picture 47](images/4d157f46a992994b2a6873b14196f5733e8adab6d2de6a23643da185aaa2ca9f.png)  

## One-Pass Main Memory Algorithms for Unary Operators
![picture 48](images/61cbe8e294974176a4de63b68958353bd042cb77447a4083779d0b60bae3b430.png)  

## One-Pass Nested Loop Join
![picture 49](images/0670859a3d3590d142e02b8750836dbc05d9cd1f7f753d52df236323653fbb8c.png)  

## Generalization of Nested-Loops
![picture 50](images/4e4f3f6f06d80b3e6045aaf2aa9c4fd1b99b22bd11c1136dd571cc639f0b000a.png)  

## Simple Sort-Merge Join
![picture 51](images/e0c4eee7e90c201ff3a712ba9353c44e0fc24ee2fb2a200a79cbf0ab455c2745.png)  
- Cost:
- totally： 5 B(R) + 5 B(S)
- sorting:  4 B(R) + 4 B(S)
## Efficient Sort-Merge Join
![picture 52](images/214a1b5cf9fa91f177cbfd50255bed105545d324307823572875887eb73e9d20.png)  
- ignore phase 2
- totally 3 B(R) + 3 B(S)
### Example
![picture 53](images/ece16b75663308ef66f0e79c8dd86eda685e94657027696e910aca2f1843d313.png)

## Two-Pass Hash-Based Algorithms
![picture 54](images/047a64346b6fb151240cf9866739f4a3baad1043ce3cc359461a415a462e1033.png)  

## Hash-Join Algorithms
![picture 55](images/8a9e5031e580243300453780381bd5372cc144c876506cebeb72047de3071797.png) 
- totally 3 B(R) + 3 B(S)

## Index-Based Join: The Simplest Version
![picture 56](images/badbc0c034e332b52aca0010977b0ef0f14b26376214e8740a015f589940fccd.png)  

