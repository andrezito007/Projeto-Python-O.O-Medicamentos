class Medicamentos:
    def __init__(self, nome, nome_cientifico, tarja, local):
        self.nome = nome
        self.nome_cientifico = nome_cientifico
        self.tarja = tarja
        self.local = local
        self.estoque = False

    def __str__(self):
        return f'{self.nome} | {self.nome_cientifico} | {self.tarja} | {self.local} | {self.estoque}'

medicamento_tadalafila = Medicamentos('Tadalafila', 'Cialis', 'Vermelha', 'Morumbi')
medicamento_buscopan = Medicamentos('Buscopan', 'butilbrometo de escopolamina', 'Amarela', 'Vila A')
medicamento_paracetamol = Medicamentos('Paracetamol', 'Acetaminofeno', 'Branca', 'Centro')

medicamentos = [medicamento_tadalafila, medicamento_buscopan, medicamento_paracetamol]

print(medicamento_tadalafila)
print(medicamento_buscopan)
print(medicamento_paracetamol)

