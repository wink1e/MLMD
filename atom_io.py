import numpy as np


def wash(line):
    r"""
    读取某一行的信息并返回列表，用来读取XDATCAR
    """
    line = line.split(" ")
    while "" in line:
        line.remove("")
    #删除最后的"\n"   
    line[-1] = line[-1][:-1]
    while "" in line:
        line.remove("")
    return line

#读取XDATCAR中的位置信息
def load_position(start_line, Atom_dict,lines):
    for j in Atom_dict.keys():
        direct = []
        for i in lines[start_line:start_line + Atom_dict[j].number]:
            direct.append([float(k) for k in wash(i)])
        pos = np.matrix(direct)             #直接用direct的坐标.dot(Atom_dict[j].lattice)
        start_line += Atom_dict[j].number
        Atom_dict[j].position.append(np.array(pos))
    
#读取XDATCAR并初始化
def loadfile(timestep, filename="XDATCAR"):
    with open(filename, 'r') as f:
        lines = f.readlines()
    #读取晶格矢量
    a,b,c = [np.array(wash(lines[i]), dtype="double") for i in range(2,5)]
    #读取原子符号和个数
    Atom_name = wash(lines[5])
    Atom_number = wash(lines[6])
    print("Reading XDATCAR...")
    #print(Atom_name,Atom_number)
    Atom_list = []
    Atom_dict = {}
    for i in range(len(Atom_number)):
        Atom_dict[Atom_name[i]] = Atom(Atom_name[i],int(Atom_number[i]))
        Atom_dict[Atom_name[i]].lattice = np.array([a,b,c])
        Atom_dict[Atom_name[i]].timestep = timestep
        # print("%-6s"%Atom_name[i],":",Atom_number[i])
        print(f"{Atom_name[i]:<6}: {Atom_number[i]}")
    #读取所有原子的位置轨迹
    print("Loading XDATCAR...")
    for i in range(len(lines)):
        if "Di" in lines[i]:
            load_position(i+1,Atom_dict,lines)
    print("done")
    return Atom_dict