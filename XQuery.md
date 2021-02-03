# Why XQuery?

- XQuery vs XSLT
  - XSLT is a procedural language, good at transforming XML documents
  - XQuery is a declarative language, good at efficiently retrieving some content from large (collections of) documents

# Main principles
- Closed-form evaluation. XQuery relies on a data model, and each query maps
an instance of the model to another instance of the model.
- Composition. XQuery relies on expressions which can be composed to form arbitrarily rich queries.
- Type awareness. XQuery may associate an XSD schema to query interpretation. But XQuery also operates on schema-free documents.
- XPath compatibiliy. XQuery is an extension of XPath 2.0 (thus, any XPath expression is also an XQuery expression).
- Static analysis. Type inference, rewriting, optimisation: the goal is to exploit the declarative nature of XQuery for clever evaluation.

# A simple model for document collections
- A value is a sequence of 0 to n items.
- An item is either a node or an atomic value.
- There exist 7 kinds of nodes:
  - Document, the document root;
  - Element, named, mark the structure of the document;
  - Attributes, named and valued, associated to an Element;
  - Text, unnamed and valued;
  - Comment;
  - ProcessingInstruction;
  - Namespace.

- The model is quite general: everything is a sequence of items. This covers anything from a single integer value to wide collections of larges XML documents.

# Examples of values
![picture 6](images/ee9d0692095643239baf256ccbcafd75d3e4deafe3f7db05c2508a3b57b329b4.png)  

# Sequences: details 
- There is no distinction between an item and a sequence of length 1 ⇒ everything is a sequence.
- Sequence cannot be nested (a sequence never contains another sequence)
- The notion of “null value” does not exist in the XQuery model: a value is there, or not.
- A sequence may be empty
- A sequence may contain heterogeneous items (see previous examples).
- Sequences are ordered: two sequences with the same set of items, but ordered differently, are different.

# Items: details
- Nodes have an identity; values do not.
- Element and Attribute have type annotations, which may be inferred from the XSD schema (or unknown if the schema is not provided).
- Nodes appear in a given order in their document. Attribute order is undefined.

# Syntactic aspects of XQuery
- XQuery is a case-sensitive language (keywords must be written in lowercase).
- XQuery builds queries as composition of expressions.
- An expression produces a value, and is side-effect free (no modification of the context, in particular variable values).
- XQuery comments can be put anywhere. 

# Evaluation context
- An expression is always evaluated with respect to a context. It is a slight generalization of XPath and XSLT contexts, and includes:
- Bindings of namespace prefixes with namespaces URIs
- Bindings for variables
- In-scope functions
- A set of available collections and a default collection
- Date and time
- Context (current) node
- Position of the context node in the context sequence
- Size of the sequence

# XQuery expressions
- An expression takes a value (a sequence of items) and returns a value.
- Expressions may take several forms
  - path expressions;
  - constructors;
  - FLWOR expressions;
  - list expressions;
  - conditions;
  - quantified expressions;
  - data types expressions;
  - functions

# Simple expressions
![picture 7](images/3d0cd3212edda2de6b79c01ed3d7475044b7e65e8c24e2f4536ebe7c6c8a046b.png)  

# Retrieving documents and collections
- A query takes in general as input one or several sequences of XML documents, called collections.
- XQuery identifies its input(s) with the following functions:
  - doc() takes the URI of an XML document and returns a singleton document tree;
  - collection() takes a URI and returns a sequence.
- The result of the doc() function is the root node of the document tree, and its type is Document.

# XPath and beyond
![picture 8](images/e51affb2bbf0df9bb8c8c3a71444aeaf19df39921f36782f285767b9a2426596.png)  
- The XPath expression is evaluated for each item (document) in the sequence delivered by collection(’movies’).

# Constructors
- XQuery allows the construction of new elements, whose content may freely mix literal tags, literal values, and results of XQuery expressions.
- An expression e must be surrounded by curly braces {} in order to be recognized and processed.

![picture 9](images/d23a50de92f3b82e43710db5a6b12f82594856fa786dbd04251b5119c7d1bf25.png)  

# Variables
- A variable is a name that refers to a value. It can be used in any expression (including identity) in its scope.
![picture 10](images/9a3c8da5f401ab7761d9d089c29c320a024a4472b691a69c5d267cd10c5fbcaf.png)  

# FLWOR expressions
- The most powerful expressions in XQuery. A FLWOR (“flower”) exp.:
  - iterates over sequences (for);
  - defines and binds variables (let);
  - apply predicates (where);
  - sort the result (order);
  - construct a result (return).

![picture 11](images/d4ed0572bc4781b173ff6f6e43e9c51f6dfa5b63b9684365e92be11767f9f693.png)  

# FLWOR expressions and XPath
- In its simplest form, a FLWR expression provides just an alternative to XPath
expressions. For instance:
![picture 12](images/f7f0d1f90beae1fbc698e77e55fa14d97beeafaa26f934f8160f5232d5502ad0.png)  
- Not all FLWR expressions can be rewritten with XPath.

# A complex FLWOR example
![picture 13](images/5798b51ae9c4696bf614c86b7b243a0ef7182d42f50cf3c4970ca97aecd77638.png)  

# for and let
- Both clauses bind variables. However:
![picture 14](images/96d76d774422fdacb29cbd07ef7d0a97e6a0458ce7da6891e8e94b2a221fd036.png)  

