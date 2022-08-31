

import os, shutil

sourcefolder = input('Please input the absolute directory of the files your would like to copy.\n')
destinationfolder = input('Please input the absolute directory for the file destination.\n')

for file in os.listdir(sourcefolder):
    shutil.copy(os.path.join(sourcefolder, file), destinationfolder)
    print('Copying %s to %s.' %(file, destinationfolder))

print('')
print('Your files have been copied. :) ')