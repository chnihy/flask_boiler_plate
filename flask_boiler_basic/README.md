# Basic Boiler Plate # 1

A very simple setup, only features html templates and an initial '/index' route

Useful for hello world style pages, and one page API apps

## How to launch flask app 
1. Requirements:
```bash
>>> pip3 install -r requirements.txt
```
2. Flask factory or 'if __name___' 
```bash
>>> export FLASK_APP=app.py
```
or
uncomment this line in the <code>app.py</code> file
```python
'''
if __name__=="__main__":
	app.run()'''
```
3. Launch
```bash
flask run
```
or 
```bash
python3 app.py
```
4. View in browser
Open your browser and go to <code>localhost:5000</code>