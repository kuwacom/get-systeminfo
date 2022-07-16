# get-systeminfo
Get system information such as CPU usage and RAM usage

# HOW TO USE
First run this command to install the required libraries.<br>
`pip install -r requirements.txt`

Call it from another program or load it as a module in python.<br>
## Example
Call example from nodejs.<br>
```
const {PythonShell} = require('python-shell');
PythonShell.run('systeminfo.py', null, function (err, result) {
    if (err) throw err
    resultJson = JSON.parse(result[0])
    console.log(resultJson)
})
```
Result
![image](https://user-images.githubusercontent.com/83022348/179366367-351d1898-b099-47e1-b2f2-7fba6bcc67d0.png)
