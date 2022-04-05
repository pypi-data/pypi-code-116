import pyverilog.vparser.ast as vast
from pyverilog.ast_code_generator.codegen import ASTCodeGenerator

name = "my_verilog"

class port:
    def __init__(self, name:str, IO:str, lenth:int):
        self.name = name
        self.lenth = lenth
        if IO == 'out' and lenth == 1:
            self.item = vast.Ioport(vast.Output(self.name)) 
            
        elif IO == 'in' and lenth == 1:
            self.item = vast.Ioport(vast.Input(self.name))
            
        elif IO == 'out' and lenth != 1:
            width = vast.Width(vast.IntConst(str(lenth-1)),vast.IntConst('0'))
            self.item = vast.Ioport(vast.Output(self.name,width=width)) 

        elif IO == 'in' and lenth != 1:
            width = vast.Width(vast.IntConst(str(lenth-1)),vast.IntConst('0'))
            self.item = vast.Ioport(vast.Input(self.name,width=width))  
            
    def __add__(self, other):
        try:
            plus = vast.Plus(vast.Identifier(self.name), vast.IntConst(other.name))
        except:
            plus = vast.Plus(vast.Identifier(self.name), vast.IntConst(str(other)))
        return plus
    def __sub__(self, other):
        try:
            sub = vast.Minus(vast.Identifier(self.name), vast.IntConst(other.name))
        except:
            sub = vast.Minus(vast.Identifier(self.name), vast.IntConst(str(other)))
        return sub
      

class reg:
    def __init__(self, name:str, lenth:int):
        self.name = name
        if lenth == 1:
            self.item = vast.Reg(self.name) 

        else:
            width = vast.Width(vast.IntConst(str(lenth-1)),vast.IntConst('0'))
            self.item = vast.Reg(self.name,width=width)  
    def __add__(self, other):
        try:
            plus = vast.Plus(vast.Identifier(self.name), vast.IntConst(other.name))
        except:
            plus = vast.Plus(vast.Identifier(self.name), vast.IntConst(str(other)))
        return plus
    def __sub__(self, other):
        try:
            sub = vast.Minus(vast.Identifier(self.name), vast.IntConst(other.name))
        except:
            sub = vast.Minus(vast.Identifier(self.name), vast.IntConst(str(other)))
        return sub

        
class module:
    def  __init__(self, name, params, items, *ports):
        self.params = vast.Paramlist((params))                
        self.items = items  
        self.name = name
        items_ = []
        ports_ = []
        self.extern_count = 0
        self.extern_ = []
        try:
            for item in items:
                try:
                    if 'extern' in item:
                        extern = reg('extern'+str(self.extern_count), 1)
                        items_.append(extern.item)
                        self.extern_count = self.extern_count + 1
                        self.extern_.append(item.replace('extern_',''))
                except:
                    items_.append(item)
            for port in ports: 
                ports_.append(port.item)
        except:
            pass
        ports = vast.Portlist(ports_)
        self.ports = ports               
        self.ast = vast.ModuleDef('test',params,ports,items_)
    
    def visit(self):
        codegen = ASTCodeGenerator()
        code = codegen.visit(self.ast) 
        for i in range(self.extern_count):
            code = code.replace('reg extern'+str(i),self.extern_[i])
        return code

class always:
    def __init__(self, *sens):
        self.sens_1 = []
        self.sens_2 = []
        self.block = []
        for var in sens:
            self.sens_1.append(var)
            self.sens_2.append(vast.Sens(vast.Identifier(var.name), type='posedge'))
        self.senslist = vast.SensList(self.sens_2)

        self.item = vast.Always(self.senslist, None)
    
    def nonblock_assign(self, var, item):
        self.block.append(vast.NonblockingSubstitution(
            vast.Lvalue(vast.Identifier(var.name)),
            vast.Rvalue(item)))
        self.item = vast.Always(self.senslist, vast.Block(self.block))
        
    def block_assign(self, var, item):
        self.block.append(vast.BlockingSubstitution(
            vast.Lvalue(vast.Identifier(var.name)),
            vast.Rvalue(item)))
        self.item = vast.Always(self.senslist, vast.Block(self.block))
        
    def __if__(self, stat , block1, block2):
        self.block.append(vast.IfStatement(vast.Identifier(stat), block1, block2))
        self.item = vast.Always(self.senslist, vast.Block(self.block))
        
    def negedge(self, *sens):
        sens_3 = []
        for var in self.sens_1:
            if var in sens:
                sens_3.append(vast.Sens(vast.Identifier(var.name), type='negedge'))
            else:
                sens_3.append(vast.Sens(vast.Identifier(var.name), type='posedge'))
        self.senslist = vast.SensList(sens_3)
        self.item = vast.Always(self.senslist, vast.Block(self.block))

class block:
    def __init__(self):
        self.block = []      
        self.item = vast.Block(block)
        
    def nonblock_assign(self, var, item):
        self.block.append(vast.NonblockingSubstitution(
            vast.Lvalue(vast.Identifier(var.name)),
            vast.Rvalue(item)))
        self.item = vast.Block(self.block)
        
    def block_assign(self, var, item):
        self.block.append(vast.BlockingSubstitution(
            vast.Lvalue(vast.Identifier(var.name)),
            vast.Rvalue(item)))
        self.item = vast.Block(self.block)
    

def assign(port, dat):
    try:
        return vast.Assign(vast.Identifier(port.name),vast.IntConst(dat.name))  
    except:
        return vast.Assign(vast.Identifier(port.name),vast.IntConst(str(dat))) 

def extern_module(module,name,*ports):
    code = 'extern_' + module.name + ' ' + name + '('
    for port in ports:
        code = code + port.name
        code = code + ','
    code = code[0:-1] + ')'
    return code
