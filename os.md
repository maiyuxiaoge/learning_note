![picture 11](images/9e7840815eeaed31c2dba40acf625d1d8a860b5e8b94d20fefa3ccc0686598c6.png)  
# introduction
## what is an operating system
- software that makes computer easier to use
- improves the computer's capabilities
  - performance:speed,efficiency
  - reliability:correctness,fault tolerance
  - security: privacy,authenticity,integrity

## operating system vs. the Kernel
- our focus is much more limited:kernel

## two purposes of the kernel
- to provide abstract machine
- to manage resources

![picture 12](images/360d0cf5d9f8da7802754921a0be6af4cb938713263fb5fc7013eb6ed23ab45b.png)  

## turn undesirable into desirable
- Undesirable inconveniences of	reality
  - Complexity	of	hardware	
  - Single/limited	number	of	processors	
- Small/limited	amount	of	memory	
- Desirable	conveniences:	illusions	
  - Simple,	easy-to-use	resources	
  - Multiple/unlimited	number	of	processors	
  - Large/unlimited	amount	of	memory	


## From	Programmer’s Point of View
- Algorithm/program	design is hard	enough!	
- Allow	programmer to focus	on algorithm design	
- Not how to make machine run the	algorithm	
- Minimize accounting for computer	limitations	
- Introduces unnecessary complexity	
- May lead to modifying	the	algorithm	
- May make the	program	not	portable	

## Three Key Ideas
- Abstraction	
  - What is	the	desired	illusion	
- Mechanism	
  - How	to create illusion:	basic	functionality	
  - Fixed: works one way, the only	way	
- Policy	
  - Which way to use mechanism, to meet a goal	
  - Variable: many possible, select	best for situation

# processes
## Basic	Resources	for	Processes
- CPU	
  - Processing	cycles	(time)	
  - To	execute	instructions	
- Memory	
  - Bytes	or	words	(space)	
  - To	maintain	state	
- Other	resources	(e.g.,	I/O)
## Context	of	a	Process
- Context:	machine	and	kernel-related	state	
- CPU	context:	values	of	registers	
  - PC	(program	counter)	
  - SP	(stack	pointer),	FP	(frame	pointer),	GP	(general)	
- Memory	context:	pointers	to	memory	areas	
  - Code,	static	variables	(init,	uninit),	heap,	shared,	…	
  - Stack	of	activation	records	
- Other	(kernel-related	state,	…)	

## Process	Memory	Structure
- Text	
  - Code:	program	instructions	
- Data	
  - Global	variables	
  - Heap	(dynamic	allocation)	
- Stack	
  - Activation	records	
  - Automatic	growth/shrinkage

![picture 13](images/c570f2c19c1e42017340b74d803dd2f9b60cb697f798c760a9d22489f0a9967b.png)  


## process stack
- Stack	of	activation	records	
  - One	per	pending	procedure	
- An	acitvation	record	may	store	
  - where	to	return	to	
  - link	to	previous	record	
  - automatic	(local)	variables	
  - other	(e.g.,	register	values)	
- Stack	pointer	points	to	top
![picture 14](images/d3d1eb530af5b130513aa8b2415587f2952848a99b891845f51c90cd809ad584.png)  


## Goal:	Support	Multiple	Processes
## Multiprogramming
- Given	a	running	process	
  - At	some	point,	it	needs	a	resource,	e.g.,	I/O	device	
  - Say	resource	is	busy,	process	can’t	proceed	
  - So,	“voluntarily”	gives	up	CPU	to	another	process	
- yield	(p)	
  - Let	process	p	run	(voluntarily	give	up	CPU	to	p)	
  - Requires	context	switching

## Context	Switching
- Allocating	CPU	from	one	process	to	another	
  - First,	save	context	of	currently	running	process	
  - Next,	restore	(load)	context	of	next	process	to	run	
- Loading	the	context	
  - Load	general	registers,	stack	pointer,	etc.	
  - Load	program	counter	(must	be	last	instruction!)	

## Simple	Context	Switching
- Two	processes:	A	and	B
-  A	calls	yield(B)	to	voluntarily	give	up	CPU	to	B	
- Save	and	restore	registers	
  - General-purpose,	stack	pointer,	program	counter	
- Switch	text	and	data	
- Switch	stacks	
  - Note	that	PC	is	in	the	middle	of	yield!	

## The	magic	of	yield
![picture 15](images/eb6bdb0e271e4f557282e569802410ec1b93f21b8be71f2d375f55705783a5ee.png)  
## Example
![picture 16](images/fde4cfb036ab0bb4f95a2d3008c58740c6fafa393ba12c7499c4bdbb7c9af3e0.png)  
![picture 17](images/62327edf3c151af5e0d3422eea18a2efe03a93c11f192d723b910fd960ebde95.png)  

## yielding via kernel
- yield	routine	is	common	code:	put	in	kernel	
- Process	contexts	are	also	in	the	kernel	
  - This	way	they	are	protected	
  - Only	needed	by	yield	routine	anyway	
