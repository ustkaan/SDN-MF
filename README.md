# SDN_MF
Network Programming Group Project

## Requirements <br>
-Linux <br>
-Mininet <br>
-Floodlight <br>

## Mininet
```
sudo mn --custom topo.py --topo mytopo --mac --switch ovsk --controller=remote,ip=10.02.15,port=6653 --link=tc
```

## Floodlight
```
java -jar target/floodlight.jar
```
```
10.02.15:8080/ui/index.html
```

## SDN

Open Terminal
```
gterm h1 h2
or
xterm h1 h2
```

Select one host as server and the other host as client and then run python files
```
python3 server.py
```
```
python3 client.py
```

<br/><br/>
## License
[![GNU GPLv3 or Later](https://www.gnu.org/graphics/gplv3-or-later.svg)](https://www.gnu.org/licenses/gpl-3.0.html)
