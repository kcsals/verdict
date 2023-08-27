import axios from 'axios'

const searchArticles = async () => {
  const response = await axios.get('https://swapi.dev/api/people/1/')
  console.log(response)
  return response
}

export default searchArticles