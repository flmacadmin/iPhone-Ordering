# iPhone Ordering

A Tkinter GUI that displays menu selections for iPhones.

![Screenshot](/images/demo.gif)

## Use

At Jamf, staff use this script to select iPhones for IT to purchase on the corporate wireless account. Our version of this script generates a Service Desk ticket from the collected options using a service account's credentials passed as parameters in the Self Service policy *($4 and $5 respectively)*.

If you wish to use this script within your organization you may copy the contents and customize it to work in your environment following the guide below.

> **This script has no external dependencies and has been tested on macOS 10.10+.**

## Customization

The object `MODEL_OPTIONS` defines the contents of the GUI when it loads.

For each `model` of iPhone you can define the `color` and `storage size` options that are available in the drop-downs. Each model in this object will be a menu option in the GUI that will update the color and storage menus when selected.

> *The URLs currently in the script that link to Dropbox are not guaranteed to work - you are encouraged to use your own hosting options for these images!*

The following syntax shows how to define each model.

```pyton
{
    '<model name>': {
        'storage': [16],  # Array of integers for allowed sizes
        'colors': {
            '<color name>': {
                'image_url': 'https://url_to_image.gif'
            }
        }
     }
}
```

Multiple `colors` can be defined for each `model`. Each `color` needs an image available at a reachable URL to load. The images must meet the following specifications:

* GIF Format (Tkinter only supports this format by default)
* 300 × 355 pixels
* Background color #F0F0F0 (Tkinter does not render transparency)

Below `MODEL_OPTIONS` there is a `create_ticket()` function where you will write the code to handle passing the user's selections into your ticketing system. The following data will be available to generate the ticket's contents from:

* `request_type`
* `model_name`
* `model_color`
* `model_storage`

A global variable named `LOGGED_IN_USER` is available to obtain the username of who is running the script. When run from Self Service, this variable can be one of two values:

1. Self Service requires authentication - it will be the authenticated username, or
2. Self Service does not require authentication - it will be the username of the local Mac user account.

## Testing

To run this script locally, type the path to the system's Python interpreter and **pass three values after the filename** to fill in the needed parameters *(the script uses $3 to obtain the username)*:

```
~$ /usr/bin/python iPhone-Ordering.py 1 2 username
```

The script will log the user's actions in the GUI as it runs and print the selected information at the end:

```
Starting app
Downloading photo for: iPhone 6s Space Gray
Setting new displayed photo
Creating ticket...
a new device, iPhone 6s, Space Gray, 32 GB, bryson.tyrrell
Successfully created help ticket
~$
```

## License

```
Jamf Standard License

Copyright (c) 2017, Jamf All rights reserved.

Redistribution and use in source and binary forms, with or without modification, are permitted
provided that the following conditions are met:

    * Redistributions of source code must retain the above copyright notice, this list of
      conditions and the following disclaimer.
    * Redistributions in binary form must reproduce the above copyright notice, this list of
      conditions and the following disclaimer in the documentation and/or other materials
      provided with the distribution.
    * Neither the name of the JAMF Software, LLC nor the names of its contributors may be
      used to endorse or promote products derived from this software without specific prior
      written permission.

THIS SOFTWARE IS PROVIDED BY JAMF SOFTWARE, LLC "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES,
INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A
PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL JAMF SOFTWARE, LLC BE LIABLE FOR ANY
DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR
BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT,
STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
```
