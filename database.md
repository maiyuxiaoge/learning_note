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

- LRU is not a gool policy for b+tree![picture 18](images/2875688756d6996bd42d2c921dbb241dcec458b5c15620e4953ed946fe474594.png)  
 buffers 
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


## Opportunities in Joins Using Sorted Indexes

- Estimating cost of query plan
  - Estimating sizeof results
  - Estimating # of IOs
![picture 1](images/abefc849019301569977295c8085108c6e6dd2be17b06b5f58a625ce70d722e7.png)  

- Example
![picture 1](images/c02e9e09781e0c0440880db8ece21d38f0857c625e396500c056ab68fa7e94b9.png)  

- Size estimates for $W=R 1 \times R 2$
  - $\mathrm{T}(\mathrm{W})=\mathrm{T}(\mathrm{R} 1) \times \mathrm{T}(\mathrm{R} 2)$
  - $S(W)=\quad S(R 1)+S(R 2)$
- Size estimate for $\mathrm{W}=\sigma_{\text {z=val }}(\mathrm{R})$
  - $S(W)=S(R)$
  - $\mathrm{T}(\mathrm{W})=\frac{\mathrm{T}(\mathrm{R})}{\mathrm{V}(\mathrm{R}, \mathrm{Z})}$
- Size estimate for $\mathrm{W}=\sigma_{\mathrm{z} \geq \mathrm{val}}(\mathrm{R})$
  - T(W) = 

![picture 2](images/2c1685697173f4bda5e0a53410ad60ea49e0c43c584a1f3997e43ff9f2add6b3.png)  
![picture 3](images/9db923a20e85e7d4e4453e42fd7351a7f821b2386f4698bbdafe25616292bf92.png)  
![picture 4](images/5654e34c3f984b5bb2461b1ed416e3211028b0d9a3c749269a7215f5e2f7f5ea.png)  

- size estimate for $W=R 1 \bowtie R 2$
![picture 5](images/6fbc92d655d3aa7dfbc688db121d9916e4dcb3abd5d352c4986978571e5af375.png)  
![picture 6](images/bd0307959dcf1d1e7782a88e71341cffab327315b9aab663920d370c4da88003.png)  

![picture 7](images/ad45470f581d2e5372f91041a9ff2b772b5efea851d0c70aecec8b883e383d3c.png)  

![picture 8](images/7882567be8efeb0e91dcb7a45470014a26a14d75689551e141b3cc3a64818b0e.png)  
![picture 9](images/6807cf0318f0e02df8bfa9b183840076ae2ff45cf5bd8ef4dd861425e0768a52.png)  


- Example

![picture 10](images/0cb63c57f1df129c4488a3abb63798ffe6ddec13a900a442695efc12a47fa887.png)  

![picture 11](images/e45ae486d551f64b5754e55e935cde4069b9a941d15e1bbd741775c0cd6502fe.png)  


# Arranging the Join Order: the Wong-Youssefi algorithm (INGRES)

## challenges with Large Natural Join Expressions

![picture 12](images/ac1f9023a7f998005b91b6ab0d48167b2e14a8555e3ff56cabd2ebb7bfc067fd.png)  
![picture 13](images/e4d0beb7dc16b7ff315f8baa8535f289b4120a8bab018478f728327856465291.png)  


## Wong-Yussefi algorithm assumptions and objectives
![picture 14](images/87cf4722cdb60dbca7c50c465cafc4a7640ad4ebfcad1ad13ba7856d227abf01.png)  
![picture 15](images/f5288215c32916083ac586b403fb04dd4c493619ba6eab37d740c932da766a8d.png)  


# failure recovery

## Integrity or correctness of data
- Would like data to be “accurate” or“correct” at all times

## Integrity or consistency constraints
![picture 1](images/0874e605b0a2744c62daf3e26142e99038be214aba6c155b0f06bbd56b4cffc4.png)  

- Big working assumption:

If T starts with consistent state +T executes until completion & in isolationT leaves consistent state

## How can we prevent/fixviolations?Preview of the next episodes:
- Failure Recovery: fixing violations due to failures only•
- Concurrency Control: fixing violations due to concurrency & data sharing only
- finally a mix of the two: fixing violations that are stem from interaction of failures with sharing

# failure and recovery
## failure model
![picture 2](images/48c5256832c94c65a699057bbc54cf8f95ce56207b45d4ccb04186561fb75463.png)  


- Desired events:see product manuals
- Undesired expected events:
  - System crash
    - memory lost
    - cpu halts, resets

- Examples:
  - Disk data is lost
  - Memory lost without CPU halt
  - Skynet’sCPU decides to wipe out its programmers

