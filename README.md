# IRC WebHook Highlights

## Usage:
- Copy the configuration file addon_python.conf in ~/.config/hexchat
- Fill all the fields in addon_python.conf
- Copy the content of the addons folder in ~/.config/hexchat/addons

## How it works:
A POST request will be sent to URL_RECEIVED whenever any of the words within the 'highlight' array is found in a received message.
A POST request will be sent to URL_READ whenever the HexChat window gains focus.
