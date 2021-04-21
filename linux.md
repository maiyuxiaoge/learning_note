[toc]
# MSDOS（MBR） 与 GPT 磁盘分区表（partition table）

## MSDOS （MBR） 分区
### 格式
- 主要开机记录区（Master Boot Record, MBR）：可以安装开机管理程序的地方，有446 Bytes
- 分区表（partition table）：记录整颗硬盘分区的状态，有64 Bytes

- 主要分区与延伸分区最多可以有四笔（硬盘的限制）
- 延伸分区最多只能有一个（操作系统的限制）
- 逻辑分区是由延伸分区持续切割出来的分区；
- 能够被格式化后，作为数据存取的分区为主要分区与逻辑分区。延伸分区无法格式化；
- 逻辑分区的数量依操作系统而不同，在Linux系统中SATA硬盘已经可以突破63个以上的分区限制；
![picture 1](images/1fc5ee091739bcdc86f0bcd7ec66caed9e151a2828d6e61652860af1bab8b27a.png)  

### 限制
- 操作系统无法抓取到 2.2T 以上的磁盘容量！
- MBR 仅有一个区块，若被破坏后，经常无法或很难救援。
- MBR 内的存放开机管理程序的区块仅 446Bytes，无法容纳较多的程序码。

## GUID partition table, GPT 磁盘分区表
![picture 2](images/6f8bcd24e2d70ee65f14c72c824dea947eef132ec0e78ac76b624233ffbb4d53.png)  
- 与 MBR 仅使用第一个 512Bytes 区块来纪录不同， GPT 使用了 34 个 LBA 区块来纪录分区信息
- GPT 除了前面 34 个 LBA 之外，整个磁盘的最后 33 个 LBA 也拿来作为另一个备份
- GPT 分区默认可以提供多达 128 笔纪录
- GPT 分区已经没有所谓的主、延伸、逻辑分区的概念，既然每笔纪录都可以独立存在， 当然每个都可以视为是主分区，每一个分区都可以拿来格式化使用

# 开机启动的流程
1. BIOS：开机主动执行的固件，会认识第一个可开机的设备；
2. MBR：第一个可开机设备的第一个扇区内的主要开机记录区块，内含开机管理程序；
3. 开机管理程序（boot loader）：一支可读取核心文件来执行的软件；
4. 核心文件：开始操作系统的功能...

# bootloader的主要任务
- 提供菜单：使用者可以选择不同的开机项目，这也是多重开机的重要功能！
- 载入核心文件：直接指向可开机的程序区段来开始操作系统；
- 转交其他loader：将开机管理功能转交给其他loader负责。

# 文件系统与目录树的关系（挂载）
- 所谓的“挂载”就是利用一个目录当成进入点，将磁盘分区的数据放置在该目录下； 也就是说，进入该目录就可以读取该分区的意思
- 设备与磁盘分区对应的关系，就是 windows 概念下的挂载

# linux目录配置的依据（FHS）

## 必须存在度目录
- /bin: 可以被root和一般用户使用的指令
- /boot: 开机会使用的文件
- /dev: 装置与周边设备
- /etc：系统主要的设定档： 比如账号和密码，各种服务的启动档，可以让一般使用者查阅，只有root用户可以修改
- /lib： 在开机时会使用的函数库，以及在/bin或/sbin底下的指令会呼叫的函式库。
- /media： 可移除的装置，比如光盘
- /mnt: 临时挂载的装置
- /opt: 给第三方软件放置的位置
- /run: 系统开机后所产生的各项资讯
- /sbin： 只有root才能用来使用的指令，其他使用者最多只能查询，比如开机，修复，还原系统的指令
- /srv: 一些网络服务启动后所需要取用的资料目录
- /tmp: 正在执行的程序临时放置文件的地方，任何人能存取，不能放重要资料
- /usr:可分享不可变动的，类似windows中window的一部分+program files
  - /usr/bin/： 一般用用户能使用的指令，相当于/bin
  - /usr/lib/： 基本上与/lib功能相同
  - /usr/local/： 在本机自行安装自己下载的软件
  - /usr/sbin/： 非系统正常运行所需要的系统指令，比如服务器的服务指令
  - /usr/share/： 几乎都是文字档案及共享文件
  - /usr/games/： 与问阿金相关的资料
  - /usr/include/： c和c++ 的header和include放置处
  - /usr/libexec/： 不被使用者惯用的脚本
  - /usr/lib<qual>/： /lib<qual>连接到这个目录
  - /usr/src/： 原始码放置的位置
