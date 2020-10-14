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

# hardware & physical organization
![picture 1](images/5a046a181c3f393886607bed18958933d4a9b111b538decfd269a0e4e69ab641.png)  

# memory hierarchy
- cache hierarchy
- ran
- disk
- tertiary storage

# colatile vs non-volatile
- persistence important for transaction atomicity and durability

# peculiarityes of storage mediums affect algorithm choice

- block-based access
- how many blocks were accessed not how many objects

- moore 's law:
- all improves, but at different speed
- dis transfer rate improves a lot
- disk access time improves less

# 2-phase merge sort: an algorithm tuned for blocks
- when considering block based storage,  algorithm we have learned may not always be the best.

![picture 1](images/d510e6b6e1d94a8fc6c527cd996a76e3b3b481dd85e9fc63f60a43d6e601a3ca.png)  
![picture 2](images/9312554501ec6d37e87659bb22352c4f6a320889e2bd3ebd3a9176f3c99c3fa9.png)  

![picture 3](images/f8ff19ea30813220be9cca7b8ddf413f4065aa8da65748bab1b0b8e944d94dc9.png)  

# 2- phase merge sort : most files can bt sorted in just two passes.
![picture 4](images/1b10415f3e20bd421e97123c0296a9de0ed9dacfe14be65fc7a3ef835622f7e3.png)  

# the records are packed row-oriented
![picture 5](images/fe4bedc7b2594507f25df77996a5873a3bb8d45a9baddce7a8c0e265030d5ebb.png)  
- pack each block with maximum number of records
- do not reclaim deleted records:
  - when delete one record, just leave the space marked blank, not moving every record behind to the front
- utilize overflow blocks for insertion with out of order primary key
  - ![picture 6](images/78ee770bdd819bdacf561e2108981e77c862dc28a16255cce244921716c4702d.png)  
- a novel generation of databases features column storage
  - benefits when we only need to focus on a few columns of the records

# indexing 

## terms and distinctions
- primary index
  -  the index on the atribute that determines the sequencing of the table
-  secondary index
   -  index on any other attribute
-  dense index
   -  every value of the indexed attribute appears in the index
-  sparse index
   -  many values do not appear

## dense and sparse primary indexes
![picture 10](images/c07b39347fd00fcb689045749cdff49a6888b07fafb80250c581874591e2a44a.png)  

## multi-level indexes
- treat the index as a file and build an index on it
- two levels are usually sufficient.More than three levels are rare.
- Can we build a dense second level index fro a dense index?

## a note on pointers
- record pointers consist of block pointer and postion of record in the block

## representation of duplicate values in primary indexes.

## deletion from dense index
- deletion from dense primary index file with no duplicate values is handled in the same way with deletion from a sequential file

## deletion from sparse inde
- if the deleted entry does not appear in the index do nothing.
- if the deled 


## duplicate values & secondary indexes
![picture 11](images/97117b4828994c30a5cb22a300908712b4e86c8d6008957ae9762b861a75b59b.png)  

## why bucket + record pointers is useful
- enables the processing of queries working with pointers only
- very common technique in information retrieval

## advantage of buckets: processing queries using pointers only
![picture 12](images/711d469c709f65d412a622caae8c9c28f3bd74aadc3e366ffaa3f018af5f96f8.png)  


## b+ tree - another kind of index
![picture 13](images/4e104373c0e02a5eb0d6b0d500a0c5ae230e6ed76d12dfe42906386100b544df.png)  

![picture 14](images/0021a23743b571f54c918ac765b23ed57735c6a9c63d0f7cacd356192cf15b42.png)  

### size of nodes:
-  n+1 pointers
-  n data

### b+ tree rules
1. all leaved at same lowest level (balanced)