- But	what	is	the	kernel?	
  - code	that	supports	processes	
  - runs	as	an	extension	of	current	process	
- Has	text,	data,	and	multiple	stacks

![picture 18](images/007e29e120b273d50b47739a259bf779f17f539763453cc954251eb15934d266.png)  


# Timesharing
## time sharing
![picture 35](images/f9ec7fec7b4389eb1759ae5f99acc82c21f29f0ff89c9c64f9493092756ff080.png)  

- Timesharing:	multiplexing	use	of	CPU	over	time	
- Multiple	processes,	single	CPU	(uniprocessor)	
- Conceptually,	each	process	makes	progress	over	time	
- In	reality,	each	periodically	gets	quantum	of	CPU	time	
- Illusion	of	parallel	progress	by	rapidly	switching	CPU	

## How	is	Timesharing	Implemented?
- Kernel	keeps	track	of	progress	of	each	process	
- Characterizes	state	of	process’s	progress	
  - Running:	actually	making	progress,	using	CPU	
  - Ready:	able	to	make	progress,	but	not	using	CPU	
  - Blocked:	not	able	to	make	progress,	can’t	use	CPU	
- Kernel	selects	a	ready	process,	lets	it	run	
  - Eventually,	the	kernel	gets	back	control	
  - Selects	another	ready	process	to	run,	…	

## Process State Diagram
![picture 36](images/ae508341b51b9a3a08f8a4485fd7fd30742451bfd016c1f64faf4a0d1dcde7d7.png)  
State	transitions	
  - Dispatch:	allocate	the	CPU	to	a	process	
  - Preempt:	take	away	CPU	from	process	
  - Sleep:	process	gives	up	CPU	to	wait	for	event	
  - Wakeup:	event	occurred,	make	process	ready	

## Logical	vs.	Physical	Execution
![picture 37](images/e5ecbffc9a98655d74c4cfff23ad427e1f30a18a7a2b0243f32f22b5d77cf507.png)  

## Process	vs.	Kernel
- Kernel:	code	that	supports	processes	
  - system	calls:	fork	(	),	exit	(	),	read	(	),	write	(	),	…	
  - management:	context	switching,	scheduling,	…
- When	does	the	kernel	run?	
  - system	call
  - hardware	interrupt	occurs	
- The	kernel	runs	as	part	of	the	running	process	
  - due	to	that	process	having	made	a	system	call	
  - in	response	to	device	issuing	interrupt	

## Process	Running	in	User	Space
![picture 38](images/fa11d6ae7b28e71173994a80af81fe72a5c39b22659418baffc6d2d17dd106d5.png)  

## Process	Running	in	Kernel	Space
![picture 39](images/2e8d0191107ac4d5ed7c0040eb48a35a74b2a1430729402017b8c8b95024f95b.png)  

## Kernel	Maintains	List	of	Processes
![picture 40](images/c1001e1f5c161d59cd18b727701efe8fb322ec99b9414949bed89d540ba6bd9b.png)  
- All	processes:	unique	names	(IDs)	and	states	
- Other	info	kernel	needs	for	managing	system	
  - contents	of	CPU	contexts	
  - areas	of	memory	being	used	
  - reasons	for	being	blocked	

- How	Does	Kernel	Get	Control	
  - Process	can	give	up	control	voluntarily	
  - Makes	system	call	that	blocks,	e.g.,	read	()	
  - System-call	function	calls	yield	()	to	give	up	CPU	
  - Kernel	selects	a	ready	process,	dispatches	it	
- Or,	CPU	is	forcibly	taken	away:	preemption	
  - Interrupt	generated	when	hardware	timer	expires	
  - Interrupt	forces	control	to	go	to	kernel	
  - While	kernel	running,	resets	timer	for	next	time

## How	a	Context	Switch	Occurs
- Process	makes	system	call	or	interrupt	occurs	
- What’s	done	by	hardware	
  - Switch	from	user	to	kernel	mode:	amplifies	power	
  - Go	to	fixed	kernel	location:	trap/interrupt	handler	
- What’s	done	in	software	(in	the	kernel)	
  - Save	context	of	current	process	
  - Select	a	process	that	is	ready;	restore	its	context	
  - RTI:	return	from	interrupt/trap

## How	to	Get	Parallelism	in	Process
- Process	is	a	“program	in	execution”	
  - assumed	(so	far)	a	single	path	of	execution	
  - in	a	memory	composed	of	text,	data,	stack	
- What	if	we	want	multiple	paths	of	execution?	
  - Single	text,	but	multiple	executions	in	parallel	
  - Single	data,	any	execution	can	see	others’	updates	
  - Need	separate	stacks:	one	per	ongoing	execution	
- Multiple	processes?		No	(separate	memories)

