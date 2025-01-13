from typing import Union, Generic, TypeVar, List, Optional

from fastapi.responses import JSONResponse
from pydantic.generics import GenericModel

DataType = TypeVar("DataType")


class BaseResponseModel(GenericModel):
    code: int
    message: str


class SuccessResponseModel(BaseResponseModel, Generic[DataType]):
    data: Optional[DataType] = None


class SuccessPagingResponseModel(BaseResponseModel, Generic[DataType]):
    data: Optional[DataType] = None
    page: int
    total: int
    page_size: int


class FailedResponseModel(BaseResponseModel):
    errors: List[object]


def response_success(data: Union[List, object], message: str = 'Success'):
    return JSONResponse(
        content={
            'code': 200,
            'data': data,
            'message': message
        }
    )


def response_page_success(data: Union[List, object], page: int, total: int,
                          page_size: int, message: str = 'Success'):
    return JSONResponse(
        content={
            'code': 200,
            'data': data,
            'message': message,
            'total': total,
            'page': page,
            'page_size': page_size,
        }
    )


def response_failed(error: List = None, code: Union[str, int] = 400,
                    message: str = 'Failed',
                    status_code: Union[str, int] = 400):
    return JSONResponse(
        status_code=status_code,
        content={
            'code': code,
            'errors': error,
            'message': message
        }
    )
