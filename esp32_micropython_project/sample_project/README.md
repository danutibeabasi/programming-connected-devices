# Simple MicroPython project with autocompletion


## Content of the directory

- `.vscode/extensions.json` lists the extensions that are recommended for this project. VSC will prompt you to install these extensions if required.
- `.vscode/settings.json` lists folders to be scanned for Autocomplete and IntelliSense 
- `espTypeshed` typeshed for most modules available in the ESP32. There may be minor differences with the MicroPython version you actually have flashed on your ESP32, or some missing modules.
- `lib` put any existing module you may need here, you may use the filter [`micropython` on pypi](https://pypi.org/search/?q=micropython&o=) to find drivers or useful modules
- `boot.py` and `main.py` see https://docs.micropython.org/en/latest/esp8266/tutorial/filesystem.html#start-up-scripts
- `pymakr.conf` Pymakr configuration, lists for example which files shouldn't be uploaded to the device
- `README.md` this file. 