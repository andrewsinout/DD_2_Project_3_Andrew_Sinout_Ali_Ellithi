# DD_2_Project_3_Andrew_Sinout_Ali_Ellithi

Andrew Shenouda
Ali Ellithi



•	Dependencies
o	Pyhton3
o	Pip3
o	Pyverilog parser

•	How to compile the code ?
o	In the blackboard, the code will be attached. 
o	Open the terminal 
o	>> python3 main.py 
o	The output will be in file called “output.v”

•	Code

	In this project, we handled the clock gating approach in order to save the dynamic power dissipation.
  We look to the code that is attached to us to have some clues how the python code working. 

	Then, we took the test cases that is uploaded on blackboard. Then, we took the gate level netlist.
  Parse it to be able to install the clock gating approach. We search for the FlipFlop and the connection
  to it from the gate level netlist.  Then, we created and connect the clock gate, then we check if we found mux,
  take the second input of the mux and connect it directly to the input of the flipflop and remove the mux.
  If we found  a21io, we remove it and connect its second input to an inverter, then we connect the output of the
  inverter to the input of the flipflop. Hence, we have two condition of muxs that we handle in this project, we have
  the normal muxs and the a21io. 



•	Tested the output in CloudV.io.However, there is a problem in the connection  of the output either the port has 2 inputs
at the same time or not connected 
 
  Testcases is attached to the repo



References: 

https://github.com/marwanH1998/AutomaticClockGatingDD2