- /var: 系统运行后才会逐渐占用硬盘容量的目录
  - /var/cache/： 程序运行的缓存
  - /var/lib/： 程序执行过程中需要是用的资料放置的位置
  - /var/lock/： 锁
  - /var/log/： 登录文件放置的位置
  - /var/mail/： 电子邮件的目录
  - /var/run/： 程序启动后的pid会放置到这个目录
  - /var/spool/： 放置一些排队等待其他程序使用的资料

## 建议可以存在的目录
- /home: 使用者家目录
- /lib<qual>: 用来存放和lib不同的格式的二进制函数库
- /root:root用户的家目录

## 其他目录
- /lost+found: 文件系统出现错误时，将一些遗失的片段放置到这个目录下
- /proc：本身是一个虚拟档案系统，放置记忆体中的资料
- /sys:类似proc

## 目录树
![picture 3](images/d39ed236856fb45c572026046f7d683b489b00965852b45d6da8e5925b327089.png)  

# 磁盘与档案系统管理
## 为什么要格式化磁盘
- 每种作业系统所设定的档案属性和权限不同

## indexed allocation 索引式档案系统
- inode: 记录档案的属性，一个档案占用一个inode，同时记录该档案的资料所在的block号码
- block： 记录实际档案的内容，一个档案可能占用多个block
- superblock: 记录文件系统的整体资讯，包括inode、block的总量，使用量，剩余量以及档案系统的格式
- inode和block规划好了，除非重新格式化，否则固定不再变动

![picture 1](images/0d36ebf18e3f890e5ea09d3abe1a12108b524ee82e8c31d7c0a6347261b63be1.png)  

## inode table
- 每个inode大小固定为128bytes
- 每个档案占用一个inode
- 能建立的档案数量与inode的数量有关
- 系统读取档案时先找到inode，分析inode所记录的权限与使用者是否相同，若符合才能开始实际读取block的内容

![picture 3](images/92d35a3baa36680d07596b50b3f5f9cadca78120a43819d012cce633872193d9.png)  

## superblock
- 记录整个filesystem相关资讯
- block与inode的总量
- 未使用inode，block数量
- block与inode大小
- filesystem挂载时间等系统相关资讯
- valid bit


## 目录树的读取（举例读取/etc/passwd）
1. /的inode
2. /的block
3. etc/ 的inode
4. etc/ 的block
5. passwd的inode
6. passwd的block

## 资料的不一致状态 - 日志式档案系统
- 产生原因： 断电，系统核心错误等
- 解决方法： 日志
  1. 当系统要写入一个档案时，先在日志记录区块中记录要写入的资讯
  2. 实际写入
  3. 在日志记录区块中完成档案的记录

## 挂载点的意义
- 将档案系统和目录树结合的动作叫做挂在
- 挂载点一定是目录，该目录为进入该档案系统的入口

- 同一个filesystem的某个inode只会对应到一个档案内容
- 可以通过inode号码来确认不同档名是否为相同的档案

## XFS档案系统
- EXT档案系统： 预先规划处inode。block metadata区域，格式化很慢,对于巨型档案效率低
- 资料区： 类似ext系统，包括inode，data block，superblock
- 档案系统活动登录区： 记录档案系统的变化，类似日志区

## 即时运作区
- 当有档案要被建立时，xfs会在这个区段里找到一个到数个extent区块，将档案放在这个区块内，等分配完毕后，在写入到data section的inode与block中。

## hard link
- 多个档名对应同一个inode
- 在某个目录下新增一个档名连接到某个inode号码的关联记录
- inode号码相同，有多少个档名连接到这个inode
- 优势： 安全，将任何一个档名删除，其实inode和block都还存在
- 缺点： 不能跨文件系统，不能link目录
### symbolic link
- 建立一个独立的档案，档案会让资料的读取指向他link的那个档案的档名
- 当来源被删除后，symbolic link的档案也会失效
- 优点： 限制较少

## 档案系统的挂载和卸载
- 挂载点是目录
- 这个目录是进入磁盘分割槽的入口
- 单一档案系统不应该重复挂载在不同的目录中
- 单一目录不应该重复挂载多个档案系统
- 要作为挂载点的目录，理论上应该是空目录，否则原目录底下的东西会暂时消失

