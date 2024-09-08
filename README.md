# web-automation
 This repository is for web automation using playwright.

 # Setup

 Setup a virtual env and install playwright.

 ```
 git clone https://github.com/lyfofvipin/web_automation.git; cd web_automation
 python -m venv py_env
 source py_env/bin/activate
 pip install -r requriments.txt
 playwright install
 ```

# How To Run Test Case

```
pytest tests/test.py --junitxml=results.xml.xml --hide_browser
```
