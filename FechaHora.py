class claseFechaHora:
    __d = 0     #dia
    __m = 0     #mes
    __a = 0     #año
    __h = 0     #hora
    __mi = 0    #minutos
    __s = 0     #segundos
    def __init__(self, dia = 1, mes = 1, año = 2020, hora = 0, min = 0, seg = 0):
        if(dia>=1 and dia<=31):
            if(mes>=1 and mes<=12):
                if(año>=0):
                    if(hora>=0 and hora<=24):
                        if(min>=0 and min<=60):
                            if(seg>=0 and seg<=60):
                                self.__d = dia
                                self.__m = mes
                                self.__a = año
                                self.__h = hora
                                self.__mi = min
                                self.__s = seg
                            else: print('ERROR: segundos inválido')
                        else: print('ERROR: minutos inválido')
                    else: print('ERROR: hora inválido')
                else: print('ERROR: año inválido')
            else: print('ERROR: mes inválido')
        else: print('ERROR: día inválido')
    def PonerEnHora(self, h = 0, m = 0, s = 0):
        self.__h = h
        self.__mi = m
        self.__s = s
    def AdelantarHora(self, h = 0, m = 0, s = 0):
        band = False    #indica si es año bisiesto
        self.__h += h
        self.__mi += m
        self.__s += s
        if (self.__a % 100 == 0):  # verifica que el año sea bisiesto
            if (self.__a % 400 == 0):
                band = True
        elif (self.__a % 4 == 0):
            band = True
        if (self.__s >= 60):
            self.__mi += 1
            self.__s -= 60
        if (self.__mi >= 60):
            self.__h += 1
            self.__mi -= 1
        if (self.__h >= 24):
            self.__d += 1
            self.__h -= 24
        if (band == True and self.__m == 2 and self.__d > 29):
            self.__m += 1
            self.__d -= 29
        elif (self.__m == 2 and self.__d >= 28):
            self.__m += 1
            self.__d -= 28
        if ((self.__m == 1 or self.__m == 3 or self.__m == 5 or self.__m == 7 or self.__m == 8 or self.__m == 10 or
                self.__m == 12) and self.__d > 31):
            self.__m += 1
            self.__d -= 31
        if ((self.__m == 4 or self.__m == 6 or self.__m == 9 or self.__m == 11) and self.__d < 30):
            self.__m += 1
            self.__d -= 30
        if (self.__m > 12):
            self.__a += 1
            self.__m -= 12
    def Mostrar(self):
        cadena = """\
        +--------------------------+
        | {:2}/{:2}/{:4} ---- {:2}:{:2}:{:2} |
        +--------------------------+\
        """
        print(cadena.format(self.__d, self.__m, self.__a, self.__h, self.__mi, self.__s))