![picture 3](images/9b009796a825eb38d589b5ff8f44d22aa01e1d20b99168ecb6491b84978f24e9.png)  

![picture 4](images/b3147cb4bf97776a98c436d539e716a18bd2c9906ec257426088f67c754a54d5.png)  

![picture 5](images/5bdb672dc1416fbabb2789fea3716f417f2f8d1c72771c26edde43c3dd47a00d.png)  

![picture 6](images/c19bb0b13b754f23d45b77cecc2f3ff3acc1e03c3e3f92fa878f032053db7450.png)  


## one solution: undo logging(immediate modify)
![picture 10](images/6e67cddb662504acddf0136017a35263e6a5a4f747bfd8c50df171a0291e110b.png)  

- one complication
  - Log is first written in memory
  - Not written to disk on every action
- two complication


## Undo logging rules
1. For every action generate undo log record (containing old value)
2. Before x is modified on disk, log records pertaining to  x must be on disk (write ahead logging: WAL)
3. Before commit is flushed to log, all writes of transaction must be reflected on disk

## Recovery rules
![picture 11](images/dcb75458d84bf86fb0eb326b3f2db9845982435e223075c49da6b0664bbf5eb0.png)  
![picture 13](images/27c8874da456de63b84835c5c8acf14e321a3847f7f07f7405443c9aeb1bdd13.png)  

## redo logging rules
![picture 14](images/52961dcd54bef9b51431df3123e12d61a400448080930d5ed55572cd82a6738a.png)  
![picture 15](images/53f83ca119ac3ec1864d7a10726e1a68ea1c4b24fef252fd6c3d0ac3a02a11d8.png)  
![picture 16](images/dc80d87c1306d27c3785805bf069dd3ff4117c1b1dd4b08ec619dfd37b10daa6.png)  
![picture 19](images/6b0711870725c0b1d0bb37ea58becf63cf62745a34062320b9d6c6f8f9b41c7a.png)  

- solution: checkpoints
- ![picture 20](images/56fe70eb324c8e72ea2b99a296f04554321c11aeff46abf39294dc488731f436.png)  


## Key drawbacks:
- Undo logging:
  - cannot bring backup DB copies up to date,real writes at end of transaction needed
- Redo logging
  - need to keep all modified blocks in memory until commit

## recovery process

![picture 21](images/8f02c8d1b395cd8bd5023a40a3a0a84c76bb785bc741055116874b6114d4a565.png)  


# concurrency control

- Want schedules that are “good”, I.e.,equivalent to serial regardless of
  - initial state
  - transaction semantics
- Only look at order of read and writes
- Example: SC=r1(A)w1(A)r2(A)w2(A)r1(B)w1(B)r2(B)w2(B)

![picture 1](images/c616d18d72614e29f307381ffb660ece989e791d5634bf221a64f017b7de4db8.png)  

![picture 2](images/d1b774945d11bb79f3c0f6eb3fa235959504e49638a27921a531c017864b0d98.png)  

![picture 3](images/977faec13ab0947c4f5d4342578a4a6a6d806d0878ee92aa033fe9a35b5c6005.png)  

![picture 4](images/6c430785dcfae4cd3a8d380a4a95377a73cbfe6bd24b848d600cf7f8af759f55.png)  



## definition
- S1, S2 are conflict equivalent schedules if S1 can be transformed into S2 by a series of swaps on non-conflicting actions.
- A schedule is conflict serializable if it is conflict equivalent to some serial schedule.(T1- > T2)

## Precedence graphP(S)  (S is schedule)
- Nodes: transactions in S
- Arcs:  Ti Tj whenever
  - pi(A), qj(A) are actions in S
  - pi(A) <S qj(A)
  - at least one of pi, qj is a write


## lemma 
![picture 5](images/df4afe505eeffda4b48f1f37df37246ea1ac641f7c5e00f6247dffa50893fac0.png)  

![picture 6](images/6ab533898d5b8563f2a58c5dbe3d41f27014ac29fbe21a284c5db6c173aa3924.png)  

![picture 7](images/27412d5cea03ae61d22ae12999bbf3ab0e499a5470c0d67f1f653c2650fbfbc0.png)  

![picture 8](images/fd6ae345f799a739c5ebc0bee2bf3b019ad092f32c13fcbb1a55cf91560f194c.png)  

## How to enforce serializable schedules?
- Option 1: 
  - run system, recording P(S)
  - check for P(S) cycles and declare if execution was good
  - or abort transactions as soon as they generate a cycle
- prevent P(S) cycles from occurring 
![picture 9](images/2a4dfa79b5451b11966e828efb7971e45a6f85c3d999085be8ed1466105e7646.png)  

