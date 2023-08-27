import axios from 'axios';

const BASE_URL = 'http://localhost:8000';

export const fetchMovies = () => {
    return axios.get(`${BASE_URL}/movies/api/movies/`);
}

export const fetchMovieById = (id) => {
    return axios.get(`${BASE_URL}/movies/api/movies/${id}/`);
}

// ... any other movie-related API calls.
