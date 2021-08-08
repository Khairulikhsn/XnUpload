Troubleshooting
===============

Videos are not streameable in Telegram app
-------------------------------------------
**Only mp4 videos can be played on Telegram without downloading them first**. To stream your video in Telegram you must
convert it before uploading it. For example you can use ffmpeg to convert your video::

    $ ffmpeg -i input.mov -preset slow -codec:a libfdk_aac -b:a 128k \
             -codec:v libx264 -pix_fmt yuv420p -b:v 2500k -minrate 1500k \
             -maxrate 4000k -bufsize 5000k -vf scale=-1:720 output.mp4


Database is locked
------------------
xnup is already running, or an old process **has locked the session** (``xnup.session``). Only one
xnup session can be run at a time.

**If you need to run xnup multiple times anyway**, you need to duplicate the session and config files:

1. Copy the session file (``~/.config/xnup.session``) to another path.
2. Copy the configuration file (``~/.config/xnup.json``) to another path.
3. Edit this file and add the path to session file like this: ``{"api_id": 0, "api_hash":
   "...", "session": "/path/to/xnup.json"}``.
4. Run using ``--config /path/to/xnup.json``.

If you are sure that xnup is not running, search for the process that is blocking the file::

    fuser ~/.config/xnup.session

As a last resort, you can restart your machine.


xnup does not work! An error occurs when executing it
-----------------------------------------------------------------
xnup is not tested with all versions of all dependencies it uses. If you have installed xnup
on your system (using root) maybe some existing dependency is on an incompatible version. You can try updating the
dependencies carefully::

    $ pip install -U xnup Telethon hachoir cryptg click

To avoid errors it is recommended to use `virtualenvs <https://docs.python-guide.org/dev/virtualenvs/>`_.

Before asking for help, remember to find out if `the issue already exists <https://github
.com/Khairulikhsn/XnUpload/issues>`_. If you open a ticket remember to paste your system dependencies on the issue::

    $ pip freeze

Some problems may not be related to xnup. If possible, `Google before asking <https://google.com/>`_.
