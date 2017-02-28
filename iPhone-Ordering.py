#!/usr/bin/python
import AppKit
import base64
import sys
import Tkinter
import tkFont
import tkMessageBox
import urllib2

# ----------------------------------------------------------------------------------------------------------------------

# The script will determine the logged in user by the $3 parameter passed by Self Service
# If Self Service requires a login the value will be set to the authenticated username
# If Self Service does not require a login the value will be set to the username of the local Mac user account

LOGGED_IN_USER = sys.argv[3]

# The script will take a username and password as arguments you may pass as parameters to use in the 'create_ticket()'
# function defined below. Uncomment these variables if your ticket system uses an API that requires authentication.

# API_USERNAME = sys.argv[4]
# API_PASSWORD = sys.argv[5]


# Configure the available options for devices in the 'MODEL_OPTIONS' dictionary
# This dictionary object's syntax is as follows:

# {
#     '<model name>': {
#         'storage': [16],  # Array of integers for allowed sizes
#         'colors': {
#             '<color name>': {
#                 'image_url': 'https://url_to_image.gif'
#             }
#         }
#      }
# }

MODEL_OPTIONS = {
    'iPhone SE': {
        'storage': [16, 64],
        'colors': {
            'Silver': {
                'image_url': 'https://www.dropbox.com/s/d2ufzaq5fobpmgn/iphone-se-silver.gif?dl=1'
            },
            'Space Gray': {
                'image_url': 'https://www.dropbox.com/s/7kto399l046hiem/iphone-se-spacegray.gif?dl=1'
            },
            'Gold': {
                'image_url': 'https://www.dropbox.com/s/u7mc83nvk7jryou/iphone-se-gold.gif?dl=1'
            },
            'Rose Gold': {
                'image_url': 'https://www.dropbox.com/s/8vlnh2gz8qwnjbc/iphone-se-rosegold.gif?dl=1'
            }
        }
     },
    'iPhone 6s': {
        'storage': [32, 128],
        'colors': {
            'Silver': {
                'image_url': 'https://www.dropbox.com/s/tip995iiv64oymw/iphone-6s-silver.gif?dl=1'
            },
            'Space Gray': {
                'image_url': 'https://www.dropbox.com/s/mdliiwj3i6pyl2u/iphone-6s-spacegray.gif?dl=1'
            },
            'Gold': {
                'image_url': 'https://www.dropbox.com/s/yjy9t7weq5yuhcd/iphone-6s-gold.gif?dl=1'
            },
            'Rose Gold': {
                'image_url': 'https://www.dropbox.com/s/36qej0gy5arpwoi/iphone-6s-rosegold.gif?dl=1'
            }
        }
    },
    'iPhone 6s Plus': {
        'storage': [32, 128],
        'colors': {
            'Silver': {
                'image_url': 'https://www.dropbox.com/s/qkfhq8qv9j2bzbz/iphone-6sp-silver.gif?dl=1'
            },
            'Space Gray': {
                'image_url': 'https://www.dropbox.com/s/236jtowi94oqj11/iphone-6sp-gray.gif?dl=1'
            },
            'Gold': {
                'image_url': 'https://www.dropbox.com/s/j21j7pbz95x17vm/iphone-6sp-gold.gif?dl=1'
            },
            'Rose Gold': {
                'image_url': 'https://www.dropbox.com/s/qt7kfd5960qxq4s/iphone-6sp-rosegold.gif?dl=1'
            }
        }
    },
    'iPhone 7': {
        'storage': [32, 128, 256],
        'colors': {
            'Jet Black (128 only)': {
                'image_url': 'https://www.dropbox.com/s/f300k1yhrm42lq6/iphone-7-jetblack.gif?dl=1'
            },
            'Silver': {
                'image_url': 'https://www.dropbox.com/s/bf1d3iqt1mv64x2/iphone-7-silver.gif?dl=1'
            },
            'Black': {
                'image_url': 'https://www.dropbox.com/s/qrupfg2sk8ivc8a/iphone-7-black.gif?dl=1'
            },
            'Gold': {
                'image_url': 'https://www.dropbox.com/s/gau3o6hljvlvabq/iphone-7-gold.gif?dl=1'
            },
            'Rose Gold': {
                'image_url': 'https://www.dropbox.com/s/twu2u31elig2qwd/iphone-7-rosegold.gif?dl=1'
            }
        }
    },
    'iPhone 7 Plus': {
        'storage': [32, 128, 256],
        'colors': {
            'Silver': {
                'image_url': 'https://www.dropbox.com/s/b93xq2yu8qt9mcd/iphone-7-plus-silver.gif?dl=1'
            },
            'Black': {
                'image_url': 'https://www.dropbox.com/s/1n44ndkj4olgg0o/iphone-7-plus-black.gif?dl=1'
            },
            'Gold': {
                'image_url': 'https://www.dropbox.com/s/4o3fyf4fhjz1a1p/iphone-7-plus-gold.gif?dl=1'
            },
            'Rose Gold': {
                'image_url': 'https://www.dropbox.com/s/53nsniej3sqdm1x/iphone-7-plus-rosegold.gif?dl=1'
            }
        }
    }
}


