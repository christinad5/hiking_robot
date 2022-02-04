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

p.resetBasePositionAndOrientation(boxId, startPos, startOrientation)
output_file = open('orientation_data.csv', 'w')
datawriter = csv.writer(output_file)
for i in range(100):
    cubePos, cubeOrn = p.getBasePositionAndOrientation(boxId)
    datawriter.writerows([cubeOrn])
    p.stepSimulation()
    time.sleep(1./240.)

output_file.close()
p.disconnect()
