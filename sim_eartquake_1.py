from kesmarag.spf import SinglePlanarFault
from instaseis import FiniteSource

top_center = (38.0, 20.0, 3.0)
dims = (30, 20)
angles = (50, 60)
ngrid = (60, 40)
hyp_idx = (24, 14)
vr = 2.4
dt = 0.01
mu = [(30, 20), (33, 17)]
sigma = [2.0, 1.0]
dmax = [10.0, 5.0]
rake = [50.0, 40.0]
t_acc = [0.1, 0.2]
t_eff = [1.2, 1.0]

fault = SinglePlanarFault(top_center,
                          dims,
                          angles,
                          ngrid,
                          hyp_idx,
                          vr,
                          dt,
                          mu,
                          sigma,
                          dmax,
                          rake,
                          t_acc,
                          t_eff)

fault.animation_slip_velocity('./animations/sim_earthquake_1.mp4', 700)
fault.create_srf('./srf_files/sim_earthquake_1.srf')

source = FiniteSource.from_srf_file('./srf_files/sim_earthquake_1.srf')

print(source)
