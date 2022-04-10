# Basic Boiler Plate # 1

A very simple setup, only features html templates and an initial '/index' route

Useful for hello world style pages, and one page API apps

## How to launch flask app 
### Download Requirements:
```bash
pip3 install -r requirements.txt
```

### Launch app
There are two ways to launch a flask app:
<p class="codeblock_title">Launching flask through command line<p>
```bash
$ export FLASK_APP=app.py
```
then...
```bash
$ flask run
```
Or you can uncomment this line in the <code>app.py</code> file
<p class="codeblock_title">app.py</p>
```python
'''
if __name__=="__main__":
	app.run()'''
```
then...
```bash
python3 app.py
```

### View in browser
Open your browser and go to <code>localhost:5000</code>