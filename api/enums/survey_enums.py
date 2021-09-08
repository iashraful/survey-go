from enum import Enum


class SurveyStatusEnum(Enum):
    Draft: str = 'Draft'
    Published: str = 'Published'
    Archived: str = 'Archived'


class QuestionTypeEnum(Enum):
    Text: str = 'text'
    Number: str = 'number'
    SingleSelect: str = 'single_select'
    MultipleSelect: str = 'multiple_select'
    MultipleChoice: str = 'multiple_choice'
    Email: str = 'email'
    PhoneNumber: str = 'phone_number'
    Image: str = 'image'
    File: str = 'file'