# for + return = an expression!
- The combination for and return defines an expression: for defines the input sequence, return the output sequence.
![picture 16](images/894446c74baf316b99837c305b35cf8d894f1655dafaddcff403b0b3a0fbc72e.png)  

# Defining variables with let
- let binds a name to a value, i.e., a sequence obtained by any convenient mean, ranging from literals to complex queries:
![picture 17](images/c8b8a56ef5df4d4d06664259a97816d477674d4f03eb954babeb402487780616.png)  

# The where clause
- where is quite similar to its SQL synonym. The difference lies in the much more flexible structure of XML documents
![picture 18](images/9ccc54cf37bb2f2522c6cd707b043f1bd78687978461be65d0ca442b6e7523d5.png)  
- Looks like a SQL query? Yes but predicates are interpreted according to the XPath rules:
  1. if a path does not exists, the result is false, no typing error!
  2. if a path expression returns several nodes: the result is true if there is at
  least one match.
![picture 19](images/ec84aa237e19ebbe72062cc8782975748cba55834401997802faca979d3574ed.png)  

# The return clause
- return is a mandatory part of a FLWR expression. It is instantiated once for each binding of the variable in the for clause.
![picture 20](images/8e39dabbe12c78508b75372b916908d21a26d25469ae7c3a1da912ddc003df3b.png)  

# Joins
- Nested FLWOR expressions makes it easy to express joins on document, à la SQL:
![picture 21](images/63cb6e937cfb5024a6f50b2703c6a1b1550e0c927716b871682ab45dc3cbb3b0.png)  

- The join condition can be expressed either as an XPath predicate in the second for, or as a where clause

# Join and grouping
![picture 22](images/05a4d14de5984903f62a2ea187bacfc5e41f8b5160899a55ec6c1491b8fa7999.png)  

# Operations on lists
- XQuery proposes operators to manipulate lists:
  1. concatenation
  2. set operations: (union, intersection, difference)
  3. Functions (remove(), index-of(), count(), avg(), min(), max(), etc.)
- The distinct values from a list can be gathered in another list. (This loses identity and order.)
![picture 23](images/98ce15063e87ee323d16b7244632d6e4f9275cb8062ff45829a3cedb737fba5c.png)  

# if-then-else expressions
![picture 24](images/fdc35a580a631d1dbabd3f2f45299e9ea624f24caca39e513f02ab6f33938a21.png)  


# some expressions
- some expresses the existential quantifier:
![picture 25](images/831930fe9790669c557e29390d94f76851c34816042fcb6412829fc139630407.png)  

# every expressions
- every expresses the universal quantifier:
![1](images/decfb2417728108a45620935dd49c824bce57e9cd8e1209f60254c1c3338b24f.png)  

# XQuery processing model
![picture 27](images/9fa882a3c1a40b46dda7b8b2bd7b2c5d7802ce6c502e66bfd9d72baff249e1a3.png)  

# When XQuery doesn’t behave as expected
1. The query does not parse (applet grammar check page) ⇒ reformulate it. You may start from the XQuery use cases.
2. The query parses, but does not work.
3. The query works, but the results are unexpected ⇒ figure out what the parser understood.

- Sometimes the query parses but will not work (the engine will refuse it). The parser only checks that the production is well-formed. It does not check that the context provides sufficient information to run the query:
  - the functions called in the query are defined
  - the variables referred in the query are defined
  - the numeric operations are legal etc.

![picture 28](images/fd24ca249f802bbfe30626590d148be9971343942ba871749e5e5e7cf95db2bf.png)  

- Sometimes the query parses but will not work (the engine will refuse it).
- The parser saw this as a sequence formed of:
  - a for-return expression
  - a path expression
![picture 30](images/bf2f56b1401d0a216b881486e385991dba6083077f1a75cbf2ba9af86dbe7669.png)  

![picture 31](images/f35f8a9cd85be38bbae178cdae0d525d4fbe62ffe46741ea7b1c55d73f054c17.png)  

![picture 32](images/066bec5d7b4b3f5ab955be2b3ef24b66431176ab1e7a73fa315c489de2a5c46e.png)  

# More on comparisons
1. Two atomic values:
   - determine the types of both operands
   - cast then to a common type
   - compare the values according to the rules of that type
2. One atomic value and a node:
   - Cast the node to a string, then proceed as above.
3. Two lists (one list may be of length one):
   - Compare all list item pairs, return true if the predicate is satisfied at least for one item pair.
- Casting is described in the XQuery Functions and Operators document.

# XQuery implementations
- Among those that are free and/or open-source:
- Galax : complete, not very efficient
- Saxon : in memory; by Michael Kay, XSL guru
- MonetDB : based on in-memory column-oriented engine; among the fastest
- eXist : very user-friendly interface
- QizX : Xavier Franc. Nice but not great
BerkeleyDB XML : now belongs to Oracle

# SQL/XML: bridging the two worlds
- Recent SQL versions (2003) include:
  - a native XML atomic type, which can be queried in XQuery style
  - a set of XML publishing functions: extracting XML elements out of relational data by querying
- mapping rules: exporting relational tables in XML
- Advantages:
  - Unified manipulation of relational and XML data
  - Efficient relational query engine well exploited
  - Ease of transformation from one format to another
- Disadvantage:
  - Complexity

# SQL/XML: bridging the two worlds
![picture 33](images/0e2cae9f8957f070adfe8c8bd595fd247e58d559ee244f0075f6d93b5bf43698.png)  
