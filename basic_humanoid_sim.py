import pybullet as p
import time
import pybullet_data
import csv

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.8)
planeId = p.loadURDF("/data/plane.urdf")
startPos = [0,0,1]
startOrientation = p.getQuaternionFromEuler([0,0,0])
boxId = p.loadURDF("/data/humanoid.urdf", startPos, startOrientation)

"""
link_name_to_index = {p.getBodyInfo(boxId)[0].decode('UTF-8'):-1,}
        
for id in range(p.getNumJoints(boxId)):
	name = p.getJointInfo(boxId, id)[12].decode('UTF-8')
	link_name_to_index[name] = id
print(link_name_to_index)
"""

# important link indices
link_names_index = {'torso': -1, 'lwaist': 2, 'pelvis': 4, 'right_thigh': 8, 'right_shin': 10, 
'right_foot': 13, 'left_thigh': 17, 'left_shin': 19, 'left_foot': 22, 'right_upper_arm': 25,
'right_lower_arrm': 27, 'left_upper_arrm': 30, 'left_lower_arm': 32}

link_info_names = ['torso', 'lwaist', 'pelvis', 'right_thigh', 'right_shin', 'right_foot',
'left_thigh', 'left_shin', 'left_foot', 'right_upper_arm', 'right_lower_arm', 'left_upper_arm',
'left_lower_arm']

p.resetBasePositionAndOrientation(boxId, startPos, startOrientation)
output_file1 = open('overall_orientation_data.csv', 'w')
output_file2 = open('link_orientation_data.csv', 'w')
datawriter1 = csv.writer(output_file1)
datawriter2 = csv.writer(output_file2)
for i in range(50):
    cubePos, cubeOrn = p.getBasePositionAndOrientation(boxId)
    datawriter1.writerows([cubeOrn])


    p.stepSimulation()
    time.sleep(1./240.)

output_file1.close()
output_file2.close()
p.disconnect()