# This function is called by the 'App.submit()` method
# All variables set by the selections in the GUI are passed to this function
# Code to generate a ticket for your ticketing system will go here

def create_ticket(request_type, model_name, model_color, model_storage):
    # Place your code to create a ticket here
    print('{}, {}, {}, {}, {}'.format(request_type, model_name, model_color, model_storage, LOGGED_IN_USER))

# ----------------------------------------------------------------------------------------------------------------------


class App:
    def __init__(self, master):
        """The main GUI window and methods"""
        self.master = master
        self.master.resizable(False, False)
        self.master.title("Order Your iPhone")

        # Set the 'close' button for the window to call our 'Cancel' function
        self.master.protocol('WM_DELETE_WINDOW', self.cancel)

        # This sets the background color to match the OS X 10.11 dialog window color
        bgcolor = '#F0F0F0'
        self.master.tk_setPalette(background=bgcolor, highlightbackground=bgcolor)

        # Set the default font used by Tkinter to match the system
        font = tkFont.nametofont('TkDefaultFont')
        font.config(family='system', size=14)
        self.master.option_add("*Font", font)

        # Suppress the macOS menu bar
        menu_bar = Tkinter.Menu(self.master)
        self.master.config(menu=menu_bar)

        print('Starting app')

        # Input variables for option menus
        self.model_options = MODEL_OPTIONS
        self.model_names = sorted(MODEL_OPTIONS.keys())

        self.model_photo = None

        self.input_request_type = Tkinter.StringVar()
        self.input_request_type.set('a new device')

        self.input_model_name = Tkinter.StringVar()
        self.input_model_name.set(self.model_names[0])

        self.input_model_color = Tkinter.StringVar()
        self.input_model_color.set(
            sorted(self.model_options[self.input_model_name.get()]['colors'].keys(), reverse=True)[0]
        )

        self.input_model_storage = Tkinter.StringVar()
        self.input_model_storage.set('{} GB'.format(self.model_options[self.input_model_name.get()]['storage'][0]))

        self.input_phone_number = Tkinter.StringVar()

        # ---------- Purchase New Device / Upgrade Device frame ----------
        self.frame1 = Tkinter.Frame(self.master)
        request_type_label = Tkinter.Label(self.frame1, text='I am requesting...')
        request_type_label.grid(row=0, column=0)
        self.request_type = Tkinter.OptionMenu(self.frame1, self.input_request_type, 'a new device',
                                               'to upgrade my device', command=self.action_request_type)
        self.request_type.config(width=20)
        self.request_type.grid(row=0, column=1)
        self.frame1.pack(padx=15, pady=(10, 5))

        # ---------- Device Selections frame ----------
        self.frame2 = Tkinter.Frame(self.master)
        self.select_model_name = Tkinter.OptionMenu(self.frame2, self.input_model_name, *self.model_names,
                                                    command=self.action_update_selections)
        self.select_model_name.config(width=14)
        self.select_model_name.grid(row=0, column=0)

        model_colors = self.model_options[self.input_model_name.get()]['colors'].keys()
        self.select_model_color = Tkinter.OptionMenu(self.frame2, self.input_model_color, *model_colors,
                                                     command=self.action_update_photo)
        self.select_model_color.config(width=12)
        self.select_model_color.grid(row=0, column=1)

        model_storage = ['{} GB'.format(size) for size in self.model_options[self.input_model_name.get()]['storage']]
        self.select_model_storage = Tkinter.OptionMenu(self.frame2, self.input_model_storage, *model_storage)
        self.select_model_storage.config(width=9)
        self.select_model_storage.grid(row=0, column=2)

        self.frame2.pack(padx=15, pady=5)

        # ---------- Photo frame ----------
        self.frame3 = Tkinter.Frame(self.master)
        self.photo_canvas = Tkinter.Canvas(self.frame3, width=300, height=355)
        self.photo_canvas.pack()
        self.frame3.pack(padx=15, pady=5)

        # ---------- Download and display the default iPhone
        self.displayed_photo = self.photo_canvas.create_image(0, 0, image=self.model_photo, anchor='nw')
        self.action_update_photo(self.input_model_color.get())

        # ---------- Current Phone Number frame ----------
        self.frame4 = Tkinter.Frame(self.master)
        phone_number_label = Tkinter.Label(self.frame4, text='Your current mobile number (if applicable):')
        phone_number_label.pack()
        self.entry_phone_number = Tkinter.Entry(self.frame4, background='white', textvariable=self.input_phone_number,
                                                width=30)
        self.entry_phone_number.pack()
        self.frame4.pack(padx=15, pady=5)

        # ---------- Cancel and Submit Buttons frame ----------
        self.frame5 = Tkinter.Frame(self.master)
        submit = Tkinter.Button(self.frame5, text='Submit', height=1, width=8, command=self.submit)
        cancel = Tkinter.Button(self.frame5, text='Cancel', height=1, width=8, command=self.cancel)
        submit.pack(side='right')
        cancel.pack(side='right')
        self.frame5.pack(padx=10, pady=(5, 10), anchor='e')

        self.user_data = None

    def action_update_selections(self, value):
        """Update colors, storage sizes and displayed photo when a different model is selected"""
        self._set_color_selections(value)
        self._set_storage_selections(value)
        self.action_update_photo(self.input_model_color.get())

    def _set_color_selections(self, value):
        """Update color menu with options specific to the selected model"""
        menu = self.select_model_color['menu']
        menu.delete(0, 'end')
        new_colors = sorted(self.model_options[value]['colors'].keys(), reverse=True)
        for color in new_colors:
            menu.insert('end', 'command', label=color,
                        command=Tkinter._setit(self.input_model_color, color, self.action_update_photo))

        self.input_model_color.set(new_colors[0])

    def _set_storage_selections(self, value):
        """Update storage size menu with options specific to the selected model"""
        menu = self.select_model_storage['menu']
        menu.delete(0, 'end')
        new_storage = [ '{} GB'.format(size) for size in self.model_options[value]['storage']]
        for size in new_storage:
            menu.add_command(label=size, command=lambda v=size: self.input_model_storage.set(v))

        self.input_model_storage.set(new_storage[0])

    def action_request_type(self, value):
        """Placeholder for action upon selection of a request type"""
        pass

    def action_update_photo(self, value):
        """Update the displayed photo for the selected model and color"""
        color = self.model_options[self.input_model_name.get()]['colors'][self.input_model_color.get()]
        if 'photo' not in color:
            color['photo'] = self._retrieve_photo(color)

        print('Setting new displayed photo')
        self.model_photo = Tkinter.PhotoImage(data=color['photo'])
        self.photo_canvas.itemconfig(self.displayed_photo, image=self.model_photo)

    def _retrieve_photo(self, color):
        """Returns base64 representation of a downloaded GIF for the current model and passed color"""
        print("Downloading photo for: {} {}".format(self.input_model_name.get(), self.input_model_color.get()))
        photo_data = urllib2.urlopen(color['image_url']).read()
        return base64.b64encode(photo_data)

    def cancel(self):
        """Exit the GUI without submitting a ticket"""
        print('User has closed the app')
        self.master.destroy()

    def submit(self):
        """Submit a ticket with the selections and then exit after displaying a message to the user"""
        print('Creating ticket...')
        create_ticket(
            self.input_request_type.get(),
            self.input_model_name.get(),
            self.input_model_color.get(),
            self.input_model_storage.get()
        )

        print('Successfully created help ticket')
        tkMessageBox.showinfo(message='Your request has been submitted!', parent=self.master)
        self.master.destroy()


def main():
    # Prevent the Python app icon from appearing in the Dock
    info = AppKit.NSBundle.mainBundle().infoDictionary()
    info['CFBundleIconFile'] = u'PythonApplet.icns'
    info['LSUIElement'] = True

    root = Tkinter.Tk()
    app = App(root)
    # Have the GUI appear on top of all other windows
    AppKit.NSApplication.sharedApplication().activateIgnoringOtherApps_(True)
    app.master.mainloop()

    sys.exit(0)

if __name__ == '__main__':
    main()
