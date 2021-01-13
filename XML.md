# Web Data Management and Distribution
# preliminaries
## Web data handling
- Web data: by far the **largest** information system ever seen, and a fantastic
means of sharing information.
- The challenge, under a data management perspective: master the size and
extreme variability of Web information, and make it usable.
## The role of XML
- XML describes **content**, and promotes machine-to-machine communication and **data exchange**.
- XML is a generic data format, apt to be specialized for a wide range of fields
  - ⇒ (X)HTML is a specialized XML dialect for data presentation
- XML makes easier **data integration**, since data from different sources now share a common format;
- XML comes equipped with many software products, APIs and tools

# xml,Semi-structured data model
## Semi-structured data model
- A data model, based on **graphs**, for representing both regular and irregular
data.
- Basic ideas
  - Self-describing data. The content comes with its own description;
    - ⇒ contrast with the relational model, where schema and content are represented separately.
  - Flexible typing. Data may be typed (i.e., “such nodes are integer values” or “this part of the graph complies to this description”); often no typing, or a very flexible one
  - Serialized form. The graph representation is associated to a serialized form, convenient for exchanges in an heterogeneous environment.
## Self-describing data
![picture 3](images/8f0796a8fd78087ea3e107a89278a8ee3d8fb214f548725e18cda098d69c148e.png)  
## Tree-based representation
- One choice:Data can be graphically represented as trees: label structure can be captured by tree edges, and values reside at leaves.
![picture 4](images/659ca0b7d190c84093896a4505b299dcba3acbbe136c876ae13f8c9e1c0d27e5.png)
- Another choice is to represent both labels and values as vertices(The XML data model adopts this)
![picture 5](images/9bcead71efbc226887c7afc8a03b9b9233435c1810bfc2206b3c141c44ae2258.png)  
## representation of regular data
![picture 6](images/737f774b20897b4607ac7609b55e4c0b3a6acc699dc61f2d29542154d8fa0a97.png)  
1. relational data can be represented
2. for regular data, the semi-structure representation is highly
redundant.

## Representation of irregular data
![picture 7](images/766799f0d66824c6eaadf7fc809d95eae0928e759fb3e40aedc9384860694ceb.png)  
- Node identity:Nodes can be identified, and referred to by their identity. Cycles and objects models can be described as well.

## xml in brief
1. XML is a simplified version of SGML, a long-term used language
for technical documents.
2. HTML, up to version 4.0, is also a variant of SGML. The successor of HTML 4.0, is XHTML, an XML dialect.

## XML documents
- An XML document is a labeled, unranked, ordered tree:
  - **Labeled** means that some annotation, the label, is attached to each node.
  - **Unranked** means that there is no a priori bound on the number of children of a node.
  - **Ordered** means that there is an order between the children of each node.
- XML specifies nothing more than a syntax: no meaning is attached to the labels.

## XML documents are trees
![picture 8](images/d82d1e28eab15d450623d94df473f8a33a608668c8e3674ebe7eb94a32f42a79.png)  

## Serialized representation of XML document
![picture 9](images/5f008052ae1d25f06b5f6d4f312a068dc5955d66c30a47d2015c7e4a5df5fff6.png)  

## XML describes structured content
![picture 10](images/f5746ee170f5fd082d41c9e2fa141a9cf3c1ce39cf2aefe9b97fd868895445be.png)  

# xml syntax
## Serialized form, tree form
Typically, an application gets a document in serialized form, parse it in tree form, and serializes it back at the end.
![picture 19](images/b563c456813296a2e1256378c52a4e125dd7f378de05202c43fea1e716b3f51d.png)  

- The serialized form is a textual, linear representation of the tree; it complies to a (sometimes complicated) syntax;
There exist an **object-oriented model for the tree form**: the **Document Object Model**(DOM) (W3C).

## The syntax for serialized document, in brief
![picture 20](images/7fe7757c5c2e01b3e174e5fabd637cd1014f78be480b43d96bd304191553686e.png)  

