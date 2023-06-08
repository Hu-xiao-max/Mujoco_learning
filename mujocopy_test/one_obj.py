import mujoco_py

from mujoco_py import load_model_from_path, MjSim, MjViewer

model1 = load_model_from_path('/home/ubuntu/code/test_mujoco/mujocopy_test/one_obj.xml')


sim1 = MjSim(model1)
viewer1 = MjViewer(sim1)

while True:
    viewer1.render()

    sim1.step()
