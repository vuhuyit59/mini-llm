interface AiVideoRequestModel {
  id: number;
  status: string;
  input_sample: string;
  user_id: string;
  output_video_url?: string;
  image_url?: string;
  process_percent: number;
}

interface CreateAiVideoRequestModel {
  input_sample: string;
  user_id: string;
}

export type {AiVideoRequestModel, CreateAiVideoRequestModel};