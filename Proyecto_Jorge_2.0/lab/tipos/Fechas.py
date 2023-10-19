'''
Created on 17 oct 2023

@author: Jorge-Feo
'''

from __future__ import annotations
from dataclasses import dataclass
@dataclass (order=True, frozen=True)
class Fecha:
    # Lista auxiliar para obtener el nombre del mes
    nombres_meses = [
        "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
        "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
    ]
    
    # Lista auxiliar para obtener el nombre del día de la semana
    nombres_dias_semana = [
        "Sábado", "Domingo", "Lunes", "Martes", "Miércoles", "Jueves", "Viernes"
    ]

    def __init__(self, año, mes, dia):
        self._año = año
        self._mes = mes
        self._dia = dia

    @property
    def año(self):
        return self._año

    @property
    def mes(self):
        return self._mes

    @property
    def dia(self):
        return self._dia

    @property
    def nombre_mes(self):
        return Fecha.nombres_meses[self._mes - 1]

    @property
    def dia_semana(self):
        return Fecha.nombres_dias_semana[self.zeller()]

    def zeller(self):
        # Implementación del algoritmo de Zeller
        m = (self._mes - 3) % 12 + 1
        j = self._año // 100
        k = self._año % 100
        return (self._dia + (13 * (m + 1)) // 5 + k + k // 4 + j // 4 - 2 * j) % 7

    def sumar_días(self, num_dias):
        from datetime import timedelta
        from datetime import date

        fecha = date(self._año, self._mes, self._dia)
        nueva_fecha = fecha + timedelta(days=num_dias)

        return Fecha(nueva_fecha.year, nueva_fecha.month, nueva_fecha.day)

    def restar_días(self, num_dias):
        return self.sumar_días(-num_dias)

    def diferencia_en_dias(self, otra_fecha):
        from datetime import date

        fecha1 = date(self._año, self._mes, self._dia)
        fecha2 = date(otra_fecha.año, otra_fecha.mes, otra_fecha.dia)
        
        return abs((fecha1 - fecha2).days)
    
    @staticmethod
    def es_año_bisiesto(año: int) -> bool:
        if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
            return True
        else:
            return False
    @staticmethod
    def días_en_mes(año: int, mes: int) -> int:
        if mes < 1 or mes > 12:
            return 0
        if mes == 2:
            if Fecha.es_año_bisiesto(año):
                return 29
            else:
                return 28
        elif mes in [4, 6, 9, 11]:
            return 30
        else:
            return 31
    
    @staticmethod
    def parse2(fecha_str: str):
        try:
            if fecha_str.startswith("[") and fecha_str.endswith("]"):
                # Eliminar los corchetes "[" y "]" del formato
                fecha_str = fecha_str[1:-1]

                # Dividir la cadena en partes usando "/" como separador
                partes = fecha_str.split("/")
                if len(partes) == 3:
                    día = int(partes[0])
                    mes = int(partes[1])
                    año = int(partes[2])
                    
                    if 1 <= mes <= 12 and 1 <= día <= Fecha.días_en_mes(año, mes):
                        return Fecha(año, mes, día)
        
        except (ValueError, IndexError):
            pass
        
        return None