## Threads	
- Thread:	single	sequential	path	of	execution	
- Abstraction	is	independent	of	memory	
  - Contrast	to	process:	path	of	execution	+	memory	
- A	thread	is	part	of	a	process	
  - Lives	in	the	memory	of	a	process	
  - Distinction	allows	multiple	threads	in	a	process	
- To	the	user:	unit	of	parallelism	
- To	the	kernel:	unit	of	schedulability

- Implementing	Threads
- Thread	calls	are	system	calls	
  - ForkThread():	like	process	Fork()	but	for	threads	
  - Thread	system	call	functions	are	in	kernel	
- Thread	management	functions	are	in	kernel	
  - Thread	context	switching	
  - Thread	scheduling	
- Each	thread	requires	user	and	kernel	stacks	
- Kernel	can	schedule	threads	on	separate	CPUs

## Single	Process,	Multiple	Threads	
![picture 41](images/76669980ab613add2643771a2b1b2af98792c65bfc50faacf0baef142cafe7fc.png)  

## Many	Processes	with	Threads
![picture 42](images/28f5c21723a60746714132a11725f9dd95b9cb10f778c9c8b4c86fa90a125e3d.png)  

## User-Level	Threads
- Can	support	threads	at	user	level	
- Included	via	thread	library	
- Thread	calls	at	user	level	
  - ForkThread	(),	YieldThread	(),	…	
- Thread	Management	at	user	level	
- Supports	threads	regardless	of	kernel	support	
- However,	no	true	parallelism	
![picture 43](images/76bacfab67028c8f5acc2571dff8354eeb11423d267a4534ed7b65c9450728db.png)  
![picture 44](images/e29a73705060f1d3afcb5dc15a22738de85a90e21495f79374bddbfb5c0f9abc.png)  

## Pros	and	Cons
- User-level	threads	
  - Portability:	works	on	any	kernel	
  - Efficient:	thread-switching	occurs	in	user	space	
  - User	can	decide	on	scheduling	policy	
  - But	no	true	parallelism	(without	special	support)	
- Kernel-level	threads	
  - Can	achieve	true	parallelism	
  - Overhead:	thread	switch	requires	kernel	call	

## Thread	Support	vs.	Execution
- Distinguish	between	
  - Where	is	thread	abstraction	supported?	
  - Where	is	thread	executing?	
- User-level	vs.	kernel-level	threads	
  - Is	thread	support	part	of	user	or	kernel	code?	
- Running	in	user	space	vs.	kernel	space	
  - Is	thread	running	in	user	or	kernel	space?	
- Make	sure	you	understand	the	distinction!

# Scheduling
## There	is	No	Single	Best	Policy
Different	for	
– your	personal	computer	
– large	time-shared	computer	
– computer	controlling	a	nuclear	power	plant	

## Longest	First	vs.	Shortest	First
![picture 1](images/4cfeca62de127f97863b692089a42b025c1fe5bd5a09c9f8816a34265af72a8f.png)  

- Given	n	processes	with	service	times	S1,	…	,	Sn
  - Note:	processes	are	numbered	1,	2,	3,	…,	n	
-  Average	turnaround	time	computed	as	follows
   - [S1	+	(S1	+	S2)	+	(S1	+	S2	+	S3)	+	…	+	(S1	+	…	+	Sn)]	/	n	
   - [(n	×	S1)	+	((n-1)	×	S2)	+	((n-2)	×	S3)	+	…	+	Sn]	/	n
- In	general:	order	by	shortest	to	longest	

## Consider	Different	Arrival	Times
![picture 2](images/4af06222f375eedafade25a5fae98f215528773963fa5a4d9e22422f28f877da.png)  

## FCFS:	First	Come	First	Served
![picture 3](images/2170b0f40452179237c11239998b4b4b183c121dee4297709598883b93e9f673.png)  
- Average	turnaround	time	=	(5	+	7	+	7)/3	=	6.3	
- Non-preemptive,	simple,	no	starvation	
- Poor for short	processes	

## RR: Round	Robin
![picture 4](images/daabb31a7e5395938d45654053956c4d096b145a0ed488cdd880f28d7168ce1c.png)  
- Average	turnaround	time	=	(9	+	6	+	2)/3	=	5.7	
- Preemptive,	simple,	no	starvation	
- Process	waits	at	most	(n	-	1)	x	quantum	

## SPN:	Shortest	Process	Next
![picture 5](images/ef052d248d9dbb3abc5dfa95318064ca6d65451c257952b90af817d148af54fd.png)  
- Average	turnaround	time	=	(5	+	8	+	4)/3	=	5.7	
- Optimal	for	non-preemptive,	allows	starvation	
- Assumes	service	times	are	known	

## SRT:	Shortest	Remaining	Time
![picture 6](images/74874fc171dcc0bcd56fcf01a28fd0b3e183811334a0df54b837cd4166a482a0.png)  
- Average	turnaround	time	=	(9	+	4	+	1)/3	=	4.7	
- Assumes	service	times	are	known	
- Optimal	for	preemptive,	but	allows	starvation	

