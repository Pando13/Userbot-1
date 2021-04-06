

import sys


__version_mjaor__ = 2
__version_minor__ = 1
__version_micro__ = 0
__version_beta__ = 1

__version__ = "{}.{}.{}".format(__version_mjaor__,
                                __version_minor__,
                                f"{__version_micro__}-beta.{__version_beta__}" \
                                    if __version_beta__ else __version_micro__)

__license__ = "[Licenza AGPL-3.0]" + \
                "(https://github.com/leoatomic/userbot/blob/master/LICENSE)"

__copyright__ = "© 2020 dev [Leoatomic](https://github.com/leoatomic)"

__python_version__ = "{}.{}.{}".format(sys.version_info[0],
                                       sys.version_info[1], 
                                       sys.version_info[2])
