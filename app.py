from modelos.medicamento import Medicamentos

medicamento_tadalafila = Medicamentos('Tadalafila', 'Cialis', 'Vermelha', 'Morumbi')
medicamento_buscopan = Medicamentos('Buscopan', 'butilbrometo', 'Amarela', 'Vila A')
medicamento_paracetamol = Medicamentos('Paracetamol', 'Acetaminofeno', 'Branca', 'Centro')

medicamento_tadalafila.alterar_estado()
medicamento_paracetamol.receber_preço('Vila Farma', 23)
medicamento_paracetamol.receber_preço('Farma Vida', 22)
medicamento_paracetamol.receber_preço('São João', 24)

def main():
    Medicamentos.listar_medicamentos()

if __name__ == '__main__':
    main()