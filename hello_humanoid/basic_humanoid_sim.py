import pybullet as p
import time
import pybullet_data
import csv

physicsClient = p.connect(p.DIRECT) #p.GUI for graphics
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
startPos = [0,0,1]
startOrientation = p.getQuaternionFromEuler([0,0,0])
boxId = p.loadURDF("humanoid_torso.urdf", startPos, startOrientation)

"""
link_name_to_index = {p.getBodyInfo(boxId)[0].decode('UTF-8'):-1,}
        
for id in range(p.getNumJoints(boxId)):
	name = p.getJointInfo(boxId, id)[12].decode('UTF-8')
	link_name_to_index[name] = id
print(link_name_to_index)
"""

# important link indices for humanoid.urdf
link_names_index = {'lwaist': 2, 'pelvis': 4, 'right_thigh': 8, 'right_shin': 10, 
'right_foot': 13, 'left_thigh': 17, 'left_shin': 19, 'left_foot': 22, 'right_upper_arm': 25,
'right_lower_arm': 27, 'left_upper_arm': 30, 'left_lower_arm': 32}

link_info_names = ['lwaist', 'pelvis', 'right_thigh', 'right_shin', 'right_foot',
'left_thigh', 'left_shin', 'left_foot', 'right_upper_arm', 'right_lower_arm', 'left_upper_arm',
'left_lower_arm']

# create empty dictionaries to store link quaternions to 
header_name = link_info_names
link_data = {}
for i in link_info_names:
    link_data[i] = None

p.resetBasePositionAndOrientation(boxId, startPos, startOrientation)

# open up files to write data to
output_file1 = open('overall_orientation_data.csv', 'w')
link_data_file = open('link_orientation_data.csv', 'w')
datawriter1 = csv.writer(output_file1)
datawriter2 = csv.DictWriter(link_data_file, fieldnames=header_name)
datawriter2.writeheader()

for i in range(2):
    # obtain overall quat
    cubePos, cubeOrn = p.getBasePositionAndOrientation(boxId)
    datawriter1.writerows([cubeOrn])


    # obtain link quat
    for name, linkId in link_names_index.items():
        #print(name, linkId)
        linkInfo = p.getLinkState(boxId, linkId)
        linkWorldOrn = linkInfo[1]
        linkInertOrn = linkInfo[3]
        link_data[name] = linkWorldOrn

    datawriter2.writerow(link_data)
    
    p.stepSimulation()
    time.sleep(1./240.)

output_file1.close()
link_data_file.close()
p.disconnect()
