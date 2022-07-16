# get-systeminfo
Get system information such as CPU usage and RAM usage

# HOW TO USE
First run this command to install the required libraries.<br>
`pip install -r requirements.txt`

Call it from another program or load it as a module in python.<br>
## Example
Call example from nodejs.<br>
```js
const {PythonShell} = require('python-shell');
PythonShell.run('systeminfo.py', null, function (err, result) {
    if (err) throw err
    resultJson = JSON.parse(result[0])
    console.log(resultJson)
})
```
Result<br>
![image](https://user-images.githubusercontent.com/83022348/179367430-b61e1595-6447-4eab-a5ad-1f61f59f2707.png)
<br>
# About network and drive results
The meaning of each number in the disk and network results is output in the same order as the following psutil document.<br>
Disk: https://psutil.readthedocs.io/en/latest/#psutil.disk_io_counters<br>
Network: https://psutil.readthedocs.io/en/latest/#psutil.net_io_counters