## From serialized to tree form: 
### text and elements
![picture 21](images/59f18816081f7ae67e29f522e4bb797c97ba9499a65c03109df254ac6e2a8364.png)  

### nesting elements
![picture 22](images/0b5749d042d44974c9fa3658d84164cde7a871757d2e5f9cf95bf0f8ece9cbc9.png)  

### attributes
![picture 23](images/d426518614df95f164ac917ca891a72c1d0c28e30e7931feb54c5dccfd232f40.png)  
- Unlike elements, attributes are **not ordered**, and **there cannot be two attributes with the same name in an element**.
### the document root
![picture 24](images/be4bd1706323a784d1a331537a7ddd1e6fe757d27c6afd1a81cd5111fb17338e.png)  

## summary: syntax and vocabulary
- Serialized form
  - A document begins with a prologue,
  - It consists of a single upper-level tag,
  - Each opening tag <name> has a corresponding closing tag </name>; everything between is either text or properly enclosed tag content.
- Tree form
  - A document is a tree with a root node (Document node in DOM),
  - The root node has one and only one element child (Element node in DOM), called the element root)
  - Each element node is the root of a subtree which represents its
  structured content
## Entities and references
- Entities are used for the physical organization of a document.
- An entity is **declared** (in the document type), then **referenced**.

![picture 25](images/7c43c79e5397449f3e54e189eaab4d3d4b3c5778bda93a561dd91bc1445c2610.png)  

## Predefined entities
- Several symbols cannot be directly used in an XML document, since they would be misinterpreted by the parser.
- They must be introduced as entity references.
![picture 26](images/21b14fb75c742bcdffb2d175f3004d66c4d9ee3d0a1bff6dfc59dc7557d2b7d3.png)  

## Comments and instructions
Comments can be put at any place in the serialized form.
- They appear as Comment nodes in the DOM tree (they are typically ignored by applications).
- Processing instructions: specific commands, useful for some applications, simply ignored by others.
![picture 1](images/3f0c6895f49dd46ab5900c0f4077dfed006a4353c592cc146b6400d56a63a88d.png)  

## Literal sections
![picture 27](images/a8b80573c758c9436e7bf50c1a03be4c9ac1fa81b5275b25e721225ee0bd392a.png)  

# Typing
## To type or not to type
- What kind of data: very regular one (as in relational databases), less regular
(hypertext systems) - all kind of data from very structured to very unstructured.
- What kind of typing (unlike in relational systems)
  - Possibly irregular, partial, tolerant, flexible
  - Possibly evolving
  - Possibly very large and complex
  - Ignored by some applications such as keyword search.

**Typing is not compulsory.**

## Type declaration
- XML documents may be typed, although they do not need to. The simplest (and oldest) typing mechanism is based on **Document Type Definitions (DTD)**.
- A DTD may be specified in the prologue with the keyword **DOCTYPE** using an ad hoc syntax.

![picture 28](images/af3180ea8917f6a1178eb1eecdc2ac2550d11c0cc99e801aea6bd51ffc3e4263.png)  

## Document Type Definition
![picture 29](images/91c6897c2a34bbae87efdbf505d0bfc51a99bdd9a7fe328925b1e5899cb6d088.png)  

- A DTD may also be specified externally using an URI.
![picture 30](images/1dd962c2d74b9cba50c23eb3fe014e2317318617ce98df73bbd2a968e35ac720.png)  

## Interpreting labels: Namespaces
A particular label, e.g., job, may denote different notions in different contexts, e.g., a hiring agency or a computer ASP (application service provider).
The notion of namespace is used to distinguish them
![picture 31](images/16344a48d0905d9eaafb6d56bdc566d64d442cd862c38f6f2d3c16a648b78b3a.png)  

## DTD vs. XML schema
DTD: old style typing, still very used
XML schema: more modern, used e.g. in Web services
![picture 32](images/0d599acfe665a67a55755c016526ea61ff4cf0e5edd8a80994826d528a99bb8c.png)  
![picture 33](images/95ff559bca5df7a82f5877841cc62f1b430ff0dfe8578070c642fc4c52db99da.png)  

