from os import name
import pyverilog.vparser.ast as vast
from pyverilog.vparser.parser import parse
from pyverilog.ast_code_generator.codegen import ASTCodeGenerator


rtl = "test1.gl.v" 
ast , _ = parse([rtl])
desc = ast.description 
definition = desc.definitions[0]

# Intializing Arrays and variables 

index = 0
FF_input = ""
FF_output = ""
check = True; # For MUXs
new_file1= []
new_file= []
list_1 = []
list_2 = []
clock_gate = []
not_gates_counter=0
flag = 0



###################################################################

# Intializing and Writing the clock gating module using vast

g_clk_wire = vast.Wire('__gclk__')
n_wire = vast.Wire('n[5]')



clock_gate = [
vast.PortArg("GCLK", vast.Identifier("__gclk__")),
vast.PortArg("GATE", vast.Identifier("EN")),
vast.PortArg("CLK", vast.Identifier("clk"))]

list_1 = [
vast.PortArg("A", vast.Identifier(str(FF_input))),
vast.PortArg("Y", vast.Identifier(str(not_gates_counter)))
]





clk_gate = vast.Instance(
 "sky130_fd_sc_hd__dlclkp",
 "__clockgate_cell__",
 tuple(clock_gate),
 tuple()
)


new_file.append(g_clk_wire)
new_file.append(n_wire)

######################################################################

# Generating MUX from the given cells /// NEEDED

########################################################################
# Getting the item and the instace in order to change the gatelevel netlist

for item in definition.items:
    flag=0

    item_type = type(item).__name__     # Get the name of the type to be able to get the instance
    
    
    if item_type != "InstanceList":     # Get the wires of the input 
        new_file.append(item)
    
    #instance_1 = item.instances[0]
    

    if item_type == "InstanceList":     # The type of the item
        instance = item.instances[0]    # Get the instance of the module in the item
        
        # Handle all the MUXs
        

#####################################################################################################            
    ## Exclude tge FF and the two types a21oi
        if((instance.module != "sky130_fd_sc_hd__dfxtp_1") & (instance.module != "sky130_fd_sc_hd__a21oi_1") & (instance.module != "sky130_fd_sc_hd__o21ai_0") & (instance.module != "sky130_fd_sc_hd__mux2_1")):  # Need to be fixed and modify 
            new_file.append(item)
        if (check):
            new_file.append(vast.InstanceList("sky130_fd_sc_hd__dlclkp", tuple(), tuple([clk_gate]))) # Instace - InstaceList --- Write to the gat-level-netlist
            check = False
            continue

    
#####################################################################################################            
    # Get the connection of the FF
        if(instance.module == "sky130_fd_sc_hd__dfxtp_1"):  

            i = 0
            for name in instance.portlist:
                
                name_2 = instance.name

                if i == 1:
                    #name.argname = "AA"
                    #FF_input = ""
                    FF_input = name.argname

                if i == 2:
                    FF_output = name.argname
                if i == 1:
                    FF_output_mux = name.argname
                i = i + 1
            
            
            
            for item_1 in definition.items:

                item_type_1 = type(item_1).__name__     # Get the name of the type to be able to get the instance
                if item_type_1 == "InstanceList":     # The type of the item
                    instance_1 = item_1.instances[0]    # Get the instance of the module in the item

                    for name_1 in instance_1.portlist:
                        #print(name_1.argname)

####################################################################################################
        # Deal with the a2oi with inverters
                        if (name_1.argname == FF_input) & (instance_1.module == "sky130_fd_sc_hd__a21oi_1") & (flag==0):


                            i = 0
                            for name1 in instance_1.portlist:
                                
                                # name_2 = instance_1.name

                                if i == 1:
                                    #name.argname = "AA"
                                    #FF_input = ""
                                    FF_input = name1.argname
                                i = i + 1

                            flag=1
                            not_gates_counter=not_gates_counter+1
                            print("HERE")
                            print(instance_1.module)

                            list_1 = [
                            vast.PortArg("A", vast.Identifier(str(FF_input))),
                            vast.PortArg("Y", vast.Identifier("n["+str(not_gates_counter)+"]"))]

                            temp_1 = vast.Instance(
                            "sky130_fd_sc_hd__inv_1",
                            "_n"+str(not_gates_counter)+"_",
                            tuple(list_1),
                            tuple()
                            )

                            new_file.append(vast.InstanceList("sky130_fd_sc_hd__inv_1", tuple(), tuple([temp_1]))) # Instace - InstaceList --- 

                            list_1 = [
                            vast.PortArg("CLK", vast.Identifier("__gclk__")),
                            vast.PortArg("D", vast.Identifier("n["+str(not_gates_counter)+"]")),
                            vast.PortArg("Q", vast.Identifier("r["+str(name.argname.ptr)+"]"))]

                            temp_1 = vast.Instance(
                            "sky130_fd_sc_hd__inv_1",
                            name_2,
                            tuple(list_1),
                            tuple()
                            )

                            new_file.append(vast.InstanceList("sky130_fd_sc_hd__dfxtp_1", tuple(), tuple([temp_1]))) # Instace - InstaceList --- 
        

                        elif (name_1.argname == FF_input) & (instance_1.module == "sky130_fd_sc_hd__mux2_1") & (flag==0):


                            i = 0
                            for name1 in instance_1.portlist:
                                if i == 1:
                                    FF_input = name1.argname
                                i = i + 1

                            flag=1
                            print("HERE")
                            print(instance_1.module)

                            list_1 = [
                            vast.PortArg("CLK", vast.Identifier("__gclk__")),
                            vast.PortArg("D", vast.Identifier(str(FF_input))),
                            vast.PortArg("Q", vast.Identifier(str(name.argname)))]

                            temp_1 = vast.Instance(
                            "sky130_fd_sc_hd__not_1",
                            name_2,
                            tuple(list_1),
                            tuple()
                            )

                            new_file.append(vast.InstanceList("sky130_fd_sc_hd__dfxtp_1", tuple(), tuple([temp_1]))) # Instace - InstaceList --- 



            

    
                    
                    
                    
                    
    
            
            
    #new_file.append(item)
            
            
        
    
        
#####################################################################

                # Get the name of the ports of the modules with clk 
                # NEED TO FIND THE MUX 
                # code start
            # for name in instance.portlist:
            #     print(name)

                    
                #     if name.portname == "A1": 
                #         list_1.append(name.argname)
                #     if name.portname == "A0": 
                #         list_2.append(name.argname)
                #continue
                # code end
                
            # Handle the flip flops modules
            
#####################################################################
    # Connect the wire of the FF with the output of the MUX
    # instance.argname="aaaaaa"
    #new_file.append(item)
    #     for name in instance.portlist:
    #         if name.portname == "CLK":
    #             name.argname=vast.Identifier('__gclk__')
    #         if name.portname == "D":
    #             name.argname=list_1[index]
    #         if name.portname == "Q":
    #             name.argname=list_2[index]
    #     index = index + 1
    #     print("portname: ", name.portname, "argname: ", name.portname)
    

            
            
            
                
                
        

        







########################################################################
# Generating output 
    
definition.items = tuple(new_file)
codegen = ASTCodeGenerator()
generate = codegen.visit(ast)
f = open("output.v", "w+")
f.write(generate)
f.close()