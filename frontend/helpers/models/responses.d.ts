interface BaseResponse {
  code: number;
  message: string;
}

interface SuccessResponse extends BaseResponse {
  data: any;
}

interface SuccessPagingResponse extends BaseResponse {
  page: number;
  total: number;
  page_size: number;
}

interface FailedResponse extends BaseResponse {
  errors: any;
}

type Omit<T, K extends keyof T> = Pick<T, Exclude<keyof T, K>>;
type Merge<M, N> = Omit<M, Extract<keyof M, keyof N>> & N;

export {Merge, SuccessResponse, SuccessPagingResponse, FailedResponse};