## Multi-Level	Feedback	Queues
- Priority	queues:	0	(high),	…,	N	(low)	
- New	processes	enter	queue	0	
- Select	from	highest	priority	queue	
- Run	for	T	=	2k quantums
  -  Used	T:	move	to	next	lower	queue,	FIFO	
  -  Used	<	T:	back	to	same	queue,	RR	
-  Due	to	yield	or	higher	priority	arrival	
- Periodically	boost	(e.g.,	all	to	highest	queue)

![picture 7](images/52b0548ed5bbd8f969aebbac525f9f450c2eedb8dac6d723c54bb749b524fd90.png)  
![picture 8](images/e4e5207946cf0f30063901b56070d1ffbf6cb75520d7afe15ad88dba8dd4e6ff.png)  
- Average	Turnaround	Time	=	(9	+	6	+	1)/3	=	5.3	
- Complex,	adaptive,	highly	responsive	
- Favors	shorter	over	longer,	possible	starvation

## Priority	Scheduling
![picture 9](images/19d3b3915d228c747ade3c617c1dd9ec0b83b814d2ef589254d2539384d74750.png)  
- Allows	scheduling	based	on	external	criteria	
  - E.g.,	priority	=	1/CPU_time_used,	or	=	f	(pay)	

## Fair	Share	(Proportional	Share)	
![picture 10](images/1dc7450d4f514e7f03e4a81d3eb4bb4efd8a61ab3c678689cb1a87dd2b2457ed.png)  
- Goal:	utilization	over	long	run,	actual	≈	request	
- How	do	we	determine	who	runs	each	quantum?	
- Select	process	with	minimum	actual/request	ratio	

## Stride	Scheduling	
- For	processes	A,	B,	C	…	with	requests	RA,	RB,	RC	…	
- Calculate	strides:	SA	=	1/RA,	SB	=	1/RB,	SC	=	1/RC	…	
- For	each	process	x,	maintain	pass	value	Px	(init	0)	
- Schedule:	repeat	every	quantum	
  - Select	process	x	with	minimum	pass	value	Px,	run	
  - Increment	pass	value	by	stride	value:	Px	=	Px	+	Sx
- Optimization:	use	only	integers	for	Rx,	Sx	and	Px		
  - Calculate	Sx	=	L/Rx	using	very	large	L,	e.g.,	L	=	100000

## Stride	Scheduling	Example
![picture 11](images/94f1a1e36948ed9d37c6dfbe56f50870d4d6cf0bf9ed5ec68146d2159843defb.png)  


## Real	Time	Scheduling
- Correctness	of	real-time	systems	depend	on	
  - logical	result	of	computations	
  - and	the	timing	of	these	results	
- cType	of	real-time	systems	
  - Hard	vs.	soft	real-time	
  - Periodic	vs.	aperiodic
- Scheduling	
  - Earliest	Deadline	First	(EDF)	
  - Rate	Monotonic	Scheduling	(RMS)	

## Periodic	Processes	(or	Tasks)
![picture 1](images/a7898abfe234f01a68d1742b4d4ed6ec013a7010c26342dd6ac9089b595c5713.png)  
- Periodic	processes:	computation	is	cyclic	
- For	each	process,	given	
  - C	=	CPU	burst,	T	=	period,	U	=	C/T	=	utilization	

## EDF:	Earliest	Deadline	First
![picture 2](images/474f931a542c641764d24551fb2532cf21ec5bf77db72a5100797cadb08b7ea6.png)  
- Schedule	process	with	earliest	deadline	
- If	earlier	deadline	process	appears,	preempt	
- Works	for	periodic	and	aperiodic	processes	
- Achieves	100%	utilization	(ignoring	overhead!)	
- Expensive:	requires	ordering	by	deadlines	

![picture 3](images/999dc4e895dbbde66077fdbd9ae73fd09a45e2e0d18ef7b5e937f917cf62ce69.png)  

## RMS:	Rate	Monotonic	Scheduling	
![picture 4](images/0f4138f236b6126a06255b58668ac4c465735be19d6a83a76f72b4af0b95c78a.png)  

- If	periodic	processes,	prioritize	based	on	rates	
- At	start	of	period,	select	highest	priority	
- Preempt	if	necessary	
- When	burst	done,	wait	till	next	period	
- If	U1	+	…	+	Un	≤		n	($2^{1 / n}$	–	1),	all	deadlines	met

### RMS	Test	Passes,	All	Deadlines	Met	
![picture 5](images/42460e4170e5a24b1eefbd69f74e7f553f738dc38e805e1193be47bfea830f10.png)  

### RMS	Test	Fails,	Deadline	Missed
![picture 6](images/52ad12b2af82e4ac4df2fd74cb57aff434e326482722d928c2e15002e456e02a.png)  

