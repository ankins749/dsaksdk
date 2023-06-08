import os, time

MenuPrincipal = True
MenuCantidad = False

PrecioNormal, DescuentoNormal, TotalNormal, CantidadNormal = 25000, 1, 0, 0
PrecioVipBasico, DescuentoVipBasico, TotalVipBasico, CantidadVipBasico = 35000, 0.35, 0, 0
PrecioVipPremium, DescuentoVipPremium, TotalVipPremium, CantidadVipPremium = 45000, 0.25, 0, 0

while MenuPrincipal:
    try:
        os.system("cls")
        print("-= Carro de Compras =-")
        if CantidadNormal + CantidadVipBasico + CantidadVipPremium > 0:
            if CantidadNormal > 0: 
                print(f"* Cantidad Entrada Normal: {CantidadNormal} (${TotalNormal})")
            if CantidadVipBasico > 0: 
                print(f"* Cantidad Entrada Vip Basica: {CantidadVipBasico} (${TotalVipBasico})")
            if CantidadVipPremium > 0: 
                print(f"* Cantidad Entrada Vip Premium: {CantidadVipPremium} (${TotalVipPremium})")
            print(f"* Total: ${TotalNormal + TotalVipBasico + TotalVipPremium}\n")
        else:
            print("* No has comprado entradas *\n")
        print("Seleccione una opcion:")
        print(" [0] Salir")
        print(" [1] Entrada Normal")
        print(" [2] Entrada Vip Basica")
        print(" [3] Entrada Vip Premium")
        print(" [4] Finalizar Compra")
        print(" [5] Anular compra")
        opcion = int(input(">"))
        if opcion == 0:
            print("--- Hasta Pronto ---")
            break
        elif opcion == 1:
            MenuCantidad = True
            while MenuCantidad:
                cantidad = int(input("Ingrese Cantidad"))
                if cantidad <= 0:
                    print("[Error] Cantidad Inválida.")
                    time.sleep(3)
                else:
                    TotalNormal += (PrecioNormal * cantidad) * DescuentoNormal
                    CantidadNormal += cantidad
                    break
        elif opcion == 2:
            MenuCantidad = True
            while MenuCantidad:
                cantidad = int(input("Ingrese cantidad: "))
                if cantidad <= 0:
                    print("[Error] Cantidad Inválida.")
                    time.sleep(3)
                else:
                    TotalVipBasico += (PrecioVipBasico * cantidad) * DescuentoVipBasico
                    CantidadVipBasico += cantidad
                    break
        elif opcion == 3:
            MenuCantidad = True
            while MenuCantidad:
                cantidad = int(input("Ingrese cantidad: "))
                if cantidad <= 0:
                    print("[Error] Cantidad Inválida.")
                    time.sleep(3)
                else:
                    TotalVipPremium += PrecioVipPremium * cantidad
                    CantidadVipPremium += cantidad
                    break
        elif opcion == 4:
            if CantidadNormal + CantidadVipBasico + CantidadVipPremium == 0:
                print("[Error] No Ha Comprado Entradas.")
                time.sleep(3)
            else:
                os.system("cls")
                print("--- Boleta ---")
                if CantidadNormal > 0:
                    print(f"* {CantidadNormal}x Entradas Normales: ${TotalNormal}")
                if CantidadVipBasico > 0:
                    print(f"* {CantidadVipBasico}x Entradas Vip Basicas: ${TotalVipBasico}")
                if CantidadVipPremium > 0:
                    print(f"* {CantidadVipPremium}x Entradas Normales: ${TotalVipPremium}")
                print(f"Total: ${TotalNormal + TotalVipBasico + TotalVipPremium}/n")
                print("Gracias por su compra :D.")
                CantidadNormal, CantidadVipBasico, CantidadVipPremium = 0, 0, 0
                TotalNormal, TotalVipBasico, TotalVipPremium = 0, 0, 0
                time.sleep(5)
        elif opcion == 5:
            if CantidadNormal + CantidadVipBasico + CantidadVipPremium == 0:
                print("[Error] No ha comprado entradas.")
                time.sleep(3)
            else:
                CantidadNormal, CantidadVipBasico, CantidadVipPremium = 0, 0, 0
                TotalNormal, TotalVipBasico, TotalVipPremium = 0, 0, 0
        else:
            print("[Error] Opcion Inválida.")
            time.sleep(3)
    except Exception as error:
        print(f"[Precaución] Ocurrio un Error: {error}")
        time.sleep(3)	