# The XML world
## Popular XML dialects
![picture 2](images/24960dead31f992525501a5189c83c43906dadd7d022ed429c374c8607109d9e.png)  

## XML standards
![picture 3](images/109a16e40180b7115c2868ec9ee7193191df493d6c1df226abef172cacd5631c.png)  

## Zoom:
### DOM
- Document Object Model - DOM
- Document model that is tree-based
- Used in APIs for different programming languages (e.g. Java)
- Object-oriented access to the content:
  - Root of the document
  - First child of a node (with a particular label)
  - Next one (with a particular label)
  - Parent of a node
  - Attribute of a node...

### XPATH
- Language for expressing **paths** in an XML document
  - Navigation: child, descendant, parent, ancestor
  - Tests on the nature of the node
  - More complex selection predicates
- Means to specify portions of a document
- Basic tool for other XML languages: Xlink, XSLT, Xquery

### XLINK
- XML Linking Language
- Advanced hypertext primitives
- Allows inserting in XML documents descriptions of links to external Web resources
- Simple monodirectional links ala (HREF) HTML
- Mulridirectional links
- XLink relies on XPath for addressing portions of XML documents
- XML trees + XLINK ⇒ graph

### XSLT
- Transformation langage: “Perl for XML”
- An XSLT style sheet includes a set of transformation rules: pattern/template
- Pattern: based on XPATH expressions; it specifies a structural context in the
tree
- Template: specifies what should be produced
- Principle: when a pattern is matched in the source document, the corresponding templates produces some data

### XQuery
- Query language: “SQL for XML”
- Like SQL: select portions of the data and reconstruct a result
- Query structure: FLW (pronounced "flower")
- Exemple
```
    FOR $p IN document("bib.xml")//publisher
    LET $b := document("bib.xml)//book[publisher = $p]
    WHERE count($b) > 100
    RETURN $p
```
- $p : scans the sequence of publishers
- $b : scans the sequence of books for a publisher
- WHERE filters out some publishers
- RETURN constructs the result

# Use Cases
## Exploiting XML content
- Publishing: an XML document can easily be converted to another XML document (same content, but another structure)
  - ⇒ Web publishing is the process of transforming XML documents to XHTML.
- Integration: XML documents from many sources can be transformed in a common dialect, and constitute a collection.
  - ⇒ Search engines, or portals, provide browsing and searching services on collections of XML documents.
- Distributed Data Processing: many softwares can be adapted to consume/produce XML-represented data.
  - ⇒ Web services provide remote services for XML data processing.

## Web Publishing
### restructuring to XHTML
- The Web application produces some XML content, structured in some application-dependent dialect, on the server.
- In a second phase, the XML content is transformed in an XHTML document that can be visualized by humans.
- The transformation is typically expressed in XSLT, and can be processed either on the server or on the client.
![picture 4](images/a812af2f930d7e54c419f6dc73a85612c234e85edba366545ddd3c122702dd79.png)  

### content + presentation instructions
![picture 5](images/e6dcd7c843e1a4f971e4de9b214da292a2828743b503ad51b624f2c1e65b9e23.png)  

![picture 6](images/08821a80a8c49e13bc78a5b90864860998e9da0a716639529af197e14a81ffee.png)  
![picture 7](images/72632f8dac0d604e8c63c894a9779ecbf8480b852d348da3a4bacbe8ea3a623f.png)  

## Web Integration: gluing together heterogeneous sources
![picture 8](images/73190da10651f3cc80f37eeda336baa338aca5c21b78b12cf5abc47877f67c7b.png)  

## Data integration, a larger perspective
![picture 9](images/a4a02932ed627003d6589096213dbc0cefe7f04c2d147515aafb17567e6a28a7.png)  

## Distributed Data Management with XML
![picture 10](images/0c67a25856733d67497df51ff6c90ec29a03472cf5db9837141af919d9a6e5c5.png)  

## Exploiting XML documents: the big picture
![picture 11](images/5283a71a0de3cd2fc2bcfc0b54bfeea6b92d8e2f57d18786d16195c53b2f1b16.png)  
