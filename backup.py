"""
    py-gitbackup
    Copyright (C) 2014  Javier Casas

    This program is free software; you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation; either version 2 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License along
    with this program; if not, write to the Free Software Foundation, Inc.,
    51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.


Backup: pushes all the branches in the known repositories
        to the backup repositories
"""

import os
import config


def get_destinations():
    """
    Returns a list of paths to backup directories
    """
    path = os.path.abspath(config.destinations_base_dir)
    items = os.listdir(path)
    fullitems = [(os.path.join(path, item), item) for item in items]
    return fullitems


def system(cmd):
    """
    Wrapper for debugging os.system
    """
    #print cmd
    os.system(cmd)


def backup_to_destination(dest_path, dest_name):
    """
    pushes all the repositories to the backup repositories
    """
    for repo in config.repositories:
        backupname = repo + ".git"
        destdir = os.path.join(dest_path, backupname)
        if not os.path.exists(destdir):
            try:
                os.makedirs(destdir)
            except OSError:
                # Something about this destination is broken
                continue

        if not os.path.exists(os.path.join(destdir, "HEAD")):
            system("cd {} && git init --bare".format(destdir))

        sourcedir = os.path.join(config.repositories_base_dir, repo)
        system("cd {} && git remote add {} {} 2> /dev/null"
               .format(sourcedir, dest_name, destdir))
        system("cd {} && git push --all {}".format(sourcedir, dest_name))


def main():
    """
    Main: pushes all the repositories to the backup repositories
    """
    for destination, name in get_destinations():
        backup_to_destination(destination, "backup_" + name)


if __name__ == '__main__':
    raise SystemExit(main())
