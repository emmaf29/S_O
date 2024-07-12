from operating_system.memory_algorithms.memory_manager import MemoryManager

class WorstFitAlgorithm(MemoryManager):
    
    def __init__(self, kernel):
        super().__init__(kernel)


    
    def load(self, data):
        best_hueco = None
        max_desperdicio = 0

        for h in super().allHueco():
            if len(data) <= h.memorySize():
                desperdicio = h.memorySize() - len(data)
            
                if desperdicio > max_desperdicio:
                    max_desperdicio = desperdicio
                    best_hueco = h

        if best_hueco is not None:
            for i in range(len(data)):
                super().hardware.mmu.place(best_hueco.baseDir() + 1, data[i])
                return best_hueco

 
            else:
                raise ValueError("Not enough space")

    

    def unload(self, pcb):
        for i in range(pcb.memory_start, pcb.memory_end):
            super().hardware.mmu.place(i,'')





       