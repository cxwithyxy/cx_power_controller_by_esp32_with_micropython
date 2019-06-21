# 充电控制器

根据目标设备的电量来控制是否接通充电线路，避免过度充电导致电池膨胀的情况发生。



## 系统结构

![结构图](doc/结构图.svg)

通过 micropython 的开发板，控制继电器，而继电器控制充电头与目标设备连接的USB充电线。因此开发板便可以控制充电线路是否接通了。

而目标设备通过开发板提供的网页对开发板进行控制，并把当前电量信息告知开发板。从而实现整个系统闭环。

