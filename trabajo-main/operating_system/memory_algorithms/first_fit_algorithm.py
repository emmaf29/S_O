from operating_system.memory_algorithms.memory_manager import MemoryManager

class FirstFitAlgorithm(MemoryManager):

    def __init__(self, kernel):
        super().__init__(kernel)
       


    def load(self, data):
        for h in super().allHueco():
            if(len(data)<= h.memorySize()):
                for i in range(0, len(data)):
                    super().hardware.mmu.place(h.baseDir() + 1, data[i])
                return h
            else:
                raise RuntimeWarning("Not enought space")



    def unload(self, pcb):
        for i in range(pcb.memory_start, pcb.memory_end):
            super().hardware.mmu.place(i,'')
            

        