### RMS	Test	Fails,	But	Deadlines	Met
![picture 7](images/2050d1ac30cfa22d3a96b50fa5d6a83b3bd1dbbf4728b66bf1742a04f833a950.png)  

## RMS	Optimal	But	Limited
- RMS	is	simple	and	efficient	
  - Static	priority	scheduling	based	on	rates	
- RMS	is	optimal	for	static	priority	algorithms	
  - If	RMS	can’t	schedule,	no	other	static	priority	can	
- RMS	is	limited	in	what	it	guarantees	
  - Utilization	bounded	by	n	(21/n	–	1)	>	ln	2	≈	69%	
  - Deadline	guarantee	applies	only	if	test	passes	
- RMS	is	limited	to	periodic	processes	

## Summary
- CPU	scheduling	is	policy:	depends	on	goals


|  scheduling  | property  |
|  :---:  | :---:  |
| First	come	first	served | very	simple,	non-preemptive |
| Round	robin|simple,	preemptive |
| Shortest	process	next | theoretical,	non-preemptive |
| Shortest	remaining	time | theoretical,	preemptive	|
| Multi-level	feedback | adaptive,	responsive,	complex	|
| Priority| external	criteria |
| Fair	share | proportional	allocation	|
| Earliest	deadline	firs | 100%	utilization,	high overhead	|
| Rate	monotonic	sched | <	100% util,	low	overhead |


# Synchronization
## Synchronization
- Synchronize:	events	happen	at	the	same	time	
- Process	synchronization	
  - Events	in	processes	that	occur	“at	the	same	time”	
  - Actually,	when	one	process	waits	for	another	
-  Uses	of	synchronization	
   - Prevent	race	conditions	
   - Wait	for	resources	to	become	available

## The	Credit/Debit	Problem
- Say	you	have	$1000	in	your	bank	account	
- You	deposit	$100	
- You	also	withdraw	$100	
- How	much	should	be	in	your	account?	
-  What	if	deposit/withdraw	occur	at	same	time?

## Credit/Debit	Problem:	Race	Condition	
![picture 8](images/3d697201c5b730a89529676c8a3f9dfb6d2ada0a52864be9a74c8f592073b92d.png)  

## To	Avoid	Race	Conditions
- Identify	related	critical	sections	
  - Section(s)	of	code	executed	by	different	processes	
  - Must	run	atomically,	with	respect	to	each	other	
- Enforce	mutual	exclusion	
  - Only	one	process	active	in	a	critical	section

## What	Does	Atomic	Really	Mean?
- Atomic	means	“indivisible”	
- We	seek	effective	atomicity	
  - can	interrupt,	as	long	as	interruption	has	no	effect	
-  It	is	OK	to	interrupt	process	in	critical	section	
  -  as	long	as	other	processes	have	no	effect	
- How	to	determine	
  - Consider	effect	of	critical	section	in	isolation	
  - Next	consider	interruptions:	if	same	result,	OK

## How	to	Achieve	Mutual	Exclusion?
- Surround	critical	section	with	entry/exit	code	
- Entry	code	should	act	as	a	barrier	
  - If	another	process	is	in	critical	section,	block	
  - Otherwise,	allow	process	to	proceed	
- Exit	code	should	release	other	entry	barriers

## Requirements	for	Good	Solution
- Given	multiple	cooperating	processes	
  - Each	process	has	a	critical	section	
  - All	critical	sections	are	to	be	mutually	exclusive	
1. At	most	one	in	a	critical	section	at	a	time	
2. Can’t	prevent	entry	if	all	others	not	in	theirs	
3. Should	eventually	be	able	to	enter	
4. No	assumptions	about	CPU	speed	or	number

## Software	Lock?
![picture 9](images/57bebfde99024cb14d291e7e4d4597a3ec064341521382c2ad574fca727c7283.png)  
- Lock	indicates	if	any	process	in	critical	section

## Take	Turns?
![picture 10](images/65bf5b51b8623afa1d07aed2accc47c4c9b0ab47fb7ce19c2ede03465488836f.png)  
- Alternate	which	process	enters	critical	section

## State	Intention?
![picture 11](images/8dce69f543aba74f70b0ebfd69d8fbe6ddee49e776eca27f3cffe5c83129eac0.png)  

- Process	states	intent	to	enter	critical	section

## Peterson’s	Solution
![picture 12](images/8f5d7330440ed8834167355d0c784ba2feda432ee2c67a19473f21f61d4db4cc.png)  
- If	competition,	take	turns;	otherwise,	enter	
- There	is	a	version	for	n	>	2;	more	complex

# What	about	Disabling	Interrupts?
- No	interrupts	⇒	no	uncontrolled	context	switches(just yield)
- No	uncontrolled	context	switches	⇒	no	races	
- No	races	⇒	mutual	exclusion	

# Test-and-Set	Lock	Instruction:	TSL
- TSL	mem	(test-and-set	lock:	contents	of	mem)
  - do atomically (i.e., locking the memory bus) [ test if mem == 0 AND set mem = 1 ]
