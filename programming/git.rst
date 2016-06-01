###
Git
###


Repository
===========

* Normal

.. code-block:: bash

  git init

* Bare repository (without working tree / used to clone)

.. code-block:: bash

  git init --bare


Commit
=======

* Append to last commit

.. code-block:: bash

  git commit --amend

* Revert a commit

.. code-block:: bash

  git revert <version>


Edit a commit 
=============

.. code-block:: bash

  git rebase -i <version>

* This opens an editor -> change the pick into edit

.. code-block:: bash

  git add -A
  git commit -C HEAD
  git rebase --continue
  git push


Logging
========

* Show changes

.. code-block:: bash

  git log -p

* Show changes for one file or dir

.. code-block:: bash

  git log -- *.py


* Show only the last 3 entries

.. code-block:: bash

  git log -3

* Show only commits from the last 2 weeks

.. code-block:: bash

  git log --since=2.weeks

* Unpushed commits

.. code-block:: bash

  git log origin..

* Show log for one file

.. code-block:: bash

  git log -- [filename]


Branching
==========

* Create branch

.. code-block:: bash

  git checkout -b <branch>
  git push origin <branch>

* Checkout a branch

.. code-block:: bash

  git pull
  git checkout <branch>

* Delete branch

.. code-block:: bash

  git push origin :branch

* Show diff between two branches

.. code-block:: bash

  git diff master..<branch> --raw

* List all branches on remote

.. code-block:: bash

  git remote show origin

Merging
========

* Merge everything

.. code-block:: bash

  git checkout <branch>
  git merge master
  git checkout master
  git push origin <branch>

* Merge just one commit

.. code-block:: bash

  git cherry-pick <commit-id>


Tagging
========

* Create a tag

.. code-block:: bash

  git tag <tag_name>

* Create a tag with a comment

.. code-block:: bash

  git tag -m <comment> <tag_name>

* Show all tags

.. code-block:: bash

  git tag

* Show one tag

.. code-block:: bash

  git show <tag_name>

* Delete a tag

.. code-block:: bash

  git tag -d <tag_name>


Working with older versions
============================

* Get latest version of one file

.. code-block:: bash

  git checkout <file>

* Show specific version of one file

.. code-block:: bash

  git show <version>:<file>

* Get specific version of one file

.. code-block:: bash

  git checkout <version> <file>

* Delete all changes over a specific version

.. code-block:: bash

  git reset --hard <version>

* Delete just the changes of a specific commit

.. code-block:: bash

  git revert <commit-id>



Using the stash
================

* Save changes to the stash

.. code-block:: bash

  git stash

* Show stashes

.. code-block:: bash

  git stash list

* Show changes of a stash

.. code-block:: bash

  git stash show stash@{0}

* Apply latest stash changes and delete the stash

.. code-block:: bash

  git stash pop

* Apply a specific stash without deleting it

.. code-block:: bash

  git stash apply stash@{0}

* Delete a stash

.. code-block:: bash

  git stash drop stash@{0}

* Wipe all stashes

.. code-block:: bash

  git stash clear


Handling remote repositories
=============================

* Add a remote

.. code-block:: bash

  git remote add origin git://domain.tld/repo.git

* Show infos about remotes

.. code-block:: bash

  git remote show
  git remote show origin


Ignore existing file (if gitignore doesnt ignore)
=================================================

.. code-block:: bash

  git update-index --assume-unchanged <file>


Git over HTTP
=============

.. code-block:: bash

  git clone --bare /git/test
  touch git-daemon-export-ok                                                                                                             │
  git config --file config http.receivepack true                                                                                         │
  git config core.sharedRepository                                                                                                       │
  chown apache:apache -R /git/test


Apache config for gitweb
========================

.. code-block:: bash

  <VirtualHost *:80>
    ServerName git.server.net
    ServerAlias git

    DocumentRoot "/var/www/git"
    Timeout 2400

    LogFormat   combinedssl
    LogLevel    info
    ErrorLog    /var/log/httpd/git-error.log
    TransferLog /var/log/httpd/git-access.log

    RewriteEngine On
    RewriteLog "/var/log/httpd/git-rewirte.log"
    RewriteLogLevel 5
    RewriteCond %{QUERY_STRING} ^.*p=(.*?)(\.git|;|&|=|\s).*
    RewriteRule (.*)/$ http://git.server.net$1?

    SetEnv GIT_PROJECT_ROOT /git
    SetEnv GITWEB_CONFIG /etc/gitweb.conf
    Alias /git/static/ /var/www/git/static/
    AliasMatch ^/git/(.*/objects/[0-9a-f]{2}/[0-9a-f]{38})$          /var/www/git/$1
    AliasMatch ^/git/(.*/objects/pack/pack-[0-9a-f]{40}.(pack|idx))$ /var/www/git/$1
    ScriptAliasMatch \
                    "(?x)^/git/(.*/(HEAD | \
                    info/refs | \
                    objects/info/[^/]+ | \
                    git-(upload|receive)-pack))$" \
                    /usr/bin/git-http-backend/$1
    ScriptAlias /git/ /var/www/git/gitweb.cgi/
  </VirtualHost>


Subversion over git
====================

* You can use a subversion repo like a remote git repo
* Clone it

.. code-block:: bash

  git svn clone <svn-url>

* Pull and push changes

.. code-block:: bash

  git pull origin master
  git svn push origin master


Misc
=====

* Diff with meld http://nathanhoad.net/how-to-meld-for-git-diffs-in-ubuntu-hardy
* Code Review with ReviewBoard http://ericholscher.com/blog/2011/jan/24/using-reviewboard-git/
* Webfrontend http://gitorious.org/ or https://github.com/takezoe/gitbucket
