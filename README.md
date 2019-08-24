# website-monitor

This is a short Python script that can monitor (preferably static) websites. If the website was updated you will be notified.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install this script.

```bash
pip install git+https://github.com/YanicM/website-monitor.git
```

## Usage

Change the URL to the page you want to monitor.
```python
test_monitor = WebsiteToMonitor("https://news.ycombinator.com/")
```
You can set a timer after which the website is checked again. The default is 60 seconds.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)
