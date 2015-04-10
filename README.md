# iPhone Ordering

## What were we trying to solve?

It was decided that the entire Support department at JAMF Software would be moved off of desk phones and over to iPhones and we wanted to come up with an easy way for our users to order one of the supported options while also providing all the information we would need to port the number and ship the new phone. What we came up with is a small GUI ordering tool launched from Self Service that submitted the user's order as an IT ticket.

## What does it do?

The GUI is a Python script (Python version 2.7.6 tested) with API credentials for Zendesk passed as parameters. The username for who is logged into Self Service is used to generate a ticket on their behalf. This ordering tool contains all of the displayed images as embedded blobs of base64 data (meaning the whole app is delivered all at once). When a user clicks on an iPhone model and color, it changes the displayed picture to match. Once they click submit all of the selected options are put into the body of the ticket form and then sent to Zendesk.

![Screenshot](/images/iPhoneOrderingApp.gif)

## How to deploy this script in a policy

Upload the script to your JSS and create a policy. The #4 and #5 parameters should be a Zendesk admin account's email address and API token. We set this policy to run once per computer when we deployed it to our staff (in some cases people would cancel out and require us to flush the policy log for their Mac). This script has been tested against 10.9 and 10.10 clients.

## License

```
JAMF Software Standard License

Copyright (c) 2015, JAMF Software, LLC. All rights reserved.

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

    * Redistributions of source code must retain the above copyright notice,
      this list of conditions and the following disclaimer.
    * Redistributions in binary form must reproduce the above copyright notice,
      this list of conditions and the following disclaimer in the documentation
      and/or other materials provided with the distribution.
    * Neither the name of the JAMF Software, LLC nor the names of its contributors
      may be used to endorse or promote products derived from this software without
      specific prior written permission.

THIS SOFTWARE IS PROVIDED BY JAMF SOFTWARE, LLC "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL JAMF SOFTWARE, LLC BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
```
