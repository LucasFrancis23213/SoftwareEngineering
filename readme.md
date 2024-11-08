# 后端代码说明
## 总体设计原则
- 分层原则：  
    > 遵照数据库应用程序的分层原则，将代码分为三层  

    1. **DBA**(Database Access)：负责与数据库进行交互，实现CURD操作
    2. **ServiceLayer**：业务逻辑层/服务层，负责调用DBA层封装的方法以实现业务逻辑；同时也承接从上层(即Api层)传递的数据并进行相关处理  
    3. **ControllerLayer**：Api层，负责实现前后端交互、数据封装  
- 前后端数据交互原则：
    1. 如果可以封装为**数据类**(Data Classes)，则前端**应以数据类的形式**向后端传递信息  
    2. ControllerLayer -> ServiceLayer间的数据传递也应传递数据类(**某些情况不必遵守该原则**)  

## 代码结构
### 功能代码与测试代码  
> 此处只是对两个模块进行简要介绍，后面会有更细致的解释  
- SpringBoot框架自创建后会自动生成`main`和`test`两个文件夹，其中`main`文件夹存放**功能代码**，`test`文件夹存放**测试代码**    
- 理想情况下，main模块的每个package都应该在test文件夹中有**相同名称**的package作为测试  
### resources
- `properties`：存放本项目会使用到的、但不希望被hard code在代码中的内容，主要存放`配置文件(config)`，可理解为其他语言的`config`文件夹  
- `static/template`：涉及前端功能，暂时不需要使用  
- `application.properties`：项目的默认启动文件，存放**spring框架中已经有的配置**(如mysql在database的连接)  
- `logback-spring.xml`：日志系统的xml文件，负责**创建日志文件(.log)、设定调用规则(绑定)**  

