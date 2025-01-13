import fetchJson from '@/utils/fetchJson';
import configs from '@/constants/env';
import {NextApiRequest, NextApiResponse} from 'next';
import {SuccessPagingResponse, SuccessResponse} from '@/helpers/models';

type allowMethodType = 'get' | 'put' | 'post' | 'delete';

export const handleRouteApi = async (
  req: NextApiRequest,
  res: NextApiResponse,
  path: string,
  allowMethod: allowMethodType[] = ['get'],
  noJson?: boolean,
) => {
  let header = req.headers || {};
  const init: {[key: string]: any} = {
    method: req.method,
    headers: {
      'Content-Type': 'application/json',
    },
  };
  const reqMethod = req.method?.toLowerCase();
  if (reqMethod != 'get') {
    init.body = req.body;
  }
  if (!reqMethod || allowMethod.indexOf(reqMethod as allowMethodType) < 0) {
    res.statusCode = 405;
    res.send({success: false});
  }
  let queryParams: any = '';
  if (req.url?.includes('?')) {
    queryParams = req.url?.split('?').pop();
  }
  let url = `${configs.API_URL}/${path}`;
  if (queryParams) {
    url = url.includes('?') ? `${url}&${queryParams}` : `${url}?${queryParams}`;
  }
  try {
    const response: SuccessResponse | SuccessPagingResponse | string = await fetchJson(
      url,
      init,
      noJson
    );
    res.statusCode = 200;
    res.send(response);
  } catch (e: any) {
    console.log('err', e);
    res.statusCode = e.response?.status || 500;
    res.statusMessage = e.response?.statusText || 'Internal Server Error';
    res.send(e.response);
  }
};
