#!/usr/bin/env python

"""
Restformat to format logfile.
Referenced from:
http://otprof.blogspot.com/2009/05/rsync-home-backup-script.html

12.July.10
Hoo Chang Shin
hoo.shin@icr.ac.uk
"""

def title(mytitle='reStructuredText Title'):
    'Returns mytitle formatted as a reStructuredText title.'
    return '======================================' + '\n' + mytitle + '\n' + '======================================'

def subtitle(mysubtitle='reStructuredText Subtitle'):
    'Returns mysubtitle formatted as a reStructuredText subtitle'
    return mysubtitle + '\n' + '-----------------------------'


