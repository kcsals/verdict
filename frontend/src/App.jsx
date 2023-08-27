import Route from "./components/Route";
import MoviePage from './pages/MoviePage';
import GamePage from './pages/GamePage';
import ShowPage from './pages/ShowPage';
import HardwarePage from './pages/HardwarePage';
import Navbar from "./pages/NavbarPage";
import LandingPage from "./pages/LandingPage";


function App() {

  return(
    <div className="bg-gray-200 h-screen w-full">
      <div className="flex space-x-4 text-center h-16">AD</div>
      <Navbar />
      <div className="flex space-x-4 text-center h-16"></div>
      
      <div>
        <Route path="/">
          <LandingPage />
        </Route>
        <Route path="/movies">
          <MoviePage />
        </Route>
        <Route path="/shows">
          <ShowPage />
        </Route>
        <Route path="/games">
          <GamePage />
        </Route>
        <Route path="/hardware">
          <HardwarePage />
        </Route>
      </div>
    </div>
    
  )
}

export default App;

