<!-- ## Welcome to GitHub Pages--> 
# BOTNETS - GNU/GPLv3
## We are two students of UPB Bucaramanga university in Colombia wanting to improve the internet security.

## Working
##### There's three kind of node: common, master and slave
##### Every node starts as a common node. If there's no master one, common node will be the master. 
##### If a node starts an master is alive, but there's no slave; common node will be the slave.
##### If a node starts after master and slave are setted up, common will still common until the nodes queue makes it slave or master.

##### If master dies, slave will replace it, and next common node in queue will be set up as slave.
##### If slave dies, nobody will take it's place.
##### If common dies, nobody will take it's place.

### Needed knowledge
```
- Mqtt on python or/and Arduino developer
- Networking and telematics expert
- Cluster architecture expert
```

### To-Do list
-Fix Arduino implementation: arduino skilled developer -> High priority

&nbsp;     1. Fix Arduino wifi connection bug: arduino developer -> **Maximum priority**

&nbsp;     2. Fix Arduino mqtt code: arduino skilled developer -> **Maximum priority**

&nbsp;     3. Fix Arduino botnet rules: arduino skilled developer & networking/cluster architecture skilled engineer-> **Maximum priority**

-Master-slave (two slave at the same time) bug Python: python skilled developer, cluster architecture expert -> **Maximum priority**

-Android/IOs implementation: Android/IOs skilled developer -> Medium priority

-Charge asignation: python/arduino skilled developer -> High priority

-Project into native linux repositories: ? -> Low priority

-Fix id overlapping when executing more than one instance: cluster architecture expert -> High priority


[Release](https://github.com/intentodemusico/BotnetsHeterogeneas/releases/tag/0.1)
