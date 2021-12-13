#import hdlparse.verilog_parser as vlog
import pyverilog.vparser.ast as vast
from pyverilog.vparser.parser import parse
from pyverilog.ast_code_generator.codegen import ASTCodeGenerator
import os 
import argparse
from math import comb
import copy
import math


#path = "./merged_unpadded.lef"
#lef_parser = LefParser(path)
#var = lef_parser.parse()

#vlog_ex = vlog.VerilogExtractor()
#vlog_mods = vlog_ex.extract_objects("test1.gl.v")

ast,_ = parse(["test1.gl.v"])

temp = ast.description

defin = temp.definitions[0]

print (ast)



# for m in vlog_mods:
#     for p in m.ports:
#         p.