- Operations	occur	without	interruption	
  - Memory	bus	is	locked	
  - Not	affected	by	hardware	interrupts

## What	TSL	Does,	Expressed	in	C	
Assume	C	function,	TSL(int	*),	that	is	atomic	
```c
TSL(int *lockptr)
{ 
  int oldval;
  oldval = *lockptr
  *lockptr = 1;
  return ((oldval == 0) ? 1 : 0);
} 
```
## Mutual	Exclusion	Using	TSL
![picture 4](images/29494ebd5195cc18c1e475f5739d4c49ca077be0c7720752231d923e19d7cd90.png)  
- Shared	variable	solution	using	TSL(int	*)	
  - tests	if	lock	==	0	(if	so,	will	return	1;	else	0)	
  - before	returning,	sets	lock	to	1	
- Simple,	works	for	any	number	of	threads	
- Still	“suffers”	from	busy	waiting	

# Semaphores
- Synchronization	variable	
  - Takes	on	integer	values	
  - Can	cause	a	process	to	block/unblock	
- wait	and	signal	operations	
  - wait	(s) decrement;	block	if	<	0	
  - signal	(s) increment;	if	any	blocked,	unblock	one	
- No	other	operations	allowed	
  - In	particular,	cannot	test	value	of	semaphore!	

## Examples	and	Interpretation
- wait	(s) decrement;	block	if	<	0	
- signal	(s) increment;	if	any	blocked,	unblock	
- wait	(1) s	→	0 -	GO	
- wait	(0) s	→	-1 -	STOP	(i.e.,	block)	
- signal	(-1) s	→	0 -	GO	and	allow	one	to	GO	
- signal	(0) s	→	1 -	GO

## USAGE1:Mutual	Exclusion
![picture 5](images/f2a16c71d1900b5714d4bd5f641c0ec50c3f772fb8f426e1bbe3cf00b498dea7.png)  

## USAGE2: Order	How	Processes	Execute
![picture 6](images/6db89081d47304781b5d5daf5b8b60624a1053a222dbbcca00b5c58bae27be65.png)  
- Cause	a	process	to	wait	for	another	
- Use	semaphore	indicating	condition;	initially	0	
  - the	condition	in	this	case:	“P0	has	completed”	
- Used	for	ordering	processes	
  - In	contrast	to	mutual	exclusion	

## Semaphore	Implementation
![picture 7](images/914b9d0b69fe468b337aa9fac72cd24e483f1409053035a581c8fd4d21bdd9ea.png)  

## Alternative	Implementation
![picture 8](images/3f9f3b3d7b16619caeb7595d4875736af7d3149b82ff50c48d023b7106999c11.png)  

## Wait	and	Signal	Must	Be	Atomic
- Bodies	of	wait	and	signal	are	critical	sections	
- So,	still	need	mechanism	for	mutual	exclusion!	
- Use	a	lower-level	(more	basic)	mechanism	
  - Test-and-set	lock	
  - Peterson’s	solution	
- So,	busy-waiting	still	exists	(can	never	remove)	
  - But	at	lower-level	(within	semaphore	operations)	
  - Occurrence	limited	to	brief/known	periods	of	time	

## Analysis:	Lower-Level	Busy	Waiting	
- A	calls	wait	(s),	switch	to	B,	B	calls	wait	(s)	
  - Switch	occurs	while	A	executing	body	of	wait	
- Body	of	wait	is	critical	section,	so	B	must	block	
  - Use	test-set	lock	or	Peterson’s:		busy	waiting	
- How	long	will	B	be	blocked?	
  - For	time	it	takes	to	execute	body	of	wait	
- Small/known	amount	of	time!	
  - Compare	to	user	critical	section:	unknown	time

## Are	These	Equivalent?
![picture 9](images/e4aad80f08df42981b38e0da1d1fc15f15326a7c8f6c2b0b965d2995d092f406.png)  

- no  implementation2 has bug in wait
- \+ and \- has to be finished in the first line


# InterProcess Communication	(IPC)
## Cooperating	Processes	
- Performance:	speed	
  - Exploit	inherent	parallelism	of	computation	
  - Allow	some	parts	to	proceed	while	others	do	I/O	
- Modularity:	reusable	self-contained	programs	
  - Each	may	do	a	useful	task	on	its	own	
  - May	also	be	useful	as	a	sub-task	for	others	

## Examples	of	Cooperating	Processes
![picture 1](images/f21a4cfeaf6278f98a84df6b7dc0f695034b2c2d1fb5ef5aa9d5ae1964a74396.png)  


## Inter-Process	Communication	
- To	cooperate,	need	ability	to	communicate	
- IPC:	inter-process	communication	
  - Communication	between	processes	
- IPC	requires	
  - data	transfer
  - synchronization	
- Need	mechanisms	for	both

- Semaphore is not IPC(no data transfer)