## A locking protocol
![picture 10](images/75efd0b5744c6ffab406a612229bad80bc2edbf2de6ec29d6511ae544a5e1f94.png)  

![picture 11](images/72a582db67543c0e678a658208d3079dce120434c8daaf08356c5b1b3f8ab0f3.png)  

![picture 12](images/dc52ccc91d691dadf0d3c4316e8c1422f256091b41a07cad6fab110aceea5ca1.png)  

![picture 13](images/75e045401c0f9c7ef61acc9c1b3e73ccbf2cfc9adaa757e5bbc99694ef45c5c5.png)  

![picture 14](images/2aa8d9881909f5f21f3a39326e079d1a07e47fed22f5dde4aea469f46740d177.png)  

![picture 15](images/112a2bef7923d75967e55d2a299081de0505c25fb63d6e882f2af17875bff149.png)  

![picture 16](images/e238960a1a920590951ed97439cd924acaf58093c0d36acf37a299d3b804ac57.png)  

![picture 17](images/ed0e7e5d1487f5656716ce6a738c9ad2e5f323f0b7f75f7245fa4ccf5bff1d62.png)  

![picture 18](images/458a2025e4d0fb7d0fbcff0c33e5f7cc9d22ed3e718fc3eb183a3702f3d08d85.png)  

![picture 19](images/ab5efb59c7834a5afe978a153fbd453bf0b42030aaaf6e2d7254f9bd34032a77.png)  

![picture 20](images/aa49b51115d1568863c10dd53722661a592852145b67493240831626529b76a4.png)  

![picture 21](images/c3cfc898957adc7cf09be2768cbb889f51c2356512885099d34cb209402374dc.png)  

![picture 22](images/8f0c8290614be0b2e0a700e260805a9311c1f198272d3dc7f887122fd8bbf18b.png)  

![picture 23](images/a5e3301d4e36248df46856ca9bf9907b84f2db372577b57dc7d5659e4f020722.png)  

![picture 24](images/b9a6ac96a543e39b2de024dbda7fe3a6e58098e6326dab714977bde221e29a62.png)  

![picture 25](images/35cb77e841b70bcd4d60e8bf22e434a66056d9d346a70d42737b507dd96fc3bf.png)  

![picture 26](images/b3da34f096212e64de265a4979d903cf3fd11f79a6734fc58d2b35fd84b8640a.png)  


## Lock types beyond S/X
Examples:
- (1) increment lock
- (2) update lock

![picture 27](images/b41a1695b95ee696b4c319ada475257047adb477555e0b188fc472a1ba5be10a.png)  

![picture 28](images/4126d25c59b328183487f30029ff0d3faf76d3dfdfb026b7357a946901942a66.png)  

![picture 29](images/0e9373aa9eafd2ee8827fbada60c707a3c95a50b6f9e8d2fde4c874530f86f0a.png)  

![picture 30](images/bcaedfb2ac874b0b67639a9bd2685148660de7fdf5aef7925ecf36c38b2e5a25.png)  

![picture 31](images/712b1627eae9e8ed6f8cf1ead659600e3168cbd6e1a741d7ac8714373ee5238a.png)  

![picture 32](images/cc7ad9046758056afd842c822dbb215a631b46c9c665a7b681034115404984ec.png)  

![picture 33](images/350c56b5ae94f525d8471bb00d177b7534ede4b7265cd3debb4d7b4d84827705.png)  

![picture 34](images/454566da73ef391d4f13d0986503e085856349fe7e9f3917f199c868f966de27.png)  

- Still have a problem: Phantoms
![picture 35](images/36328e8c2576571d68439b0a4e668204f03735cb1d8a5e44c6f927fc45110dc6.png)  

## Tree-based concurrency control
![picture 36](images/c8e486d50a3faccd0493d55fe8238e229614cdf1c6cce28fca8d557e13a641e7.png)  

![picture 37](images/17b842d629201c7b0fbc611db1ab6cb7d03b24679b19b8f30834ef0c83a914a3.png)  

![picture 38](images/84332a36334b2b4d986a3c9ec5aa91bc3fb3ed5974fde8c3f22a36aa2a1c2b2e.png)  

![picture 39](images/22ea4f976a25bdf081a52a6027fab3eaa075740516832e75fe86ae84f81ac30e.png)  

![picture 40](images/f6c944dbc7e09f91fe10f71f51227387d88c413722d68462f8f5d6287f072d74.png)  


## Validation-based Concurrency Control
![picture 41](images/533706339b98332c0f7e85cd9c0a797d878b789bb27b056538912df58e152641.png)  

