from api.survey.enums.base import BaseEnum


class SurveyStatusEnum(BaseEnum):
    Draft: str = 'Draft'
    Published: str = 'Published'
    Archived: str = 'Archived'
    Deleted: str = 'Deleted'


class QuestionTypeEnum(BaseEnum):
    Text: str = 'text'
    Number: str = 'number'
    PositiveNumber: str = 'positive_number'
    SingleSelect: str = 'single_select'
    MultipleSelect: str = 'multiple_select'
    MultipleChoice: str = 'multiple_choice'
    Email: str = 'email'
    PhoneNumber: str = 'phone_number'
    Image: str = 'image'
    File: str = 'file'
