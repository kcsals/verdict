import axios from 'axios';

const BASE_URL = 'http://localhost:8000/';  // Adjust this if your backend URL is different

const instance = axios.create({
  baseURL: BASE_URL,
  timeout: 10000,  // 10 seconds; adjust as needed
});

// Function to fetch the list of games
export const fetchGames = async () => {
    try {
        const response = await instance.get('/games/');
        return response.data;
    } catch (error) {
        console.error("There was a problem with the fetch operation:", error.message);
    }
};

// Function to fetch a specific game by its slug or ID
export const fetchGameBySlug = async (slug) => {
    try {
        const response = await instance.get(`/games/${slug}/`);
        return response.data;
    } catch (error) {
        console.error("There was a problem with the fetch operation:", error.message);
    }
};

// Function to fetch the list of trending games
export const fetchTrending = async () => {
  try {
    const response = await instance.get('/games/trending/')
    return response.data
  } catch (error) {
    console.error("There was a problem with the fetch operation:", error.message)
  }
};




