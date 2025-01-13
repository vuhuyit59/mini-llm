import Env from '@/constants/env';
import {
    AiVideoRequestModel,
    CreateAiVideoRequestModel,
    Merge,
    SuccessResponse
} from '@/helpers/models';

type AiVideoRequestResponse = Merge<{ data: AiVideoRequestModel }, SuccessResponse>;

export const getAiVideoRequestDetail = async (
    userId: string,
    id: string,
) => {
    const queryPayload: any = {
        user_id: userId,
    };
    const queryParams = new URLSearchParams(queryPayload);
    let url = `${Env.BASE_URL}/api/v1/aiVideoRequest/${id}`;
    url = queryParams ? `${url}?${queryParams}` : url;
    const response = await fetch(url, {
        method: 'GET',
    });
    const response_json: AiVideoRequestResponse = await response.json();
    return response_json;
};


export const createAiVideoRequest = async (payload: CreateAiVideoRequestModel) => {
    const response = await fetch(`${Env.BASE_URL}/api/v1/aiVideoRequest`, {
        method: 'POST',
        body: JSON.stringify(payload),
    });
    const response_json: AiVideoRequestResponse = await response.json();
    return response_json;
};