## 交换空间（swap）
- 原先因为存储不足，可以暂时吧记忆体的程序放到硬盘中，称为交换空间
- 如果硬件的配备足够，那么交换空间就不会被我们的系统使用
- 对于个人linux可能影响不大，对于服务器很重要

# 文档压缩
- gzip, bzip2, xz 无法将多个文件压缩成一个文件，tar可以

## xfs系统备份工具 xfsdump
- 可以进行完整备份（full backup) 也可以进行累计备份（incremental backup）
- 累计备份只会记录与第一次完整备份所有差异的文档
![picture 1](images/6c6d4e0370221cd73340f6937a1764efc5fdbb805aefa15cd292c4cb81ba9b4b.png)  


# bash
- shell将我们的输入和kernel沟通，好让kernel可以控制硬件正确工作
![picture 2](images/f6a8c6aa0fb4b18b5abd1262d900b770dc0e618187d969134667d1e1c8bf24e2.png)  

## login shell 和 non-login shell
- login shell： 取得bash时需要完整的登入流程，比如通过tty1-tty6登入
- non-login shell： 取得bash的方法不许压迫重复登入的举动， 比如用xwindow登入后，再用图形化界面启动终端， 在原本的bash环境下再次下达bash这个指令

## 管道（pipe)
- 管道命令仅仅嗯那个处理经由前面一个指令传来的正确资讯，对于error没有处理能力
![picture 3](images/3898e5c740ec4ef8fbdcd1778ebf2b9d6562d95582741848ac93aeba0761ffe8.png)  


# linux账号管理和acl权限设置
- linux主机并不会直接识别账号名称，而是根据uid和gid

## linux 登录流程
1. 先在 /etc/passwd 中查找输入的账号，得到uid和gid
2. 核对密码表
3. 进入shell控制的阶段

## 有效群组effective group和初始群组initial group
- 初始群组： 登陆后所在的群组
- 有效群组： 当前所在的群组


# 细部权限规划： acl的使用
- acl： access control list 提供owner，group，other，rwx以外的多种权限
- 可以针对单一用户设定权限

## sudo执行流程
1. 在/etc/sudoers 档案中搜索用户是否有sudo权限
2. 让用户输入密码
3. 执行sudo命令

# 磁盘配额Quota
- 起因： 多人多工的环境，应该限制硬盘的容量给使用者，以妥善的分配系统资源

## quota的使用限制
- 仅能针对整个文件系统
- 核心必须支持quota
- 只对一般身份使用者有效
- 如果启用selinux，不是所有目录都可以设置quota

# 磁盘阵列 raid
- 可以通过一项软件或硬件，把多个较小的磁盘整合成一个较大的磁盘
- 具有存储和保护的功能

## 常见level
- raid 0： 每个磁盘交错存放数据
![picture 4](images/db0089f3e81de714462de21f3994f0477936ee1bb84468d09bc4ca199b894eb9.png)  

- raid 1： 让同一份资料，完整保存在两个磁盘上
![picture 5](images/e6b438485356c0982549e4a1fa431f30e6fa862cedb3a80a066c2265e9d26ea9.png)  

- raid 1+ 0： 先让两颗磁盘组成raid 1， 将两组raid1 组成一组raid 0
![picture 6](images/2a933b55177628ddfb5b9df083b65e6bcd8c966ec2400beda7f4c50d4f88a8a7.png)  

- raid 5： 类似raid 0 ，但在每个磁盘中还加入一个同位检查资料Parity，这个资料会记录其他磁盘的备份资料
![picture 7](images/0054044c69edbb6cdb9b18591a2681d3886790eb9eeaec929d07e55039789006.png)  
  - raid 5 的总容量是整体磁盘数量减一

## spare disk
- 一颗没有包含在原本磁盘阵列中的磁盘，平常不会被使用，在有任何磁盘损毁时，会被主动拉进阵列中，将坏掉的磁盘移除阵列，然后重建系统

## 硬件磁盘阵列： 
- 通过硬盘上专门的芯片完成处理raid的任务
- 不会重复消耗原本系统的io资源，理论上效能比较好
- 价格较贵，主板可能不支持高级raid level

## 软件磁盘阵列
- 通过软件来模拟阵列的任务
- 会消耗比较多的系统资源