## Three	Abstractions	for	IPC
- Shared	memory	+	semaphores	
- Monitors	
- Message	passing	

## The	Producer/Consumer	Problem
![picture 2](images/89ac5da7fdd0f36ebe4cfb920bec5e7f3ff1fe98a32a72ca33abac4bdbc14116.png)  

- Producer	produces	data,	inserts	in	shared	buffer	
- Consumer	removes	data	from	buffer,	consumes	it

## Producer/Consumer:	Shared	Memory
![picture 3](images/7aa9c8a3ef337fdb5942c5ce43cb1022584d1800e3ed6bf8f05deed0ae3f9c36.png)  

- No	synchronization	
  - Consumer	must	wait	for	something	to	be	produced	
- What	about	Producer?	
  - No	mutual	exclusion	for	critical	sections	
  - Relevant	if	multiple	producers	or	multiple	consumers

## Recall	Semaphores
- Semaphore:	synchronization	variable	
  - Takes	on	integer	values	
  - Has	an	associated	list	of	waiting	processes	
-  Operations	
   - wait	(s) {	s	=	s–1;	block	if	s	<	0	}	
   - signal	(s) {	s	=	s+1;	unblock	a	process	if	any	}	
- No	other	operations	allowed	(e.g.,	can’t	test	s)

## Semaphores	for	Synchronization	
![picture 4](images/52ef2715e89282f23fef48aaf0395ddf580e3287e4a29359ba7c30580040aba3.png)  
- Buffer	empty,	Consumer	waits	
- Buffer	full,	Producer	waits	
- General	synchronization	vs.	mutual	exclusion	


## Multiple	Producers
![picture 5](images/dbfa571e081baa14a6cfb5642caa99c7d0e04f5855fbd719d81038f5e0a269f2.png)  
- There	is	a	race	condition	in	the	Producer	code	
- Inconsistent	updating	of	variables	buf	and	in	
- Need	mutual	exclusion	

## Semaphore	for	Mutual	Exclusion	

![picture 6](images/475938b82873eae974d41dbe297ec66cee2df44db21f2f896671e387ac4547d4.png)  
- Works	for	multiple	producers	and	consumers	
- But	not	easy	to	understand:	easily	leads	to	bugs	
  - Example:	what	if	wait	statements	are	interchanged?

## Monitors
- Programming	language	construct	for	IPC	
  - Variables	(shared)	requiring	controlled	access	
  - Accessed	via	procedures	(mutual	exclusion)	
  -  Condition	variables	(general	synchronization)	(cannot store value ,cannot remember anything)
     - wait	(cond):	block	until	another	process	signals	cond
     - signal	(cond):	unblock	a	process	waiting	on	cond
- Only	one	process	can	be	active	inside	monitor	
  - Active	=	running	or	able	to	run;	others	must	wait	

## Producer/Consumer	using	a	Monitor
![picture 7](images/3879ab9f05414b3e2e4ff05fdc2c8004703665afd3868bc61ddf6ac745179083.png)  


## How	Synchronization	Works
![picture 8](images/972e54bf468b4d56f77ca627e9d23e737d6b2015a5d2674251e0ec7d1a1b6578.png)  

## Issues	with	Monitors
- Given	P1	waiting	on	condition	c,	P2	signals	c
  - P1	and	P2	able	to	run:	breaks	mutual	exclusion	
  - One	solution:	signal	just	before	returning	
- Condition	variables	have	no	memory	
  - Signal	without	someone	waiting	does	nothing	
  - Signal	is	“lost”	(no	memory,	no	future	effect)	
- Monitors	bring	structure	to	IPC	
  - Localizes	critical	sections	and	synchronization	

## Message	Passing	
![picture 1](images/4220d04367e64e236a2993288417bda13a913c0e2313769b200779b0c3f81206.png)  
- Two	methods	
  - send (destination, &message)
  - receive (source, &message)
- Data	transfer:	in	to	and	out	of	kernel	message	buffers	
- Synchronization:	receive	blocks	to	wait	for	message

## Producer/Consumer:	Message-Passing
![picture 2](images/7d0188f046e6d4e146dac242c15b94d248915de86f1178a69e539d5034f04151.png)  

## An	Optimization
![picture 3](images/508a45ea88e3de5849edc2d14c1308c2c58531b3852f0c06faba9e2c79845dba.png)  

- consume and produce may take time

## Issues	with	Message	Passing
- Who	should	messages	be	addressed	to?	
  - ports	(“mailboxes”)	rather	than	processes	
- How	to	make	process	receive	from	anyone?	
  - pid = receive (*, &message)
- Kernel	buffering:	outstanding	messages	
  - messages	sent	that	haven’t	been	received	yet	
- Good	paradigm	for	IPC	over	networks	
 Safer	than	shared	memory	paradigms	

 # Deadlock
 ## What	is	Deadlock?
 - Set	of	processes	are	permanently	blocked	
  - Unblocking	of	one	relies	on	progress	of	another	
  - But	none	can	make	progress!	
