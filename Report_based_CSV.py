import csv

class Asignatura ():
    def __init__(self , asignatura):
        self.asignatura = asignatura
        self.candidates = []
        self.num_candit = 0
        self.scores = []
        self.fail = 0
        self.passi = 0
        self.mini = 0
        self.maxim = 0
        self.pasar = [self.asignatura, self.num_candit, self.passi, self.fail, self.maxim,self.fail]
        
    def __str__(self):
        return ("La asignatura es {} y los candidatos que tuvo fueron:{}"\
                    "la lista asociada es {}".format(self.asignatura, self.candidates, self.pasar))
    
class ExamResultReader ():
    
    def __init__(self, file):        
        self.asignaturas_dict = {}
        
        with open(file, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            
            for row in reader:
                asignatura = row['Exam Name']
                
                if asignatura not in self.asignaturas_dict:
                    self.asignaturas_dict[asignatura] = Asignatura(asignatura)
                    
                candidato = row['Candidate ID']
                if candidato not in self.asignaturas_dict[asignatura].candidates:
                    self.asignaturas_dict[asignatura].candidates.append(candidato)

                score = row['Score']                
                self.asignaturas_dict[asignatura].scores.append(score)

                if row['Grade'] == 'Fail':
                    self.asignaturas_dict[asignatura].fail += 1
                else:
                    self.asignaturas_dict[asignatura].passi += 1
                    
                
    def visual_datos_asig(self):
        
        for asignatura in self.asignaturas_dict:
            
            num_candidat = len(self.asignaturas_dict[asignatura].candidates)
            self.asignaturas_dict[asignatura].num_candit = num_candidat
            print("Num candidatos: ", num_candidat)
            
            minimo = min(self.asignaturas_dict[asignatura].scores)
            self.asignaturas_dict[asignatura].minimo = minimo
            print("El min: ", minimo)
            
            maximo = max (self.asignaturas_dict[asignatura].scores)
            self.asignaturas_dict[asignatura].maxim = maximo
            print("El max: ", maximo)
            
            print("Failed: ", self.asignaturas_dict[asignatura].fail)
            print("Passed: ", self.asignaturas_dict[asignatura].passi)

            self.asignaturas_dict[asignatura].pasar = [
            self.asignaturas_dict[asignatura].asignatura,
            self.asignaturas_dict[asignatura].num_candit,
            self.asignaturas_dict[asignatura].passi,
            self.asignaturas_dict[asignatura].fail,
            self.asignaturas_dict[asignatura].maxim,
            self.asignaturas_dict[asignatura].fail
        ]
        
            print(self.asignaturas_dict[asignatura].pasar)

    def archivo(self):
        with open('mi_reporte.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=',')
            writer.writerow(['Name', 'Num Candita', 'Passed', 'Failed', 'Best', 'Worst'])
            for asignatura in self.asignaturas_dict: 
                writer.writerow(self.asignaturas_dict[asignatura].pasar)
        
exam_result_reader = ExamResultReader('exam_results.csv')
exam_result_reader.visual_datos_asig()
exam_result_reader.archivo()
