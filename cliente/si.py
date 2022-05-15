datos = [{'idclientelogo': 1, 'status': '01', 'date': '04/27/2022, 18:05:06'},
         {'idclientelogo': 31, 'status': '01', 'date': '04/28/2022, 23:15:06'},
         {'idclientelogo': 32, 'status': '01', 'date': '04/28/2022, 23:45:01'},
         {'idclientelogo': 33, 'status': '01', 'date': '04/28/2022, 23:46:14'},
         {'idclientelogo': 34, 'status': '01', 'date': '04/28/2022, 23:47:24'},
         {'idclientelogo': 35, 'status': '01', 'date': '04/28/2022, 23:47:40'},
         {'idclientelogo': 36, 'status': '01', 'date': '04/29/2022, 19:59:03'},
         {'idclientelogo': 37, 'status': '01', 'date': '04/29/2022, 19:59:36'},
         {'idclientelogo': 38, 'status': '01', 'date': '04/29/2022, 20:01:41'}]
for x in range(len(datos)):

    #print(type(x))
    lista=list(datos[x].values())
    lista=lista[1:]
    print(lista)
    print(type(lista))
    print("\n")