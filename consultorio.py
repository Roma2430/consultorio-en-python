from cliente import Cliente

cantidad_extraccion = 0
class Consultorio:
        
    array_prioridad_de_atencion = ["normal", "urgente"]
                            
    def valor_atencion(tipo_de_cliente, cantidad):
        valor_cita = 0 
        global cantidad_extraccion       
        valor_atencion = 0        
            
        if tipo_de_cliente == "particular":
            valor_cita = 80000
            print("Ingrese el servicio: ")
            print("limpieza")
            print("calzas")
            print("extraccion")
            print("diagnostico")
                       
            valor_atencion = input("seleccione: ")
            if valor_atencion == "limpieza":
               if cantidad > 1:
                  print("Lo sentimos solo permite una limpieza")
                  valor_atencion = 60000
            elif valor_atencion == "calzas":
                 valor_atencion = 80000
            elif valor_atencion == "extraccion":
                 valor_atencion = 100000
                 cantidad_extraccion += 1
            elif valor_atencion == "diagnostico":
                 if cantidad > 1:
                    print("Lo sentimos solo permite un diagnostico")
                 valor_atencion = 50000
    
        elif tipo_de_cliente == "eps":
             valor_cita = 5000
             print("Ingrese el servicio: ")
             print("calzas")
             print("extraccion")
             valor_atencion = input("seleccione: ")
             
             if valor_atencion == "calzas":
                valor_atencion = 40000
             elif valor_atencion == "extraccion":
                  valor_atencion = 40000
                  cantidad_extraccion += 1
                
        elif tipo_de_cliente == "prepagada":
             valor_cita = 30000
             print("Ingrese el servicio: ")
             print("calzas")
             print("extraccion")
             valor_atencion = input("seleccione: ")
                         
             if valor_atencion == "calzas":
                valor_atencion = 10000
             elif valor_atencion == "extraccion":
                  valor_atencion = 10000
                  cantidad_extraccion += 1
                
        total = (valor_cita + (valor_atencion * cantidad))

        print(total)
            
        return total
    
    lista_cliente = []
    registrar = input("Vas a registrar un cliente si o no: ").lower()
    
    
    while registrar == "si":
       cedula = input("Ingrese numero de cedula: ")
       nombre = input("Ingrese su nombre: ")
       telefono = input("Ingrese su numero de telefono: ")
       print("Ingrese el tipo de cliente: ")
       print("particular")
       print("eps")
       print("prepagada")
           
       tipo_cliente = input("seleccione")
           
       cantidad =int(input("Ingrese la cantidad"))
           
       print("Ingrese el tipo de atencion: ")
       print("normal")
       print("urgente")
       prioridad_de_atencion = input("seleccione: ")
           
       fecha_de_la_cita = input("Ingrese la fecha de la cita: ") 
       print(fecha_de_la_cita)
       valor = valor_atencion(tipo_cliente, cantidad)
       
       cliente = Cliente(cedula, nombre, telefono, tipo_cliente, valor, cantidad, prioridad_de_atencion, fecha_de_la_cita)
       lista_cliente.append(cliente)
       registrar = input("Vas a registrar un cliente si o no: ").lower()
    
    print("total clientes: ", len(lista_cliente))
    print("cantidad de extracciones por cliente: ", cantidad_extraccion)
    
    ingresos_totales = 0
    
    for new_lista_cliente in lista_cliente:
        
        ingresos_totales += new_lista_cliente.valor_atencion
                
        print(vars(new_lista_cliente))
    
    print("ingresos totales: ", ingresos_totales)
        
           
