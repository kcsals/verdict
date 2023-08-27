import axios from 'axios';

const BASE_URL = 'http://localhost:8000';

export const fetchGames = () => {
    return axios.get(`${BASE_URL}/games/api/games/`);
}

export const fetchGameById = (id) => {
    return axios.get(`${BASE_URL}/games/api/games/${id}/`);
}

// ... any other game-related API calls.
