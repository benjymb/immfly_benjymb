from enum import Enum

class BaseEnum(Enum):
    @classmethod
    def choices(cls):
        return [
            (member.value, member.name)
            for member in cls
        ] 

class LANGUAGES(BaseEnum):
    SPANISH = 'ES'
    ENGLISH = 'EN'
    CATALAN = 'CA'
    PORTUGUESE = 'PT'

    

class METADATA_TYPES(BaseEnum):
    TYPE_1 = 'TYPE 1'
    TYPE_2 = 'TYPE 2'