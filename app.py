from modelos.medicamento import Medicamentos

medicamento_tadalafila = Medicamentos('Tadalafila', 'Cialis', 'Vermelha', 'Morumbi')
medicamento_buscopan = Medicamentos('Buscopan', 'butilbrometo', 'Amarela', 'Vila A')
medicamento_paracetamol = Medicamentos('Paracetamol', 'Acetaminofeno', 'Branca', 'Centro')

medicamento_tadalafila.alterar_estado()

def main():
    Medicamentos.listar_medicamentos()

if __name__ == '__main__':
    main()