- Example	
  - Processes	A	and	B	
  - Resources	X	and	Y	
  - A	holding	X,	waiting	for	Y	
  - B	holding	Y,	waiting	for	X	
  - Each	is	waiting	for	the	other;	will	wait	forever	
![picture 4](images/7a841fa7f4d0ce2b1fd251fd162d677ccff25b0cf54869e1de79ded9743ba342.png)  

## Traffic	Jam	as	Example	of	Deadlock
![picture 5](images/748cc55cb2a42142cca50790a1af999ba03f402b331e5c5e3311d778c48560de.png)  

## Four	Conditions	for	Deadlock
- Mutual	Exclusion	
  - Only	one	process	may	use	a	resource	at	a	time	
- Hold-and-Wait	
  - Process	holds	resource	while	waiting	for	another	
- No	Preemption	
  - Can’t	take	a	resource	away	from	a	process	
- Circular	Wait	
  - The	waiting	processes	form	a	cycle	

## How	to	Attack	the	Deadlock	Problem
- Deadlock	Prevention	
  - Make	deadlock	impossible	by	removing	condition	
- Deadlock	Avoidance	
  - Avoid	getting	into	situations	that	lead	to	deadlock	
- Deadlock	Detection	
  - Don’t	try	to	stop	deadlocks	
  - Rather,	if	they	happen,	detect	and	resolve	

## Deadlock	Prevention
- Simply	prevent	any	single	condition	for	deadlock	
- Mutual	exclusion	
  - Relax	where	sharing	is	possible	
- Hold-and-wait	
  - Get	all	resources	simultaneously	(wait	until	all	free)	
- No	preemption	
  - Allow	resources	to	be	taken	away	
- Circular	wait	
  - Order	all	the	resources,	force	ordered	acquisition	

## Deadlock	Avoidance
- Avoid	situations	that	lead	to	deadlock	
  - Selective	prevention	
  - Remove	condition	only	when	deadlock	is	possible	
- Works	with	incremental	resource	requests	
  - Resources	are	asked	for	in	increments	
  - Do	not	grant	request	that	can	lead	to	a	deadlock	
- Need	maximum	resource	requirements	

## Banker’s	Algorithm
- Fixed	number	of	processes	and	resources	
  - Each	process	has	zero	or	more	resources	allocated	
- System	state:	either	safe	or	unsafe	
  - Depends	on	allocation	of	resources	to	processes	
- Safe:	deadlock	is	absolutely	avoidable	
  - Can	avoid	deadlock	by	certain	order	of	execution	
- Unsafe:	deadlock	is	possible	(but	not	certain)	
  - May	not	be	able	to	avoid	deadlock	

## Banker’s	Algorithm
- Given	
  - process/resource	claim	matrix	
  - process/resource	allocation	matrix	
  - resource	availability	vector	
- Is	there	a	process	ordering	such	that	
  - a	process	can	run	to	completion,	return	resources	
  - resources	can	then	be	used	by	another	process	
  - eventually,	all	the	processes	complete	

## Deadlock	Detection	and	Recovery
- Do	nothing	special	to	prevent/avoid	deadlocks	
  - If	they	happen,	they	happen	
  - Periodically,	try	to	detect	if	a	deadlock	occurred	
  - Do	something	(or	even	nothing)	about	it	
- Reasoning	
  - Deadlocks	rarely	happen	
  - Cost	of	prevention	or	avoidance	not	worth	it	
  - Deal	with	them	in	special	way	(may	be	very	costly)	
- Most	general	purpose	OS’s	take	this	approach!

## Detecting	a	Deadlock	
![picture 66](images/dac93308a6fd1e9657a47da43ac4685ee3acd5009c65c5e6864b10389f6d1504.png)  

## Recovery	from	Deadlock
- Terminate	all	deadlocked	processes	
  - Will	remove	deadlock,	but	drastic	and	costly	
- Terminate	deadlocked	processes	one	at	a	time	
  - Do	until	deadlock	goes	away	(need	to	detect)	
  - What	order	should	processes	be	ended?	
- What	about	resources	in	inconsistent	states	
  - Such	as	files	that	are	partially	written?	
  - Or	interrupted	message	(e.g.,	file)	transfers?	

## Classical	Synchronization	Problems
- Producer/Consumer	(Bounded	Buffer)	
- Dining	Philosophers	
- Readers/Writers	

## The	Dining	Philosopher’s	Problem
![picture 67](images/fe97fa4d126f24448b518617d467bcbdc429124dfd63c2784db56706f695547c.png)  
![picture 68](images/b83f3ce5527f9719f546be59056dd39bb680b6d76c8c2ae8b3982ef7a674326c.png)  
![picture 69](images/8899534cf63c50b8084169b6bfc9f00bb9b04faf8f568c90966a805b1f6639e3.png)  
