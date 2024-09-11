class Medicamento:
    nome = ''
    nome_científico = ''
    tarja = ''
    local = ''
    ativo = False

medicamento_tadalafila = Medicamento()
medicamento_buscopan = Medicamento()
medicamento_paracetamol = Medicamento()

medicamento_tadalafila.nome = 'tadalafila'
medicamento_tadalafila.nome_científico = 'Cialis'

medicamentos = [medicamento_tadalafila, medicamento_buscopan]

print(medicamentos)
print(medicamento_tadalafila)
print(dir(medicamento_tadalafila))