import mujoco_py as mp

model = mp.load_model_from_path('/home/ubuntu/code/test_mujoco/xml/xml_add_object.xml')
sim = mp.MjSim(model)
# viewer = mp.MjViewer(sim)
sim_step=0.01
for i in range(1000):
    sim.step()

