from sqlalchemy import Column, Integer, String, Enum, DateTime, Boolean
from sqlalchemy.dialects.mysql import DECIMAL
from sqlalchemy.orm import relationship
from config.db import Base
import enum

class ViaAdministracion(enum.Enum):
    Oral = "Oral"
    Intravenoso = "Intravenoso"
    Rectal = "Rectal"
    Cutaneo = "Cutáneo"
    Subcutaneo = "Subcutáneo"
    Oftalmica = "Oftálmica"
    Otica = "Ótica"
    Nasal = "Nasal"
    Topica = "Tópica"
    Parenteral = "Parenteral"

class Presentacion(enum.Enum):
    Comprimidos = "Comprimidos"
    Grageas = "Grageas"
    Capsulas = "Cápsulas"
    Jarabes = "Jarabes"
    Gotas = "Gotas"
    Solucion = "Solución"
    Pomada = "Pomada"
    Jabon = "Jabón"
    Supositorios = "Supositorios"
    Viales = "Viales"

class Tipo(enum.Enum):
    Analgesicos = "Analgésicos"
    Antibioticos = "Antibióticos"
    Antidepresivos = "Antidepresivos"
    Antihistaminicos = "Antihistamínicos"
    Antiinflamatorios = "Antiinflamatorios"
    Antipsicoticos = "Antipsicóticos"

class Medicamento(Base):
    __tablename__ = "tbc_medicamentos"
    
    ID = Column(Integer, primary_key=True, index=True)
    Nombre_comercial = Column(String(80))
    Nombre_generico = Column(String(80))
    Via_administracion = Column(Enum(ViaAdministracion))
    Presentacion = Column(Enum(Presentacion))
    Tipo = Column(Enum(Tipo))
    Cantidad = Column(DECIMAL(10, 2))
    Volumen = Column(DECIMAL(10, 2), nullable=True)
    Estatus = Column(Boolean, default=False)
    Fecha_registro = Column(DateTime)
    Fecha_actualizacion = Column(DateTime)