# 逻辑卷轴管理员 logical volume manager
- 可以弹性的调整filesystem的容量
- 通过软件将实体的硬盘组合成一块看起来独立的大磁盘(VG)， 然后将这块大磁盘分割成可使用分割槽(LV),最终就能挂载使用了
- lvm主要的用处在于实现一个可以弹性调整容量的档案系统上，而不是一个以效能为主的磁盘上

## physical volume PV 实体卷轴
- 实际的disk

## volume group VG 卷轴群组
- 许多PV整合成的大磁盘

## physical extent PE 实体范围区块
- 类似档案系统里的block大小

## logical volume LV 逻辑卷轴
- 最终VG会被切成LV， LV就是最后可以被格式化使用的

![picture 8](images/940ba359cce89c43c9baa6cbf8267871e236ddca0b48dbd8389ff2ae327073c9.png)  
![picture 9](images/ed82b1fa6a5769a36015ec3cd2ed32acc8c6ed656833146de972ea0ea642d526.png)  

## 使用lvm thin machine 让lvm动态自动调整磁盘使用率
- 先建立一个可以实支实付、用多少容量才分配实际写入多少容量的磁碟容量储存池(thin pool)， 然后再由这个thin pool 去产生一个『指定要固定容量大小的LV 装置』

# 例行性工作排程 crontab
## at: 可以处理一次就能结束排程的指令
- 将这个工作以文字档的方式写入/var/spool/at/目录内
## crontab： 指令所设定的工作将会循环的一直进行下去

## 可唤醒停机期间的工作任务
- anacron: 处理非24 小时一直启动的Linux 系统的crontab 的执行
- anacron 会去分析现在的时间与时间记录档所记载的上次执行anacron 的时间,然后开始执行未进行的crontab 任务

# 程序管理与SELinux 初探
## 程序与进程
- 程序program： 实体档案
- 进程 process： 权限属性和program会被写入内存， 并给他一个一个识别码 (PID)，程序就是一个正在运作中的程式。

## 子程序和父程序
- 衍生出来的程序
![picture 1](images/3b0c07f0fe67defa73c81c0b0ca5dd6def5c5012beed80f735a3960973198e5f.png)  

## fork and exec: 程序呼叫的流程
![picture 2](images/e16d35edad9c8dd22d8264ead97cd423b09a060150e0981c22fd8ed3620b98b0.png)  

- 系统先以fork的方式复制一个与父程序相同的暂存程序，唯一区别是pid不同，多一个ppid参数
- 暂存程序开始以exec的方式载入实际要执行的程序

## job control 工作管理
- 在单一终端机界面下同时进行多个工作的行为管理
- 条件：
  - 这些工作所触发的程序必须来自你shell的子程序
  - 前景： 你可以控制和下达命令的环境成为前景的工作
  - 背景：可以自行运行的工作，你无法用ctrl+c终止，可以用 bg/fg 呼叫
  - 背景中执行的程序不能等待terminal和shell的输入

## 程序管理
- 如果所有的程序同时被唤醒，那么cpu应该先处理哪个程序？
- Priority 与Nice 值
  - 优先执行序(priority, PRI):PRI值越低代表越优先,PRI值是由核心动态调整的，使用者无法直接调整PRI值
  - PRI(new) = PRI(old) + nice: 使用者可以调整nice值，当nice值为负值时，那么该程序就会降低PRI值，会优先被处理

# SELinux
- Security Enhanced Linux 
- SELinux是在进行程序、档案等细部权限设定依据的一个核心模组
- 自主式存取控制(Discretionary Access Control, DAC):依据程序的拥有者与档案资源的rwx权限来决定有无存取的能力
  - root具有最高的权限
  - 使用者可以取得程序来变更档案资源的存取权限
- 委任式存取控制, MAC: 针对特定的程序与特定的档案资源来进行权限的控管

## SELinux 的运作模式
- 主体(Subject): 程序
- 目标(Object)：主体程序能否存取的『目标资源』一般就是档案系统
- 政策(Policy)：依据某些服务来制订基本的存取安全性政策
- 安全性本文(security context)：主体与目标的安全性本文必须一致才能够顺利存取,类似档案系统的rwx
![picture 3](images/2d8995ebc90154cafba346f082d4a3429b381bd52679ad0343392576c66696e3.png)  
- 安全性本文是放置到档案的inode内的
![picture 4](images/fcdc03d154777fce244cf74d52025083c8f7c7eda8dc1ea0599caf4d88b6fba9.png)  
