'''
   (C) 2019 Raryel C. Souza
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.
    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
'''

from pytranscriber.control.ctr_main import Ctr_Main
import multiprocessing
import socks
import socket

if __name__ == '__main__':
    socks.set_default_proxy(socks.HTTP, '127.0.0.1', 7890)
    socket.socket = socks.socksocket
    multiprocessing.freeze_support()
    import sys

    ctrMain = Ctr_Main()
    sys.exit(main())
