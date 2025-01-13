import {NextApiRequest, NextApiResponse} from 'next';
import {handleRouteApi} from '@/helpers/api/nextApiRouteHandler';

async function aiVideoRequestsRouter(req: NextApiRequest, res: NextApiResponse) {
  await handleRouteApi(req, res, `v1/ai_video_request/${req.query.id}`, ['get']);
}

export default aiVideoRequestsRouter;
