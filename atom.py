import numpy as np
import matplotlib.pyplot as plt

class Atom():
    def __init__(self,name,number):
        self.name = name
        self.number = number
        self.position = []
        
    #求平方平均位移
    def get_msd(self):
        msd = []
        for i in range(len(self.position)-1):
            msd.append(np.power(np.linalg.norm((self.position[i+1]-self.position[0])),2)/self.number)
        self.msd = np.array(msd)
        self.raw_msd = np.array(msd)
    
    #画出msd图
    def plot_msd(self):
        plt.figure(dpi = 180)
        plt.plot( np.array(range(len(self.msd))) * self.timestep, self.msd,linewidth = 1)
        plt.xlabel("time/fs")
        plt.ylabel("MSD/$Å^2$")
        #保存图片
        plt.savefig(r"Li_msd.jpg",dpi=200,bbox_inches = 'tight')
