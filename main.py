#!/usr/bin/env python
#
#
# jsbsim-pacejka.py
# Calculate the tyre cornering coefficient table for JSBSim groud
# reactions, using Pacejka's Magic Formula.
#
#
# USAGE
#
# jsbsim-pacejka.py <step> <stiffness> <shape> <peak> <curvature> <jsbsim-static-friction>
#
# where jsbsim-static-friction is your bogey's <static_friction> tag
# used here as inverse scaling, because JSBSim internally multiplies
# the table by that.
#
# Insert the output of this program under your <contact> in the
# following form:
#
# <table name="CORNERING_COEFF" type="internal">
#  <tableData>
#   INSERT THE OUTPUT HERE
#  </tableData>
# </table>
#
#
# EXAMPLE
#
# This will give you the same force as calculated by JSBSim by
# default, with the step of 3 degrees:
#
# jsbsim-pacejka.py 3.0 0.06 2.8 static_friction 1.03 static_friction
#
# where static_friction is the value of static_friction for your
# JSBSim contact point.

import sys
import math as m
import numpy as np

Step = float(sys.argv[1])
JSBSim_scaling = 1 / float(sys.argv[6])

Stiffness = float(sys.argv[2])
Shape = float(sys.argv[3])
Peak = float(sys.argv[4])
Curvature = float(sys.argv[5])

for WheelSlip in np.arange(-90.0, 90.0 + Step, Step):
 StiffSlip = Stiffness*WheelSlip
 FCoeff = Peak * m.sin(Shape*m.atan(StiffSlip - Curvature*(StiffSlip - m.atan(StiffSlip))))
 FCoeff *= JSBSim_scaling
 print("{}\t{}".format(WheelSlip, FCoeff))
