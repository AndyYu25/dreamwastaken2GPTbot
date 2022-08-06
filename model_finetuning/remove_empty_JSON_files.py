import os
# assign directory
directory = 'json_data/dreamwastaken2'
 
# iterate over files in
# that directory
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    # checking if it is a file
    if os.path.isfile(f):
        if os.path.getsize(f) < 50:   #set file size in kb
            os.remove(f)