![picture 42](images/30483495a24db690cae5340821aaab6c654413ab5d8cc821b66337356a0fce28.png)  

![picture 43](images/defdcc38a5660eb5407208b93c77e0ca44c874ea65ed57ff697617cac4f5585d.png)  

![picture 44](images/a98f79bb378ac1e25eae3d0c318e786193a6d8de4f5c851ee942a080f47ddacd.png)  

![picture 45](images/798232509ad994d8bb47eae817a39d22cf8078acc721731cc4bb60836af36156.png)  

![picture 46](images/0efdc3c8e1296899fb9c790081f5ff925b0ad1ff2b5fd00ac88440bfbbd0a61a.png)  

![picture 47](images/896ff0bf9c243956487d39ee4837fef72dbafcdb5fb828819a968b68c8961886.png)  

![picture 48](images/8163e3ced95e12713d28ccbefff9ec6aa20f725242dddfa396b31c4a2ea1c3d0.png)  

![picture 49](images/97181a75189a01d2f4fcfe8872fd5ac0c4b2805bd81630f6a627c3c709d37496.png)  

![picture 50](images/f47c7d73a9ed4137d4b1910d5cc76df90ba451d0c10776cd269d1c4402ee51e3.png)  

# More on Concurrency Control and Recovery
- Cascading rollback, recoverable schedule
- Deadlocks
  - Prevention
  - Detection

![picture 51](images/2f80644ab4415f3ce804172c8fb3de773dcc800f50566f5b68398a8fad9850a1.png)  

![picture 52](images/eef1d22a2f3c2918a3b5f62fe6dc0736f307b78fedc777bcf6de38d833fdfee0.png)  

![picture 53](images/1e5288c21fe2a4afa91543fb0aac85079d1f9e8f1ddd688ab51b2b5369d5e64e.png)  

![picture 54](images/de284c7a31a3f238464e9248b9b75cf655a71b313620c8348872fab6a203a448.png)  

![picture 55](images/64134094a3a11d7ce4184d0aa75af36bc1ae3ebb3403f3db15d467e76872d4bf.png)  

![picture 56](images/ce29edafb429c14de4507b60e0846f4208a26445696532f00f0d982a1cf2ad53.png)  


## How to achieve recoverable schedules?
![picture 57](images/36ee46688051d716593cdbfc6480d42af7824b5467184f612b4a117cbd9788ed.png)  

## Deadlocks
- Detection
  - Wait-for graph
- Prevention
  - Resource ordering
  - Timeout
  - Wait-die
  - Wound-wait

![picture 58](images/002bd2096956424321f928eabfc57ab9320f55377157d28f77343cdf28db9b8a.png)  

![picture 59](images/c534e5cf265be3c91fd1d97199f312a3f00e0825dcc139cb1a11df5553ae0ef3.png)  

![picture 60](images/2efb0a0da7acfec88cb1875e16c0d6912d3f23a5fdabb0bf0de4275bd9f2d045.png)  

![picture 61](images/c664cc809f4372fb709bb25d166fb947955a634301cff7640a79f38b80394f8b.png)  

![picture 62](images/41e43149d5abe3d15df4cac79d9632119ec28d5ba6864517e9a91a121c701c55.png)  


# Integration
![picture 63](images/094e34501914c5f7bc949c98902d06149ffb68c614c6e9b972a26e75b97ca148.png)  

![picture 64](images/f039580997ec5496f5d516c6e804f4adbb58b772b086f4076cb6c334e25e10c3.png)  

![picture 65](images/d802fe417bcc2b7492d11af7d58f6f28257326164895c726391e54f6151b72fe.png)  

![picture 66](images/86a636679c4c71339539eadb1dd8565aabdb52f42ca6901f4464917042d41324.png)  

![picture 67](images/a50c8f3f0f5f697a3ec15e5f7ba1b72439210441ea97e8f9acda65d42f7f77e0.png)  

![picture 68](images/6017e00b10a865b687973bdf1907bd0e5319bb902b1d9a401451084db18faa2e.png)  

![picture 69](images/dd6de6ac3853b6db2803a9b0dc336d9b7a61fdb0dd908adf0c8de429a5b8ed89.png)  

![picture 70](images/f177e42c203be20d11c8eeb491bfe29546428c93ae59259ca6d81463f05ebcc4.png)  


![picture 1](images/30df46685f65899bc684ca734265236c11a4ea4b5f04cae41bc024a5f6204834.png)  


![picture 1](images/312a839e06cfbbbf380ceb3ed9dda3157e597ad6f34e4f569b2eb58469cd27a7.png)  
