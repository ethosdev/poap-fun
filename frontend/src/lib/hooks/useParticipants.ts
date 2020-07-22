// @ts-nocheck
import { useQuery } from 'react-query';

// Lib
import { api, endpoints } from 'lib/api';
import { ParticipantsResponse } from 'lib/types';

type ParticipantParams = {
  raffle?: number | null;
};

export const isParamsEnabled = (params: Params) => Object.values(params).every(Boolean);

const fetchParticipants = (key: string, params: ParticipantParams): Promise<ParticipantsResponse> =>
  api().url(endpoints.fun.participants.all(params)).get().json();

export const useParticipants = (params: ParticipantParams) => {
  // react query
  return useQuery(['participants', params], fetchParticipants, { enabled: isParamsEnabled(params) });
};
