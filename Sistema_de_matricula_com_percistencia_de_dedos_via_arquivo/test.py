# Talvez eu use essa função
def check_entry(entry):
    valid_entry = False
    response = [0] * 2
    # Esse laço está sendo infinito, precisa modificar a condição de parada
    while entry != "1" or entry != "2":
        print("\nDeseja cadastrar outro usuário?\nSim - 1\nNão - 2")
        choise = input("Sua resposta: ")

        # Verifica se a entrada é válida
        if choise == "1" or choise == "2":
            valid_entry = True
            entry = choise

    response[0] = valid_entry
    response[1] = choise
    return response
