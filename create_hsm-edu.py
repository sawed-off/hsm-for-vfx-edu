import pprint

# Start with a Project

project_data = {
    "name": "Hyperspace Madness", # Can be refined per school
    "sg_type": "Other", # Must match - this is based on a vanilla Shotgun site
    "sg_description": "Example project with data for demonstration, testing and training purposes.",
    "tank_name": "hyperspace_madness", # Can comment this out if you want to start as Zero-Config then use Advanced Project setup later
    "layout_project": {"id": 63, "type": "Project"}, # code 63 is the Template Project in a default site
}
projectCreated = shotgun.create("Project", project_data)
pprint.pprint(projectCreated)

# From the returned object data we grab the project id value to feed to subsequent creation procedures
projectID = projectCreated["id"]

# Found this based on a snippet on the web - https://github.com/kiryha/AnimationDNA/wiki/06-Tutorials#add-thumbnail-and-billboard-image-to-a-shotgun-project
imageBillboard = "/Volumes/1TBPassport/hsm/images/banner.jpg"
imageThumbnail = "/Volumes/1TBPassport/hsm/images/hyperspace-logo.jpg"
# Add Thumbnail
shotgun.upload_thumbnail("Project", projectID, imageThumbnail)
# Upload billboard
shotgun.upload("Project", projectID, imageBillboard, field_name="billboard")

# Figure out what to do in the loop and then what needs to be done after creation

assetIdList = []

# Then grab a list of Character Assets to loop through

characterAssetList = [
    "Sven",
    "Killamari"
]

for characterAsset in characterAssetList:
    asset_data = {
        "project": {"id": projectID, "type": "Project"},
        "sg_asset_type": "Character", # the one to change in the loop
        "code": characterAsset,
        "task_template": {"id": 36, "type": "TaskTemplate"}, # Example Asset Task Template
        "description": "Training asset provided by Autodesk",
        "sg_status_list": "rdy",
    }

    newAsset = shotgun.create("Asset", asset_data)
    pprint.pprint(newAsset)
    assetId = newAsset["id"]
    imageThumbnail = ("/Volumes/1TBPassport/hsm/images/" + characterAsset + ".jpg")
    shotgun.upload_thumbnail("Asset", assetId, imageThumbnail)
    assetIdList.append(assetId)

# Environments

environmentAssetList = [
    "Beach",
    "Planet"
]

for environmentAsset in environmentAssetList:
    asset_data = {
        "project": {"id": projectID, "type": "Project"},
        "sg_asset_type": "Environment", # the one to change in the loop
        "code": environmentAsset,
        "task_template": {"id": 36, "type": "TaskTemplate"}, # Example Asset Task Template
        "description": "Training asset provided by Autodesk",
        "sg_status_list": "rdy",
    }

    newAsset = shotgun.create("Asset", asset_data)
    pprint.pprint(newAsset)
    assetId = newAsset["id"]
    imageThumbnail = ("/Volumes/1TBPassport/hsm/images/" + environmentAsset + ".jpg")
    shotgun.upload_thumbnail("Asset", assetId, imageThumbnail)
    assetIdList.append(assetId)

# Props

propAssetList = [
    "Communicator",
    "Satellite",
    "Wrench"
]

for propAsset in propAssetList:
    asset_data = {
        "project": {"id": projectID, "type": "Project"},
        "sg_asset_type": "Prop", # the one to change in the loop
        "code": propAsset,
        "task_template": {"id": 36, "type": "TaskTemplate"}, # Example Asset Task Template
        "description": "Training asset provided by Autodesk",
        "sg_status_list": "rdy",
    }

    newAsset = shotgun.create("Asset", asset_data)
    pprint.pprint(newAsset)
    assetId = newAsset["id"]
    imageThumbnail = ("/Volumes/1TBPassport/hsm/images/" + propAsset + ".jpg")
    shotgun.upload_thumbnail("Asset", assetId, imageThumbnail)
    assetIdList.append(assetId)

# Vehicles

vehicleAssetList = [
    "Juggernaut",
    "Spaceship",
    "Trilobot"
]

for vehicleAsset in vehicleAssetList:
    asset_data = {
        "project": {"id": projectID, "type": "Project"},
        "sg_asset_type": "Vehicle", # the one to change in the loop
        "code": vehicleAsset,
        "task_template": {"id": 36, "type": "TaskTemplate"}, # Example Asset Task Template
        "description": "Training asset provided by Autodesk",
        "sg_status_list": "rdy",
    }

    newAsset = shotgun.create("Asset", asset_data)
    pprint.pprint(newAsset)
    assetId = newAsset["id"]
    imageThumbnail = ("/Volumes/1TBPassport/hsm/images/" + vehicleAsset + ".jpg")
    shotgun.upload_thumbnail("Asset", assetId, imageThumbnail)
    assetIdList.append(assetId)

pprint.pprint(assetIdList)
