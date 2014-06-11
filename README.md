py-gitbackup
============

Automatically backups git repositories to available backup locations.


Usage
-----
* Edit config.py, set your base path and repositories.
* Put symlinks to the backup locations in the _destinations_ directory.
* Add a post-commit hook to your projects that runs _python backup.py_

And that's it. The system will push all the branches of all your projects to all the available backup locations each time you commit.
