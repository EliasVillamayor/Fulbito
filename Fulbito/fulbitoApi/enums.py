from enum import Enum

class UserType(Enum):
    ADMIN = 'Admin'
    USER = 'User'

class PitchSize(Enum):
    FIVE = 'Futbol 5'
    SIX = 'Futbol 6'
    SEVEN = 'Futbol 7'
    NINE = 'Futbol 9'
    ELEVEN = 'Futbol 11'

class PitchStatus(Enum):
    AVAILABLE = 'Disponible'
    MAINTENANCE = 'En mantenimiento'

class ReserveStatus(Enum):
    PENDING = 'Pendiente'
    CONFIRMED = 'Confirmada'

class PaymentType(Enum):
    CASH = 'Efectivo'
    TRANSFER = 'Transferencia'

class TournamentStatus(Enum):
    IN_PROGRESS = 'En progreso'
    FINISHED = 'Finalizado'
