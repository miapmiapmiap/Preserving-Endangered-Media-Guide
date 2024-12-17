import glob
import bagit
import json

bag_dir = input("What is the directory to your bag? \n")
json_loc = bag_dir+'/data/*.info.json'
print(json_loc)
for files in glob.glob('*/data/*.info.json'):
    with open(files) as json_data:
        data = json.load(json_data)

bag = bagit.Bag(bag_dir)
email = input("What is your email? \n")
ext_des = input("Please describe the data in the bags (e.g. Youtube video and associated metadata from filmmaker Maurice Chevalier.) \n")
source_org = input("Please write the name of the institution you work for. \n")
org_add = input("Please input the address of the institution you work for. \n")
bag.info['Contact-Email'] = email
bag.info['External-Description'] = ext_des
bag.info['Source-Organization'] = source_org
bag.info['Organization-Address'] = org_add
bag.info['Title'] = data["fulltitle"]
bag.info['Video-Description'] = data["description"]
bag.info['Uploader-Channel'] = data["channel"]
bag.info['Uploader-Username'] = data["uploader_id"]
bag.info['Video-Thumbnail'] = data["thumbnail"]

bag.save()

if bag.is_valid():
    print("Sucessfully updated bag.")
else:
    print("Bag invalid. Please update checksums.")
