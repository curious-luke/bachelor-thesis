# This file downloads the data from Archive.org and unzips it
import internetarchive
from internetarchive import configure
from internetarchive import get_session
from internetarchive import get_item
from internetarchive import get_files

def downloader(liste):
    # Grabing all files
    identifier_list = liste
    print("Number of Identifiers: ", len(identifier_list))

    # Config File & Configuration
    user = 'lsonthi@web.de'
    pw = 'bachelor'
    config_file = 'D:/Dokumente/Uni/Bachelorarbeit/Python/BA-Project.ini'
    configure(user, pw, config_file)
    config = dict(s3=dict(access='data_download', secret='bar'))
    s = get_session(config)
    s.access_key

    # Download all tar files from IA objects
    for ident in identifier_list:
        item = s.get_item(ident)
        file_names = [f.name for f in get_files(ident, glob_pattern='*tar')]
        #print(fnames)
        for i in file_names:
            item.download(files=i, dry_run=True)
        return
