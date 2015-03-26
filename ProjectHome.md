It is a backup tool like Apple Mac's Time Machine, but it maintains backup-database for different machines in a single backup database folder, which is maintained in parallel in different locations user specified (and currently connect to the machine at the time of backup), and user can select which folder to backup.

This script copies the source locations indicated in the 'backup-locations.txt' file zipped in .gz format to the backup folder in CLINMAG and to additional locations indicated in the 'backup-locations.txt' file.

It maintains separate backup location of the machines which is backed-up, so if you have multiple machines which you backup, the backup-database will be maintained separately in the folder named after the machine which is backed up.

It maintains logfile about what happend in backup.