from abc import ABC, abstractmethod
import random as rnd

class Nucleic_Acid(ABC):
    def control(seq, bases):
        for nucleotide in (seq):
            if nucleotide not in bases:
                raise ValueError(f'The sequence should contain only {bases} letters. The letter {nucleotide} was found')
    
    @abstractmethod
    def complementar(self, nitrogenous_base):
        complimentary_string = ""
        for nucleotide in self:
            complimentary_string = complimentary_string + nitrogenous_base[nucleotide]
        return complimentary_string           
    
    @abstractmethod
    def index(self, i):
        return(self[i])

    @abstractmethod
    def mul(self, other):
        result = ''
        i = 0
        j = 0
        while i<len(self) and j<len(other):
            if rnd.randint(0,1):
                result+=other[j]
                j+=1
            else:
                result+=self[i]
                i+=1
        if i == len(self):
            result+=other[j::]
        else:     
            result+=self[i::]
        return result
    
    @abstractmethod
    def __eq__(self, other):
        if len(self)==len(other):
            control = True
            n = len(self)
            for i in range(n):
                if self[i]!=other[i]:
                    control = False
                    break
            return control
        return False
            
        
    
class DNA(Nucleic_Acid, str):
    def __init__(self, seq):
        super().control("ACGT")
        self.nitrogenous_base = {"A":"T", "T":"A", "G":"C", "C":"G"}
        self.complementary = self.complementar()
        
    def __add__ (self, other): 
        res = DNA(str(self)+str(other)) 
        return(res.DNA)
    
    def index(self, i):
        nucleotide = DNA(super().index(i))
        return(nucleotide, nucleotide.complementar())
         
    def complementar(self):
        return super().complementar(self.nitrogenous_base)
    
    def mul(self, other):
        result_string =  DNA(super().mul(other))
        return result_string, result_string.complementar()
    
    def __eq__(self, other):
        res_str1 = (super().__eq__(other))
        res_str2 = (super().__eq__(other.complementary))
        if res_str1 or res_str2:
            return True
        return False
    
    def __repr__(self):
        return super().__str__() +", "+ self.complementary        
        
class RNA(Nucleic_Acid, str):
    def __init__(self, seq):
        super().control("ACGU")
        self.nitrogenous_base = {"A":"U", "U":"A", "G":"C", "C":"G"}
   
    def index(self, i):
        return super().index(i)
             
    def complementar(self):
        return super().complementar(self.nitrogenous_base)
        
    def mul(self, other):
        return super().mul(other)
    
    def __eq__(self, other):
        res_str1 = (super().__eq__(other))
        res_str2 = (super().__eq__(other.complementar()))
        if res_str1 or res_str2:
            return True
        return False
        
