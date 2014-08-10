* open Chrome
* hit F12
* go to ingress.com/intel
* drag/zoom the map to encompass all desired portals
* in the network tab of the developer tools window, search for getEntities. right click and "copy response" into a text editor. 

first part of response should look like:
```{ "result": { "map": { "15_1502_3582_1_8_100": { "deletedGameEntityGuids": [ "636ce64052de47ecaae2da332793eee5.9",```

* save the response
* ```python parser.py response.txt > output.csv```
