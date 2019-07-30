# IRC WebHook Highlights

## Usage:
- Copy the configuration file `addon_python.conf` in `~/.config/hexchat`
- Fill all the fields in `addon_python.conf`
- Copy the content of the addons folder in `~/.config/hexchat/addons`

## How it works:
A `POST` request is sent to `URL_RECEIVED` when any of the words within the `highlight` array is found in an incoming message.
A `POST` request is sent to `URL_READ` when the HexChat window gains focus.
